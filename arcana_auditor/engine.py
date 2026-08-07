"""
Auditor Engine — Motor de análisis y corrección.

Este motor orquesta los agentes de análisis (SOLID, OWASP)
y aplica los umbrales NO negociables definidos en core/config.

No acepta configuración del usuario para los criterios.
El usuario solo decide:
- Qué proyecto analizar
- Si quiere fix o no
- Qué formato de reporte
"""

import sys
from pathlib import Path
from typing import Optional

sys.path.insert(0, str(Path(__file__).parent.parent))

from core.schemas.contracts import AnalysisResult, Finding, FixResult, FixAction
from core.config import THRESHOLDS
from core.agents.base import AgentInput, SharedContext


class AuditorEngine:
    """
    Motor del Auditor — Detectar, Corregir (opcional), Reportar.

    Personalidad: Juez imparcial.
    "No me importa tu opinión. El estándar dice X. Punto."
    """

    async def analyze(self, project_path: Path) -> AnalysisResult:
        """
        Analiza el proyecto contra estándares NO negociables.

        Returns:
            AnalysisResult con scores, findings y veredicto
        """
        from core.agents.solid_agent import SOLIDAgent
        from core.agents.owasp_agent import OWASPAgent

        context = SharedContext(project_path=project_path, educational_mode="expert")
        input_data = AgentInput(
            phase="audit", project_path=project_path,
            config={}, context=context, previous_results=[]
        )

        # Ejecutar agentes
        solid_agent = SOLIDAgent()
        solid_output = await solid_agent.execute(input_data)

        owasp_agent = OWASPAgent()
        owasp_output = await owasp_agent.execute(input_data)

        # Construir resultado
        solid_score = solid_output.metrics.get("solid.health_score", 0)
        owasp_score = owasp_output.metrics.get("owasp.security_score", 0)

        # Construir findings
        findings = []
        finding_id = 1

        for rec in owasp_output.recommendations:
            if rec.startswith("✅"):
                continue
            severity = "critical" if "CRITICAL" in rec else "high" if "HIGH" in rec else "medium"
            findings.append(Finding(
                id=f"HAL-{finding_id:03d}",
                category=self._extract_owasp_cat(rec),
                severity=severity,
                description=rec,
                file_path=str(project_path),
                line_number=0,
                evidence=rec,
                remediation="Ver guía OWASP en docs/guides/OWASP-paso-a-paso.md",
                iso27001_control=self._map_iso27001(rec),
                cobit_objective=self._map_cobit(rec),
            ))
            finding_id += 1

        for rec in solid_output.recommendations:
            findings.append(Finding(
                id=f"HAL-{finding_id:03d}",
                category="SOLID",
                severity="medium",
                description=rec,
                file_path=str(project_path),
                line_number=0,
                evidence=rec,
                remediation="Ver guía SOLID en docs/guides/SOLID-paso-a-paso.md",
                iso27001_control="A.14.2 — Seguridad en desarrollo",
                cobit_objective="BAI03 — Gestionar soluciones",
            ))
            finding_id += 1

        # Determinar conformidad (NO negociable)
        solid_pass = solid_score >= THRESHOLDS["solid_min_score"]
        owasp_pass = owasp_score >= THRESHOLDS["owasp_min_score"]
        critical_pass = sum(1 for f in findings if f.severity == "critical") <= THRESHOLDS["owasp_critical_max"]

        if solid_pass and owasp_pass and critical_pass:
            status = "CONFORME"
        elif solid_pass or owasp_pass:
            status = "PARCIALMENTE CONFORME"
        else:
            status = "NO CONFORME"

        return AnalysisResult(
            project_path=str(project_path),
            scores={"solid": solid_score, "owasp": owasp_score},
            findings=findings,
            overall_status=status,
            recommendations=solid_output.recommendations + owasp_output.recommendations,
        )

    async def fix(self, project_path: Path, analysis: AnalysisResult) -> FixResult:
        """
        Aplica correcciones automáticas.
        Solo se ejecuta si el usuario lo pidió explícitamente (--fix).
        """
        from core.agents.solid_agent import SOLIDAgent
        from core.agents.owasp_agent import OWASPAgent
        from core.agents.base import AgentInput, SharedContext

        context = SharedContext(project_path=project_path, educational_mode="expert")
        input_data = AgentInput(
            phase="fix", project_path=project_path,
            config={}, context=context, previous_results=[]
        )

        all_fixes = []
        all_files = []

        # Fix OWASP
        owasp_agent = OWASPAgent()
        owasp_output = await owasp_agent.execute(input_data)
        if owasp_agent.supports_fix and owasp_output.status != "success":
            owasp_fix = await owasp_agent.fix(input_data, owasp_output)
            if owasp_fix:
                for fa in owasp_fix.fixes_applied:
                    all_fixes.append(FixAction(
                        file_path=fa.file_path,
                        line_number=fa.line_number,
                        original_code=fa.original_code,
                        fixed_code=fa.fixed_code,
                        description=fa.description,
                        category=fa.principle,
                        severity=fa.severity,
                    ))
                all_files.extend(owasp_fix.files_modified)

        # Fix SOLID
        solid_agent = SOLIDAgent()
        solid_output = await solid_agent.execute(input_data)
        if solid_agent.supports_fix and solid_output.status != "success":
            solid_fix = await solid_agent.fix(input_data, solid_output)
            if solid_fix:
                for fa in solid_fix.fixes_applied:
                    all_fixes.append(FixAction(
                        file_path=fa.file_path,
                        line_number=fa.line_number,
                        original_code=fa.original_code,
                        fixed_code=fa.fixed_code,
                        description=fa.description,
                        category=fa.principle,
                        severity=fa.severity,
                    ))
                all_files.extend(solid_fix.files_modified)

        return FixResult(
            fixes_applied=all_fixes,
            files_modified=list(set(all_files)),
            pre_scores=analysis.scores,
        )

    def generate_report(self, project_path: Path, result: AnalysisResult, fmt: str, fix_result: "FixResult" = None) -> Path:
        """
        Genera reporte de auditoría DETALLADO.

        Modo auditoría (sin fix):
        - Hallazgos detallados por archivo → clase → método
        - Severidad, descripción, código vulnerable, remediación sugerida

        Modo fix (con fix):
        - Todo lo anterior +
        - Qué se hizo para corregir cada hallazgo
        - Código original vs código corregido
        - Estado final (verificado/pendiente)
        """
        from datetime import datetime

        report_dir = project_path / "reports"
        report_dir.mkdir(exist_ok=True)

        now = datetime.now()
        report_id = f"ARC-AUD-{now.strftime('%Y%m%d-%H%M%S')}"

        if fix_result and fix_result.fixes_applied:
            report_path = report_dir / f"{report_id}-correcciones.md"
            content = self._generate_fix_report(report_id, now, result, fix_result, project_path)
        else:
            report_path = report_dir / f"{report_id}-hallazgos.md"
            content = self._generate_findings_report(report_id, now, result, project_path)

        report_path.write_text(content, encoding="utf-8")
        return report_path

    def _generate_findings_report(self, report_id: str, now, result: AnalysisResult, project_path: Path) -> str:
        """Genera reporte SOLO de hallazgos (modo auditoría sin fix)."""
        severity_icon = {"critical": "🔴", "high": "🟠", "medium": "🟡", "low": "🟢"}
        solid_score = result.scores.get("solid", 0)
        owasp_score = result.scores.get("owasp", 0)

        lines = [
            f"# 📋 Reporte de Auditoría — Hallazgos",
            f"## {report_id}",
            "",
            "| Campo | Valor |",
            "|-------|-------|",
            f"| **ID** | {report_id} |",
            f"| **Fecha** | {now.strftime('%Y-%m-%d %H:%M:%S')} |",
            f"| **Proyecto** | `{project_path}` |",
            f"| **Modo** | Solo auditoría (sin corrección) |",
            f"| **Auditor** | Arcana v3.0 |",
            f"| **Veredicto** | **{result.overall_status}** |",
            "",
            "---",
            "",
            "## Resumen Ejecutivo",
            "",
            "| Métrica | Score | Estado |",
            "|---------|-------|--------|",
            f"| SOLID | {solid_score:.1f}/100 | {'✅ Cumple' if solid_score >= 80 else '❌ No cumple'} |",
            f"| OWASP | {owasp_score:.1f}/100 | {'✅ Cumple' if owasp_score >= 80 else '❌ No cumple'} |",
            f"| Hallazgos totales | {len(result.findings)} | {severity_icon.get('critical', '')} {result.critical_count} críticos |",
            "",
            "---",
            "",
            "## Hallazgos Detallados",
            "",
        ]

        if not result.findings:
            lines.append("> ✅ **No se encontraron hallazgos.** El proyecto cumple todos los estándares.")
        else:
            # Agrupar por archivo
            findings_by_file = {}
            for f in result.findings:
                file_key = f.file_path if f.file_path != str(project_path) else "General"
                if file_key not in findings_by_file:
                    findings_by_file[file_key] = []
                findings_by_file[file_key].append(f)

            for file_path, findings in findings_by_file.items():
                lines.append(f"### 📁 `{Path(file_path).name if file_path != 'General' else 'Análisis General'}`")
                lines.append(f"*Ruta: `{file_path}`*")
                lines.append("")

                for f in findings:
                    icon = severity_icon.get(f.severity, "⚪")
                    lines.append(f"#### {icon} {f.id} — {f.severity.upper()}")
                    lines.append("")
                    lines.append(f"| Campo | Detalle |")
                    lines.append(f"|-------|---------|")
                    lines.append(f"| **Categoría** | {f.category} |")
                    lines.append(f"| **Severidad** | {f.severity.upper()} |")
                    lines.append(f"| **Archivo** | `{Path(f.file_path).name}` |")
                    lines.append(f"| **Línea** | {f.line_number if f.line_number > 0 else 'N/A'} |")
                    lines.append(f"| **Descripción** | {f.description[:200]} |")

                    if f.evidence and f.evidence != f.description:
                        lines.append(f"| **Evidencia** | `{f.evidence[:100]}` |")

                    lines.append(f"| **Remediación** | {f.remediation} |")

                    if f.iso27001_control:
                        lines.append(f"| **ISO 27001** | {f.iso27001_control} |")
                    if f.cobit_objective:
                        lines.append(f"| **COBIT** | {f.cobit_objective} |")

                    lines.append("")

        lines.extend([
            "---",
            "",
            "## Recomendaciones Priorizadas",
            "",
            "| Prioridad | Acción | Plazo sugerido |",
            "|-----------|--------|---------------|",
        ])

        critical_count = result.critical_count
        high_count = sum(1 for f in result.findings if f.severity == "high")
        medium_count = sum(1 for f in result.findings if f.severity == "medium")

        if critical_count > 0:
            lines.append(f"| 🔴 INMEDIATA | Corregir {critical_count} hallazgo(s) crítico(s) | 24 horas |")
        if high_count > 0:
            lines.append(f"| 🟠 ALTA | Corregir {high_count} hallazgo(s) alto(s) | 72 horas |")
        if medium_count > 0:
            lines.append(f"| 🟡 MEDIA | Corregir {medium_count} hallazgo(s) medio(s) | 2 semanas |")
        if not result.findings:
            lines.append("| ✅ N/A | Mantener prácticas actuales | Continuo |")

        lines.extend([
            "",
            "---",
            "",
            f"*Generado por Arcana v3.0 — {now.strftime('%Y-%m-%d %H:%M:%S')}*",
            f"*Ejecutar con --fix para aplicar correcciones automáticas.*",
        ])

        return "\n".join(lines)

    def _generate_fix_report(self, report_id: str, now, result: AnalysisResult, fix_result: "FixResult", project_path: Path) -> str:
        """Genera reporte de CORRECCIONES (modo fix)."""
        severity_icon = {"critical": "🔴", "high": "🟠", "medium": "🟡", "low": "🟢"}
        solid_score = result.scores.get("solid", 0)
        owasp_score = result.scores.get("owasp", 0)

        lines = [
            f"# 🔧 Reporte de Correcciones",
            f"## {report_id}",
            "",
            "| Campo | Valor |",
            "|-------|-------|",
            f"| **ID** | {report_id} |",
            f"| **Fecha** | {now.strftime('%Y-%m-%d %H:%M:%S')} |",
            f"| **Proyecto** | `{project_path}` |",
            f"| **Modo** | Auditoría + Corrección automática |",
            f"| **Auditor** | Arcana v3.0 |",
            f"| **Correcciones aplicadas** | {len(fix_result.fixes_applied)} |",
            f"| **Archivos modificados** | {len(fix_result.files_modified)} |",
            "",
            "---",
            "",
            "## Resumen de Mejora",
            "",
            "| Métrica | Antes | Estado |",
            "|---------|-------|--------|",
            f"| SOLID | {solid_score:.1f}/100 | {'✅' if solid_score >= 80 else '⚠️ Pendiente'} |",
            f"| OWASP | {owasp_score:.1f}/100 | {'✅' if owasp_score >= 80 else '⚠️ Pendiente'} |",
            f"| Hallazgos originales | {len(result.findings)} | |",
            f"| Correcciones aplicadas | {len(fix_result.fixes_applied)} | |",
            f"| Pendientes de corrección manual | {len(fix_result.fixes_skipped)} | |",
            "",
            "---",
            "",
            "## Correcciones Detalladas",
            "",
        ]

        if fix_result.fixes_applied:
            # Agrupar por archivo
            fixes_by_file = {}
            for fa in fix_result.fixes_applied:
                fname = Path(fa.file_path).name
                if fname not in fixes_by_file:
                    fixes_by_file[fname] = []
                fixes_by_file[fname].append(fa)

            for file_name, fixes in fixes_by_file.items():
                lines.append(f"### 📁 `{file_name}`")
                lines.append("")

                for i, fa in enumerate(fixes, 1):
                    sev_icon = severity_icon.get(fa.severity, "⚪")
                    lines.append(f"#### {sev_icon} Corrección {i} — [{fa.category}] {fa.severity.upper()}")
                    lines.append("")
                    lines.append(f"**Hallazgo:** {fa.description}")
                    lines.append(f"**Línea:** {fa.line_number}")
                    lines.append("")
                    lines.append("**Código original (vulnerable):**")
                    lines.append(f"```python")
                    lines.append(f"{fa.original_code}")
                    lines.append(f"```")
                    lines.append("")
                    lines.append("**Código corregido:**")
                    lines.append(f"```python")
                    lines.append(f"{fa.fixed_code}")
                    lines.append(f"```")
                    lines.append("")
        else:
            lines.append("> ✅ No se requirieron correcciones. El código ya cumple los estándares.")
            lines.append("")

        # Pendientes (fixes que requieren intervención manual)
        if fix_result.fixes_skipped:
            lines.extend([
                "---",
                "",
                "## ⚠️ Pendientes de Corrección Manual",
                "",
                "Estas situaciones requieren refactoring que no se puede automatizar de forma segura:",
                "",
            ])
            for skip in fix_result.fixes_skipped:
                lines.append(f"- {skip}")
            lines.append("")

        lines.extend([
            "---",
            "",
            "## Evidencia",
            "",
            "| Evidencia | Ubicación |",
            "|-----------|-----------|",
            f"| Backup de archivos originales | `{project_path}/.arcana_backup/` |",
            f"| Código corregido | Archivos del proyecto |",
            f"| Este reporte | `{project_path}/reports/{report_id}-correcciones.md` |",
            "",
            "---",
            "",
            f"*Generado por Arcana v3.0 — {now.strftime('%Y-%m-%d %H:%M:%S')}*",
        ])

        return "\n".join(lines)

    def _extract_owasp_cat(self, text: str) -> str:
        for cat in ["A01", "A02", "A03", "A04", "A05", "A06", "A07", "A08", "A09", "A10"]:
            if cat in text:
                return f"OWASP-{cat}"
        return "OWASP"

    def _map_iso27001(self, text: str) -> str:
        if "A03" in text or "SQL" in text:
            return "A.8.28 — Codificación segura"
        elif "A02" in text or "secret" in text.lower():
            return "A.8.4 — Acceso al código fuente"
        elif "A05" in text or "debug" in text.lower():
            return "A.8.9 — Gestión de configuración"
        elif "A10" in text:
            return "A.8.26 — Requisitos de seguridad"
        return "A.8.25 — Ciclo de vida seguro"

    def _map_cobit(self, text: str) -> str:
        if any(x in text for x in ["A03", "A02", "A05", "A10"]):
            return "DSS05 — Gestionar servicios de seguridad"
        return "BAI03 — Gestionar soluciones"
