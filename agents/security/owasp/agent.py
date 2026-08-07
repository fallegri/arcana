"""
OWASP Agent — Analizador de seguridad según OWASP Top 10.

Responsabilidades:
1. Escanear código Python por patrones inseguros
2. Detectar vulnerabilidades mapeadas al Top 10
3. Sugerir remediaciones específicas
4. Reportar score de seguridad
5. Emitir notas educativas por categoría

Principios SOLID:
- SRP: Solo analiza seguridad OWASP (no SOLID, no testing)
- OCP: Las reglas son extensibles (lista de patrones)
- DIP: No depende de herramientas externas directamente
"""

import ast
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List

from agents.base import AgentInput, AgentOutput, BaseAgent


@dataclass
class SecurityFinding:
    """Una vulnerabilidad detectada."""

    category: str  # A01-A10
    severity: str  # critical, high, medium, low
    file_path: str
    line_number: int
    description: str
    vulnerable_code: str
    remediation: str


@dataclass
class OWASPReport:
    """Reporte consolidado de seguridad."""

    findings: List[SecurityFinding] = field(default_factory=list)
    files_scanned: int = 0
    lines_scanned: int = 0

    @property
    def total_findings(self) -> int:
        return len(self.findings)

    @property
    def critical_count(self) -> int:
        return sum(1 for f in self.findings if f.severity == "critical")

    @property
    def high_count(self) -> int:
        return sum(1 for f in self.findings if f.severity == "high")

    @property
    def findings_by_category(self) -> Dict[str, int]:
        counts: Dict[str, int] = {}
        for f in self.findings:
            counts[f.category] = counts.get(f.category, 0) + 1
        return counts

    @property
    def security_score(self) -> float:
        """Score 0-100. Penaliza: critical=-20, high=-10, medium=-5."""
        score = 100.0
        for f in self.findings:
            if f.severity == "critical":
                score -= 20
            elif f.severity == "high":
                score -= 10
            elif f.severity == "medium":
                score -= 5
            else:
                score -= 2
        return max(0, score)


