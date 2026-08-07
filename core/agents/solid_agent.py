"""
SOLID Agent — Analizador de principios de diseño.

Responsabilidades:
1. Escanear archivos Python del proyecto
2. Detectar violaciones de cada principio SOLID
3. Sugerir refactorings específicos
4. Reportar métricas de calidad de diseño
5. Emitir notas educativas

Principios SOLID que ESTE agente cumple:
- SRP: Solo analiza SOLID (no testing, no seguridad)
- OCP: Los analizadores son extensibles (uno por principio)
- DIP: No depende de herramientas concretas de análisis
"""

import ast
import os
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional

from agents.base import AgentInput, AgentOutput, BaseAgent


@dataclass
class Violation:
    """Una violación detectada de un principio SOLID."""

    principle: str  # S, O, L, I, D
    file_path: str
    class_name: str
    description: str
    severity: str  # low, medium, high
    suggestion: str


@dataclass
class SOLIDReport:
    """Reporte consolidado del análisis SOLID."""

    violations: List[Violation] = field(default_factory=list)
    classes_analyzed: int = 0
    files_analyzed: int = 0

    @property
    def total_violations(self) -> int:
        return len(self.violations)

    @property
    def violations_by_principle(self) -> Dict[str, int]:
        counts = {"S": 0, "O": 0, "L": 0, "I": 0, "D": 0}
        for v in self.violations:
            counts[v.principle] = counts.get(v.principle, 0) + 1
        return counts

    @property
    def health_score(self) -> float:
        """Score de 0-100. Mayor = más saludable."""
        if self.classes_analyzed == 0:
            return 100.0
        violations_per_class = self.total_violations / self.classes_analyzed
        score = max(0, 100 - (violations_per_class * 25))
        return round(score, 1)