class OWASPAgent(BaseAgent):
    """
    Agente OWASP — Detecta vulnerabilidades del Top 10.

    Reglas de detección (patrones inseguros):
    - A01: Endpoints sin verificación de propiedad
    - A02: Passwords/secrets en texto plano
    - A03: SQL construido con f-strings o concatenación
    - A05: Secrets hardcoded, debug=True
    - A07: Login sin rate limiting
    - A09: Sin logging de eventos de seguridad
    - A10: Requests a URLs sin validación
    """

    # Patrones inseguros a detectar
    RULES = [
        {
            "category": "A02",
            "severity": "critical",
            "pattern": r'password\s*=\s*["\'][^"\']+["\']',
            "description": "Posible password hardcoded en el código",
            "remediation": "Usa variables de entorno o un vault de secretos. Nunca hardcodees passwords.",
        },
        {
            "category": "A05",
            "severity": "high",
            "pattern": r'(SECRET_KEY|API_KEY|TOKEN)\s*=\s*["\'][^"\']+["\']',
            "description": "Secret/API key hardcoded en código fuente",
            "remediation": "Mueve a variables de entorno (.env). Agrega .env a .gitignore.",
        },
        {
            "category": "A05",
            "severity": "medium",
            "pattern": r'debug\s*=\s*True',
            "description": "Debug mode activado — expone stack traces en producción",
            "remediation": "Usa debug=False en producción. Configúralo via variable de entorno.",
        },
        {
            "category": "A03",
            "severity": "critical",
            "pattern": r'(execute|raw)\s*\(\s*f["\']',
            "description": "SQL construido con f-string — vulnerable a SQL Injection",
            "remediation": "Usa SQLAlchemy ORM o queries parametrizadas. Nunca concatenes SQL.",
        },
        {
            "category": "A03",
            "severity": "critical",
            "pattern": r'\.execute\s*\(\s*["\'].*%s.*["\'].*%',
            "description": "SQL con formato % — vulnerable a SQL Injection",
            "remediation": "Usa queries parametrizadas con placeholders seguros.",
        },
        {
            "category": "A10",
            "severity": "high",
            "pattern": r'requests\.(get|post|put|delete)\s*\(\s*[a-zA-Z_]+\s*[,)]',
            "description": "Request HTTP a URL dinámica sin validación — posible SSRF",
            "remediation": "Valida la URL contra una allowlist de dominios permitidos.",
        },
        {
            "category": "A05",
            "severity": "medium",
            "pattern": r'allow_origins\s*=\s*\[\s*["\']\*["\']\s*\]',
            "description": "CORS con wildcard (*) — permite requests desde cualquier origen",
            "remediation": "Especifica los dominios exactos permitidos.",
        },
        {
            "category": "A02",
            "severity": "high",
            "pattern": r'algorithm\s*=\s*["\']none["\']',
            "description": "JWT con algorithm 'none' — sin firma criptográfica",
            "remediation": "Usa HS256 o RS256. Nunca 'none'.",
        },
    ]

    @property
    def name(self) -> str:
        return "owasp"

    @property
    def description(self) -> str:
        return (
            "Analiza código Python para detectar vulnerabilidades OWASP Top 10 "
            "y sugiere remediaciones específicas."
        )

    @property
    def phase(self) -> str:
        return "security"

    async def execute(self, input_data: AgentInput) -> AgentOutput:
        """Ejecuta el análisis de seguridad OWASP."""
        project_path = input_data.project_path
        report = self._scan_project(project_path)
        return self._build_output(report, input_data)

    def _scan_project(self, project_path: Path) -> OWASPReport:
        """Escanea todos los archivos Python del proyecto."""
        report = OWASPReport()

        python_files = list(project_path.rglob("*.py"))
        report.files_scanned = len(python_files)

        for py_file in python_files:
            if "__pycache__" in str(py_file):
                continue

            try:
                content = py_file.read_text(encoding="utf-8")
                lines = content.split("\n")
                report.lines_scanned += len(lines)

                # Escanear con regex patterns
                self._scan_with_patterns(content, lines, str(py_file), report)

                # Escanear con AST para análisis más profundo
                try:
                    tree = ast.parse(content)
                    self._scan_with_ast(tree, str(py_file), report)
                except SyntaxError:
                    pass

            except (UnicodeDecodeError, PermissionError):
                continue

        return report

    def _scan_with_patterns(
        self, content: str, lines: List[str], file_path: str, report: OWASPReport
    ):
        """Escanea usando patrones regex."""
        for rule in self.RULES:
            for i, line in enumerate(lines, 1):
                # Saltar comentarios y docstrings
                stripped = line.strip()
                if stripped.startswith("#") or stripped.startswith('"""') or stripped.startswith("'''"):
                    continue

                if re.search(rule["pattern"], line, re.IGNORECASE):
                    report.findings.append(SecurityFinding(
                        category=rule["category"],
                        severity=rule["severity"],
                        file_path=file_path,
                        line_number=i,
                        description=rule["description"],
                        vulnerable_code=line.strip()[:100],
                        remediation=rule["remediation"],
                    ))

    def _scan_with_ast(self, tree: ast.AST, file_path: str, report: OWASPReport):
        """Análisis AST para patrones más complejos."""
        for node in ast.walk(tree):
            # A01: Detectar queries sin filtro de user_id
            if isinstance(node, ast.Call):
                if hasattr(node.func, 'attr'):
                    # Detectar .execute() con strings formateados
                    if node.func.attr == "execute" and node.args:
                        arg = node.args[0]
                        if isinstance(arg, ast.JoinedStr):  # f-string
                            report.findings.append(SecurityFinding(
                                category="A03",
                                severity="critical",
                                file_path=file_path,
                                line_number=node.lineno,
                                description="SQL con f-string detectado via AST",
                                vulnerable_code=f"line {node.lineno}",
                                remediation="Usa SQLAlchemy ORM o queries parametrizadas.",
                            ))

    def _build_output(self, report: OWASPReport, input_data: AgentInput) -> AgentOutput:
        """Construye el AgentOutput final."""
        # Status basado en severidad
        if report.critical_count > 0:
            status = "error"
        elif report.high_count > 0:
            status = "warning"
        elif report.total_findings > 0:
            status = "warning"
        else:
            status = "success"

        # Métricas
        metrics: Dict[str, float] = {
            "owasp.files_scanned": report.files_scanned,
            "owasp.lines_scanned": report.lines_scanned,
            "owasp.total_findings": report.total_findings,
            "owasp.critical": report.critical_count,
            "owasp.high": report.high_count,
            "owasp.security_score": report.security_score,
        }

        # Recomendaciones
        recommendations = []
        for f in report.findings[:15]:
            recommendations.append(
                f"[{f.category}|{f.severity.upper()}] {f.file_path}:{f.line_number} "
                f"— {f.description}"
            )

        if report.total_findings == 0:
            recommendations.append(
                "✅ No se detectaron vulnerabilidades OWASP. "
                "Considera ejecutar también herramientas externas (bandit, semgrep)."
            )

        # Notas educativas
        educational_notes = self._generate_notes(report, input_data)

        return AgentOutput(
            agent_name=self.name,
            status=status,
            metrics=metrics,
            recommendations=recommendations,
            educational_notes=educational_notes,
        )

    def _generate_notes(self, report: OWASPReport, input_data: AgentInput) -> List[str]:
        """Genera notas educativas."""
        mode = input_data.context.educational_mode
        notes = []

        if mode == "beginner":
            notes = [
                f"🔒 Se escanearon {report.files_scanned} archivos buscando vulnerabilidades.",
                f"🏥 Score de seguridad: {report.security_score}/100",
            ]
            if report.critical_count > 0:
                notes.append(f"🚨 {report.critical_count} vulnerabilidad(es) CRÍTICA(S) encontrada(s)")
                notes.append("   Las vulnerabilidades críticas deben corregirse INMEDIATAMENTE.")
            if report.total_findings == 0:
                notes.append("✅ ¡No se detectaron vulnerabilidades! Buen trabajo.")
            notes.append("📖 Guía completa: docs/guides/OWASP-paso-a-paso.md")
        elif mode == "expert":
            notes.append(
                f"OWASP Score: {report.security_score}/100 | "
                f"Critical: {report.critical_count} | High: {report.high_count}"
            )
        else:
            notes = [
                f"Análisis OWASP: {report.security_score}/100",
                f"Findings: {report.total_findings} ({report.critical_count} critical, {report.high_count} high)",
                "Guía completa: docs/guides/OWASP-paso-a-paso.md",
            ]

        return notes


    # ═══════════════════════════════════════════════════════════════
    # FIX ENGINE — Auto-corrección de vulnerabilidades
    # ═══════════════════════════════════════════════════════════════

    @property
    def supports_fix(self) -> bool:
        return True

    async def fix(self, input_data: AgentInput, analysis: AgentOutput) -> "FixResult":
        """
        Aplica correcciones automáticas para vulnerabilidades OWASP detectadas.

        Estrategia de corrección por categoría:
        - A02 (Crypto): Reemplaza secrets hardcoded por os.environ.get()
        - A03 (Injection): Reemplaza f-strings SQL por placeholders
        - A05 (Misconfig): Cambia debug=True por debug=False, mueve secrets
        - A10 (SSRF): Agrega validación de URL
        """
        from agents.base import FixAction, FixResult
        import shutil

        project_path = input_data.project_path
        result = FixResult(agent_name=self.name)

        # Crear backup
        backup_dir = project_path / ".arcana_backup"
        backup_dir.mkdir(exist_ok=True)
        result.backup_path = backup_dir

        # Escanear para obtener findings detallados
        report = self._scan_project(project_path)

        for finding in report.findings:
            file_path = Path(finding.file_path)
            if not file_path.exists():
                continue

            content = file_path.read_text(encoding="utf-8")
            lines = content.split("\n")
            line_idx = finding.line_number - 1

            if line_idx >= len(lines):
                continue

            original_line = lines[line_idx]
            fixed_line = None

            # Aplicar fix según categoría
            if finding.category == "A05" and "debug" in original_line.lower():
                fixed_line = original_line.replace("True", "False").replace("true", "false")

            elif finding.category == "A05" and any(k in original_line for k in ["SECRET_KEY", "API_KEY", "TOKEN"]):
                # Extraer nombre de variable
                var_match = re.match(r'^(\s*)([\w]+)\s*=\s*["\'].*["\']', original_line)
                if var_match:
                    indent = var_match.group(1)
                    var_name = var_match.group(2)
                    fixed_line = f'{indent}{var_name} = os.environ.get("{var_name}", "CHANGE-ME-IN-ENV")'

            elif finding.category == "A02" and "password" in original_line.lower():
                var_match = re.match(r'^(\s*)([\w]+)\s*=\s*["\'].*["\']', original_line)
                if var_match:
                    indent = var_match.group(1)
                    var_name = var_match.group(2)
                    fixed_line = f'{indent}{var_name} = os.environ.get("{var_name.upper()}", "")'

            elif finding.category == "A03" and "execute" in original_line:
                # Marcar con comentario de advertencia (fix completo requiere refactor)
                fixed_line = f"{original_line}  # FIXME: SQL Injection — usar queries parametrizadas"

            elif finding.category == "A10" and "requests." in original_line:
                indent = len(original_line) - len(original_line.lstrip())
                spaces = " " * indent
                fixed_line = f"{spaces}# FIXME: Validar URL contra allowlist antes de hacer request\n{original_line}"

            # Aplicar fix
            if fixed_line and fixed_line != original_line:
                # Backup
                backup_file = backup_dir / file_path.name
                if not backup_file.exists():
                    shutil.copy2(file_path, backup_file)

                # Aplicar
                lines[line_idx] = fixed_line
                file_path.write_text("\n".join(lines), encoding="utf-8")

                result.fixes_applied.append(FixAction(
                    file_path=str(file_path),
                    line_number=finding.line_number,
                    original_code=original_line.strip(),
                    fixed_code=fixed_line.strip(),
                    description=f"[{finding.category}] {finding.description}",
                    principle=finding.category,
                    severity=finding.severity,
                ))

                if str(file_path) not in result.files_modified:
                    result.files_modified.append(str(file_path))
            else:
                result.fixes_skipped.append(
                    f"[{finding.category}] {finding.file_path}:{finding.line_number} — "
                    f"Requiere refactoring manual"
                )

        # Agregar import os si se usó os.environ
        if any("os.environ" in f.fixed_code for f in result.fixes_applied):
            for fpath in result.files_modified:
                p = Path(fpath)
                content = p.read_text(encoding="utf-8")
                if "import os" not in content:
                    content = "import os\n" + content
                    p.write_text(content, encoding="utf-8")

        return result