class SOLIDAgent(BaseAgent):
    """
    Agente que analiza código Python para detectar violaciones SOLID.

    Usa análisis estático (AST) para examinar:
    - Tamaño de clases y métodos (SRP)
    - Patrones if/elif extensos (OCP)
    - Herencia con NotImplementedError (LSP)
    - Clases con muchos métodos abstractos (ISP)
    - Imports y dependencias hardcoded (DIP)
    """

    @property
    def name(self) -> str:
        return "solid"

    @property
    def description(self) -> str:
        return (
            "Analiza código Python para detectar violaciones de SOLID "
            "y sugiere refactorings específicos."
        )

    @property
    def phase(self) -> str:
        return "implementation"

    async def execute(self, input_data: AgentInput) -> AgentOutput:
        """Ejecuta el análisis SOLID."""
        project_path = input_data.project_path
        report = self._analyze_project(project_path)
        return self._build_output(report, input_data)

    def _analyze_project(self, project_path: Path) -> SOLIDReport:
        """Analiza todos los archivos Python del proyecto."""
        report = SOLIDReport()

        python_files = list(project_path.rglob("*.py"))
        report.files_analyzed = len(python_files)

        for py_file in python_files:
            # Saltar tests y __pycache__
            if "__pycache__" in str(py_file) or "test_" in py_file.name:
                continue

            try:
                source = py_file.read_text(encoding="utf-8")
                tree = ast.parse(source)
                self._analyze_file(tree, str(py_file), report)
            except (SyntaxError, UnicodeDecodeError):
                continue

        return report

    def _analyze_file(self, tree: ast.AST, file_path: str, report: SOLIDReport):
        """Analiza un archivo AST."""
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                report.classes_analyzed += 1
                self._check_srp(node, file_path, report)
                self._check_ocp(node, file_path, report)
                self._check_lsp(node, file_path, report)
                self._check_isp(node, file_path, report)
                self._check_dip(node, file_path, report)

    def _check_srp(self, node: ast.ClassDef, file_path: str, report: SOLIDReport):
        """
        Detecta violaciones de SRP:
        - Clases con demasiados métodos (>10)
        - Métodos demasiado largos (>30 líneas)
        - Nombres con "And", "Or", "Manager" (múltiples responsabilidades)
        """
        methods = [n for n in node.body if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))]

        # Demasiados métodos públicos
        public_methods = [m for m in methods if not m.name.startswith("_")]
        if len(public_methods) > 10:
            report.violations.append(Violation(
                principle="S",
                file_path=file_path,
                class_name=node.name,
                description=f"Clase con {len(public_methods)} métodos públicos (máx recomendado: 10)",
                severity="medium",
                suggestion="Considera dividir en clases más pequeñas, cada una con una responsabilidad.",
            ))

        # Métodos muy largos
        for method in methods:
            method_lines = (method.end_lineno or 0) - method.lineno
            if method_lines > 30:
                report.violations.append(Violation(
                    principle="S",
                    file_path=file_path,
                    class_name=f"{node.name}.{method.name}",
                    description=f"Método con {method_lines} líneas (máx recomendado: 30)",
                    severity="low",
                    suggestion="Extrae lógica a métodos privados o clases helper.",
                ))

        # Nombres sospechosos
        suspicious = ["Manager", "Handler", "Processor", "Controller"]
        for word in suspicious:
            if word in node.name and len(public_methods) > 5:
                report.violations.append(Violation(
                    principle="S",
                    file_path=file_path,
                    class_name=node.name,
                    description=f"Nombre '{node.name}' sugiere múltiples responsabilidades",
                    severity="low",
                    suggestion=f"Renombra para ser más específico o divide la clase.",
                ))
                break

    def _check_ocp(self, node: ast.ClassDef, file_path: str, report: SOLIDReport):
        """
        Detecta violaciones de OCP:
        - Cadenas largas de if/elif (>4 ramas)
        - Pattern matching extenso sin polimorfismo
        """
        for method in ast.walk(node):
            if isinstance(method, (ast.FunctionDef, ast.AsyncFunctionDef)):
                if_count = sum(1 for n in ast.walk(method) if isinstance(n, ast.If))
                if if_count > 4:
                    report.violations.append(Violation(
                        principle="O",
                        file_path=file_path,
                        class_name=f"{node.name}.{method.name}",
                        description=f"Método con {if_count} condicionales — difícil de extender",
                        severity="medium",
                        suggestion="Usa polimorfismo, strategy pattern o un registry en lugar de if/elif.",
                    ))

    def _check_lsp(self, node: ast.ClassDef, file_path: str, report: SOLIDReport):
        """
        Detecta violaciones de LSP:
        - Métodos que lanzan NotImplementedError (refused bequest)
        """
        for method in node.body:
            if isinstance(method, (ast.FunctionDef, ast.AsyncFunctionDef)):
                for child in ast.walk(method):
                    if isinstance(child, ast.Raise):
                        if isinstance(child.exc, ast.Call):
                            if hasattr(child.exc.func, 'id'):
                                if child.exc.func.id == "NotImplementedError":
                                    report.violations.append(Violation(
                                        principle="L",
                                        file_path=file_path,
                                        class_name=f"{node.name}.{method.name}",
                                        description="Lanza NotImplementedError — el hijo no cumple el contrato del padre",
                                        severity="high",
                                        suggestion="Si la subclase no puede implementar este método, la jerarquía está mal diseñada. Usa composición o separa la interfaz (ISP).",
                                    ))

    def _check_isp(self, node: ast.ClassDef, file_path: str, report: SOLIDReport):
        """
        Detecta violaciones de ISP:
        - Clases abstractas con demasiados métodos abstractos (>5)
        """
        abstract_methods = []
        for method in node.body:
            if isinstance(method, (ast.FunctionDef, ast.AsyncFunctionDef)):
                for decorator in method.decorator_list:
                    if isinstance(decorator, ast.Name) and decorator.id == "abstractmethod":
                        abstract_methods.append(method.name)
                    elif isinstance(decorator, ast.Attribute) and decorator.attr == "abstractmethod":
                        abstract_methods.append(method.name)

        if len(abstract_methods) > 5:
            report.violations.append(Violation(
                principle="I",
                file_path=file_path,
                class_name=node.name,
                description=f"Interfaz con {len(abstract_methods)} métodos abstractos — posiblemente demasiado amplia",
                severity="medium",
                suggestion="Divide en interfaces más pequeñas y específicas.",
            ))

    def _check_dip(self, node: ast.ClassDef, file_path: str, report: SOLIDReport):
        """
        Detecta violaciones de DIP:
        - Imports dentro de __init__ (dependencias hardcoded)
        - Creación de objetos concretos dentro de __init__
        """
        for method in node.body:
            if isinstance(method, (ast.FunctionDef, ast.AsyncFunctionDef)):
                if method.name == "__init__":
                    # Buscar creación de dependencias dentro del init
                    for child in ast.walk(method):
                        if isinstance(child, ast.Call):
                            if hasattr(child.func, 'id'):
                                concrete_hints = ["connect", "create_engine", "SMTP", "Client"]
                                if child.func.id in concrete_hints:
                                    report.violations.append(Violation(
                                        principle="D",
                                        file_path=file_path,
                                        class_name=node.name,
                                        description=f"Crea dependencia concreta '{child.func.id}()' internamente",
                                        severity="high",
                                        suggestion="Recibe la dependencia como parámetro del constructor (inyección). Esto facilita testing con mocks.",
                                    ))

    def _build_output(self, report: SOLIDReport, input_data: AgentInput) -> AgentOutput:
        """Construye el AgentOutput final."""
        status = "success" if report.total_violations == 0 else "warning"
        if any(v.severity == "high" for v in report.violations):
            status = "warning"

        metrics: Dict[str, float] = {
            "solid.classes_analyzed": report.classes_analyzed,
            "solid.files_analyzed": report.files_analyzed,
            "solid.total_violations": report.total_violations,
            "solid.health_score": report.health_score,
            **{f"solid.violations_{k}": v for k, v in report.violations_by_principle.items()},
        }

        recommendations = []
        for v in report.violations:
            recommendations.append(
                f"[{v.principle}] {v.class_name}: {v.description} → {v.suggestion}"
            )

        educational_notes = self._generate_notes(report, input_data)

        return AgentOutput(
            agent_name=self.name,
            status=status,
            metrics=metrics,
            recommendations=recommendations[:20],
            educational_notes=educational_notes,
        )

    def _generate_notes(self, report: SOLIDReport, input_data: AgentInput) -> List[str]:
        """Genera notas educativas."""
        mode = input_data.context.educational_mode
        notes = []

        if mode == "beginner":
            notes = [
                f"📊 Se analizaron {report.classes_analyzed} clases en {report.files_analyzed} archivos.",
                f"🏥 Salud SOLID: {report.health_score}/100",
            ]
            if report.violations_by_principle["S"] > 0:
                notes.append("⚠️ SRP: Hay clases que hacen demasiado → divídelas")
            if report.violations_by_principle["D"] > 0:
                notes.append("⚠️ DIP: Hay dependencias hardcoded → usa inyección")
            notes.append("📖 Guía completa: docs/guides/SOLID-paso-a-paso.md")
        elif mode == "expert":
            notes.append(f"SOLID Score: {report.health_score}/100 | Violations: {report.total_violations}")
        else:
            notes = [
                f"Análisis SOLID: {report.health_score}/100 ({report.total_violations} violaciones)",
                "Guía completa: docs/guides/SOLID-paso-a-paso.md",
            ]

        return notes


    # ═══════════════════════════════════════════════════════════════
    # FIX ENGINE — Auto-corrección de violaciones SOLID
    # ═══════════════════════════════════════════════════════════════

    @property
    def supports_fix(self) -> bool:
        return True

    async def fix(self, input_data: AgentInput, analysis: AgentOutput) -> "FixResult":
        """
        Aplica correcciones automáticas para violaciones SOLID.

        Estrategia:
        - SRP (métodos largos): Agrega comentario TODO con sugerencia de extracción
        - SRP (nombres): Agrega comentario sugiriendo renombrar
        - OCP (if/elif): Agrega comentario sugiriendo strategy/registry pattern
        - DIP (dependencias): Agrega comentario sugiriendo inyección

        NOTA: SOLID requiere refactoring estructural que no se puede hacer
        automáticamente de forma segura. Los fixes son marcadores + sugerencias.
        La corrección completa requiere intervención humana (o IA asistida).
        """
        from agents.base import FixAction, FixResult
        import shutil

        project_path = input_data.project_path
        result = FixResult(agent_name=self.name)

        # Backup
        backup_dir = project_path / ".arcana_backup"
        backup_dir.mkdir(exist_ok=True)
        result.backup_path = backup_dir

        # Re-analizar para obtener violaciones frescas
        report = self._analyze_project(project_path)

        for violation in report.violations:
            file_path = Path(violation.file_path)
            if not file_path.exists():
                continue

            content = file_path.read_text(encoding="utf-8")
            lines = content.split("\n")

            # Buscar la clase/método mencionado
            target_name = violation.class_name.split(".")[-1]  # Método o clase
            fix_applied = False

            for i, line in enumerate(lines):
                if f"def {target_name}" in line or f"class {target_name}" in line:
                    indent = len(line) - len(line.lstrip())
                    spaces = " " * indent

                    # Verificar que no tiene ya un FIXME de Arcana
                    if i > 0 and "# ARCANA-FIX" in lines[i - 1]:
                        break

                    # Agregar comentario de fix según principio
                    if violation.principle == "S":
                        fix_comment = (
                            f"{spaces}# ARCANA-FIX [SRP]: {violation.description}\n"
                            f"{spaces}# SUGERENCIA: {violation.suggestion}\n"
                        )
                    elif violation.principle == "O":
                        fix_comment = (
                            f"{spaces}# ARCANA-FIX [OCP]: {violation.description}\n"
                            f"{spaces}# SUGERENCIA: Reemplazar if/elif con Strategy Pattern o Registry\n"
                        )
                    elif violation.principle == "D":
                        fix_comment = (
                            f"{spaces}# ARCANA-FIX [DIP]: {violation.description}\n"
                            f"{spaces}# SUGERENCIA: Recibir como parámetro del __init__() en vez de crear internamente\n"
                        )
                    elif violation.principle == "L":
                        fix_comment = (
                            f"{spaces}# ARCANA-FIX [LSP]: {violation.description}\n"
                            f"{spaces}# SUGERENCIA: Si no puedes implementar este método, la herencia está mal diseñada\n"
                        )
                    else:
                        fix_comment = (
                            f"{spaces}# ARCANA-FIX [{violation.principle}]: {violation.description}\n"
                            f"{spaces}# SUGERENCIA: {violation.suggestion}\n"
                        )

                    # Backup
                    backup_file = backup_dir / file_path.name
                    if not backup_file.exists():
                        shutil.copy2(file_path, backup_file)

                    # Insertar comentario antes de la línea
                    lines.insert(i, fix_comment.rstrip())
                    file_path.write_text("\n".join(lines), encoding="utf-8")

                    result.fixes_applied.append(FixAction(
                        file_path=str(file_path),
                        line_number=i + 1,
                        original_code=line.strip(),
                        fixed_code=f"[Comentario ARCANA-FIX agregado] {violation.suggestion}",
                        description=violation.description,
                        principle=violation.principle,
                        severity=violation.severity,
                    ))

                    if str(file_path) not in result.files_modified:
                        result.files_modified.append(str(file_path))

                    fix_applied = True
                    break

            if not fix_applied:
                result.fixes_skipped.append(
                    f"[{violation.principle}] {violation.class_name}: No se encontró el target para anotar"
                )

        return result
