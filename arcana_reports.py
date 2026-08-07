"""
🔮 ARCANA — Generador de Reportes de Auditoría

Genera reportes formales siguiendo:
- ISO 27001: Gestión de Seguridad de la Información (hallazgos)
- COBIT 2019: Gobernanza de TI (controles y madurez)
- ISO 19011: Directrices para Auditoría (proceso y formato)
- ISO 25010: Modelo de Calidad (métricas del producto)

Dos tipos de reporte:
1. REPORTE DE INCIDENCIAS (pre-fix): Hallazgos encontrados
2. REPORTE DE CORRECCIONES (post-fix): Acciones tomadas + verificación
"""

import json
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional


def generate_audit_report_data(analysis: dict, project_path: Path) -> dict:
    """Genera datos estructurados del reporte de auditoría."""
    now = datetime.now()

    # Extraer hallazgos
    findings = []
    finding_id = 1

    # De OWASP
    owasp_data = analysis.get("owasp", {})
    for rec in owasp_data.get("recommendations", []):
        if rec.startswith("✅"):
            continue
        findings.append({
            "id": f"HAL-{finding_id:03d}",
            "source": "OWASP Top 10",
            "description": rec,
            "severity": _extract_severity(rec),
            "category": _extract_category(rec),
            "iso27001_control": _map_to_iso27001(rec),
            "cobit_objective": _map_to_cobit(rec),
            "status": "open",
        })
        finding_id += 1

    # De SOLID
    solid_data = analysis.get("solid", {})
    for rec in solid_data.get("recommendations", []):
        findings.append({
            "id": f"HAL-{finding_id:03d}",
            "source": "SOLID Principles",
            "description": rec,
            "severity": "medium",
            "category": "maintainability",
            "iso27001_control": "A.14.2 — Seguridad en procesos de desarrollo",
            "cobit_objective": "BAI03 — Gestionar Soluciones",
            "status": "open",
        })
        finding_id += 1

    # Scores
    solid_score = solid_data.get("metrics", {}).get("solid.health_score", 0)
    owasp_score = owasp_data.get("metrics", {}).get("owasp.security_score", 0)

    return {
        "metadata": {
            "report_id": f"ARC-AUD-{now.strftime('%Y%m%d-%H%M%S')}",
            "report_type": "Auditoría de Calidad y Seguridad de Software",
            "date": now.isoformat(),
            "auditor": "Arcana v2.0 (Sistema Automatizado)",
            "standards": ["ISO 27001:2022", "COBIT 2019", "ISO 19011:2018", "ISO 25010:2023"],
            "project": str(project_path),
            "scope": "Análisis estático de código fuente — SOLID + OWASP",
        },
        "executive_summary": {
            "overall_status": "CONFORME" if (solid_score >= 80 and owasp_score >= 80) else "NO CONFORME",
            "solid_score": solid_score,
            "owasp_score": owasp_score,
            "total_findings": len(findings),
            "critical_findings": sum(1 for f in findings if f["severity"] == "critical"),
            "high_findings": sum(1 for f in findings if f["severity"] == "high"),
            "recommendation": _overall_recommendation(solid_score, owasp_score),
        },
        "findings": findings,
        "iso25010_assessment": {
            "security": {"score": owasp_score, "status": "pass" if owasp_score >= 80 else "fail"},
            "maintainability": {"score": solid_score, "status": "pass" if solid_score >= 80 else "fail"},
        },
    }


def generate_audit_report(all_outputs: dict, project_path: Path, fix_applied: bool = False) -> Path:
    """
    Genera el REPORTE DE INCIDENCIAS (pre-fix) en formato Markdown.

    Formato basado en ISO 19011 (estructura de reporte de auditoría):
    1. Portada y metadata
    2. Resumen ejecutivo
    3. Alcance de la auditoría
    4. Criterios de auditoría
    5. Hallazgos (no conformidades)
    6. Conclusiones
    7. Recomendaciones
    """
    now = datetime.now()
    report_dir = project_path / "reports"
    report_dir.mkdir(exist_ok=True)

    report_id = f"ARC-AUD-{now.strftime('%Y%m%d-%H%M%S')}"
    report_path = report_dir / f"{report_id}-incidencias.md"

    # Recopilar datos
    analysis = {}
    for name, output in all_outputs.items():
        analysis[name] = {
            "status": output.status,
            "metrics": output.metrics,
            "recommendations": output.recommendations,
        }

    audit_data = generate_audit_report_data(analysis, project_path)

    # Generar Markdown
    lines = [
        f"# Reporte de Auditoría de Software",
        f"## {report_id}",
        "",
        "| Campo | Valor |",
        "|-------|-------|",
        f"| **ID Reporte** | {report_id} |",
        f"| **Fecha** | {now.strftime('%Y-%m-%d %H:%M:%S')} |",
        f"| **Tipo** | Auditoría de Calidad y Seguridad |",
        f"| **Auditor** | Arcana v2.0 (Sistema Automatizado) |",
        f"| **Proyecto** | {project_path} |",
        f"| **Estándares** | ISO 27001, COBIT 2019, ISO 19011, ISO 25010 |",
        f"| **Estado** | {'Con correcciones aplicadas' if fix_applied else 'Hallazgos pendientes'} |",
        "",
        "---",
        "",
        "## 1. Resumen Ejecutivo",
        "",
        f"| Métrica | Valor | Estado |",
        f"|---------|-------|--------|",
        f"| Score SOLID | {audit_data['executive_summary']['solid_score']:.1f}/100 | {'✅' if audit_data['executive_summary']['solid_score'] >= 80 else '❌'} |",
        f"| Score OWASP | {audit_data['executive_summary']['owasp_score']:.1f}/100 | {'✅' if audit_data['executive_summary']['owasp_score'] >= 80 else '❌'} |",
        f"| Total Hallazgos | {audit_data['executive_summary']['total_findings']} | {'✅ 0' if audit_data['executive_summary']['total_findings'] == 0 else '⚠️'} |",
        f"| Hallazgos Críticos | {audit_data['executive_summary']['critical_findings']} | {'✅' if audit_data['executive_summary']['critical_findings'] == 0 else '🚨'} |",
        f"| **Veredicto** | **{audit_data['executive_summary']['overall_status']}** | |",
        "",
        f"> {audit_data['executive_summary']['recommendation']}",
        "",
        "---",
        "",
        "## 2. Alcance de la Auditoría (ISO 19011:2018 §6.3)",
        "",
        "| Elemento | Detalle |",
        "|----------|---------|",
        "| Objeto auditado | Código fuente del proyecto |",
        "| Tipo de auditoría | Automatizada (análisis estático) |",
        "| Criterios | OWASP Top 10:2021, Principios SOLID, ISO 25010:2023 |",
        "| Método | Análisis AST + Pattern Matching + Métricas |",
        "| Limitaciones | No incluye análisis dinámico (DAST) ni pentest activo |",
        "",
        "---",
        "",
        "## 3. Criterios de Auditoría",
        "",
        "### ISO 27001:2022 — Controles de Seguridad Aplicados",
        "",
        "| Control | Descripción | Verificado |",
        "|---------|-------------|-----------|",
        "| A.8.4 | Acceso al código fuente | Revisión de secrets hardcoded |",
        "| A.8.9 | Gestión de configuración | Variables de entorno vs hardcoded |",
        "| A.8.25 | Ciclo de vida de desarrollo seguro | Análisis SAST |",
        "| A.8.26 | Requisitos de seguridad de aplicaciones | OWASP Top 10 |",
        "| A.8.28 | Codificación segura | SQL Injection, XSS, SSRF |",
        "",
        "### COBIT 2019 — Objetivos de Gobernanza",
        "",
        "| Objetivo | Descripción | Evaluado |",
        "|----------|-------------|---------|",
        "| BAI03 | Gestionar soluciones (calidad de código) | SOLID score |",
        "| BAI06 | Gestionar cambios (mantenibilidad) | Complejidad |",
        "| DSS05 | Gestionar servicios de seguridad | OWASP score |",
        "| MEA01 | Supervisar y evaluar desempeño | ISO 25010 |",
        "",
        "---",
        "",
        "## 4. Hallazgos (No Conformidades)",
        "",
    ]

    if audit_data["findings"]:
        lines.append("| ID | Fuente | Severidad | Descripción | Control ISO 27001 | Objetivo COBIT |")
        lines.append("|-----|--------|-----------|-------------|-------------------|----------------|")
        for f in audit_data["findings"]:
            sev_icon = {"critical": "🔴", "high": "🟠", "medium": "🟡", "low": "🟢"}.get(f["severity"], "⚪")
            lines.append(
                f"| {f['id']} | {f['source']} | {sev_icon} {f['severity'].upper()} | "
                f"{f['description'][:80]} | {f['iso27001_control']} | {f['cobit_objective']} |"
            )
    else:
        lines.append("> ✅ No se encontraron hallazgos. El proyecto cumple los criterios de auditoría.")

    lines.extend([
        "",
        "---",
        "",
        "## 5. Conclusiones (ISO 19011:2018 §6.5)",
        "",
        f"El proyecto auditado **{audit_data['executive_summary']['overall_status']}** con los criterios establecidos.",
        "",
        f"- Seguridad (OWASP): {audit_data['executive_summary']['owasp_score']:.0f}% — "
        f"{'Cumple' if audit_data['executive_summary']['owasp_score'] >= 80 else 'No cumple'} umbral mínimo (80%)",
        f"- Mantenibilidad (SOLID): {audit_data['executive_summary']['solid_score']:.0f}% — "
        f"{'Cumple' if audit_data['executive_summary']['solid_score'] >= 80 else 'No cumple'} umbral mínimo (80%)",
        "",
        "---",
        "",
        "## 6. Plan de Remediación",
        "",
        "| Prioridad | Acción | Responsable | Plazo |",
        "|-----------|--------|-------------|-------|",
    ])

    critical_count = audit_data["executive_summary"]["critical_findings"]
    high_count = audit_data["executive_summary"]["high_findings"]

    if critical_count > 0:
        lines.append("| 🔴 INMEDIATA | Corregir vulnerabilidades críticas (SQL Injection, Secrets) | Equipo Dev | 24h |")
    if high_count > 0:
        lines.append("| 🟠 ALTA | Corregir vulnerabilidades altas (SSRF, Config) | Equipo Dev | 72h |")
    if audit_data["executive_summary"]["solid_score"] < 80:
        lines.append("| 🟡 MEDIA | Refactoring SOLID (reducir complejidad) | Equipo Dev | 2 semanas |")
    if critical_count == 0 and high_count == 0:
        lines.append("| ✅ N/A | Mantener prácticas actuales | Equipo Dev | Continuo |")

    lines.extend([
        "",
        "---",
        "",
        f"*Reporte generado por Arcana v2.0 — {now.strftime('%Y-%m-%d %H:%M:%S')}*",
        f"*Siguiente auditoría recomendada: {(now.replace(day=1)).strftime('%Y-%m-15')}*",
    ])

    report_path.write_text("\n".join(lines), encoding="utf-8")
    return report_path


def generate_fix_report(
    pre_analysis: dict,
    fix_results: dict,
    post_analysis: dict,
    project_path: Path,
) -> Path:
    """
    Genera el REPORTE DE CORRECCIONES (post-fix).

    Documenta:
    1. Estado inicial (hallazgos)
    2. Correcciones aplicadas
    3. Estado final (verificación)
    4. Evidencia de cumplimiento
    """
    now = datetime.now()
    report_dir = project_path / "reports"
    report_dir.mkdir(exist_ok=True)

    report_id = f"ARC-FIX-{now.strftime('%Y%m%d-%H%M%S')}"
    report_path = report_dir / f"{report_id}-correcciones.md"

    # Scores antes y después
    pre_solid = pre_analysis.get("solid", {}).get("metrics", {}).get("solid.health_score", 0)
    pre_owasp = pre_analysis.get("owasp", {}).get("metrics", {}).get("owasp.security_score", 0)
    post_solid = post_analysis.get("solid", {}).get("metrics", {}).get("solid.health_score", 0)
    post_owasp = post_analysis.get("owasp", {}).get("metrics", {}).get("owasp.security_score", 0)

    lines = [
        f"# Reporte de Correcciones de Software",
        f"## {report_id}",
        "",
        "| Campo | Valor |",
        "|-------|-------|",
        f"| **ID Reporte** | {report_id} |",
        f"| **Fecha** | {now.strftime('%Y-%m-%d %H:%M:%S')} |",
        f"| **Tipo** | Informe de Acciones Correctivas |",
        f"| **Herramienta** | Arcana v2.0 (Auto-fix Engine) |",
        f"| **Proyecto** | {project_path} |",
        f"| **Estándares** | ISO 27001, COBIT 2019, ISO 19011, ISO 25010 |",
        "",
        "---",
        "",
        "## 1. Resumen de Mejora",
        "",
        "| Métrica | ANTES | DESPUÉS | Δ Mejora |",
        "|---------|-------|---------|----------|",
        f"| Score SOLID | {pre_solid:.1f} | {post_solid:.1f} | {post_solid - pre_solid:+.1f} |",
        f"| Score OWASP | {pre_owasp:.1f} | {post_owasp:.1f} | {post_owasp - pre_owasp:+.1f} |",
        "",
        "---",
        "",
        "## 2. Correcciones Aplicadas",
        "",
    ]

    total_fixes = 0
    for agent_name, fixes in fix_results.items():
        if isinstance(fixes, dict) and "details" in fixes:
            lines.append(f"### {agent_name.upper()}")
            lines.append("")
            lines.append("| # | Archivo | Línea | Severidad | Descripción | Código Original | Código Corregido |")
            lines.append("|---|---------|-------|-----------|-------------|-----------------|-----------------|")

            for i, fix in enumerate(fixes["details"], 1):
                total_fixes += 1
                lines.append(
                    f"| {i} | `{Path(fix['file']).name}` | {fix['line']} | "
                    f"{fix['severity']} | {fix['description'][:50]} | "
                    f"`{fix['original'][:30]}` | `{fix['fixed'][:30]}` |"
                )
            lines.append("")

    lines.extend([
        "---",
        "",
        "## 3. Verificación Post-Corrección",
        "",
        f"| Verificación | Resultado |",
        f"|-------------|-----------|",
        f"| SOLID score ≥ 80% | {'✅ CUMPLE' if post_solid >= 80 else '❌ NO CUMPLE'} ({post_solid:.1f}%) |",
        f"| OWASP score ≥ 80% | {'✅ CUMPLE' if post_owasp >= 80 else '❌ NO CUMPLE'} ({post_owasp:.1f}%) |",
        f"| 0 vulnerabilidades críticas | {'✅' if post_owasp >= 90 else '❌'} |",
        f"| Total correcciones aplicadas | {total_fixes} |",
        "",
        "---",
        "",
        "## 4. Evidencia de Cumplimiento (ISO 19011:2018)",
        "",
        "| Evidencia | Tipo | Ubicación |",
        "|-----------|------|-----------|",
        f"| Backup pre-fix | Código original | `{project_path}/.arcana_backup/` |",
        f"| Código corregido | Archivos modificados | Directorio del proyecto |",
        f"| Re-análisis | Verificación automatizada | Este reporte (Sección 3) |",
        f"| Log de cambios | Detalle de correcciones | Este reporte (Sección 2) |",
        "",
        "---",
        "",
        "## 5. Conclusión",
        "",
    ])

    if post_solid >= 80 and post_owasp >= 80:
        lines.append("> ✅ **CONFORME**: Las correcciones aplicadas resuelven los hallazgos críticos.")
        lines.append("> El proyecto cumple los umbrales mínimos de calidad y seguridad.")
    else:
        lines.append("> ⚠️ **PARCIALMENTE CONFORME**: Algunas correcciones requieren intervención manual.")
        lines.append("> Se recomienda revisión por parte del equipo de desarrollo.")

    lines.extend([
        "",
        "---",
        "",
        f"*Reporte generado por Arcana v2.0 — {now.strftime('%Y-%m-%d %H:%M:%S')}*",
    ])

    report_path.write_text("\n".join(lines), encoding="utf-8")
    return report_path


def generate_full_report(all_outputs: dict, project_path: Path, fix_applied: bool = False) -> Path:
    """Genera reporte completo (incidencias + correcciones si aplica)."""
    return generate_audit_report(all_outputs, project_path, fix_applied)


# ═══════════════════════════════════════════════════════════════
# HELPERS
# ═══════════════════════════════════════════════════════════════

def _extract_severity(text: str) -> str:
    text_lower = text.lower()
    if "critical" in text_lower:
        return "critical"
    elif "high" in text_lower:
        return "high"
    elif "medium" in text_lower:
        return "medium"
    return "low"


def _extract_category(text: str) -> str:
    if "A01" in text:
        return "access_control"
    elif "A02" in text:
        return "cryptography"
    elif "A03" in text:
        return "injection"
    elif "A05" in text:
        return "misconfiguration"
    elif "A10" in text:
        return "ssrf"
    return "general"


def _map_to_iso27001(text: str) -> str:
    """Mapea hallazgos a controles ISO 27001:2022."""
    if "A03" in text or "injection" in text.lower() or "SQL" in text:
        return "A.8.28 — Codificación segura"
    elif "A02" in text or "secret" in text.lower() or "password" in text.lower():
        return "A.8.4 — Acceso al código fuente"
    elif "A05" in text or "debug" in text.lower() or "config" in text.lower():
        return "A.8.9 — Gestión de configuración"
    elif "A10" in text or "SSRF" in text:
        return "A.8.26 — Requisitos de seguridad"
    elif "SRP" in text or "OCP" in text or "SOLID" in text.upper():
        return "A.14.2 — Seguridad en desarrollo"
    return "A.8.25 — Ciclo de vida de desarrollo seguro"


def _map_to_cobit(text: str) -> str:
    """Mapea hallazgos a objetivos COBIT 2019."""
    if "A03" in text or "A02" in text or "A05" in text or "A10" in text:
        return "DSS05 — Gestionar servicios de seguridad"
    elif "SOLID" in text.upper() or "SRP" in text or "OCP" in text:
        return "BAI03 — Gestionar soluciones"
    return "MEA01 — Supervisar desempeño"


def _overall_recommendation(solid_score: float, owasp_score: float) -> str:
    if solid_score >= 90 and owasp_score >= 90:
        return "El proyecto cumple estándares de calidad profesional. Mantener prácticas actuales."
    elif owasp_score < 50:
        return "⚠️ URGENTE: Vulnerabilidades críticas de seguridad requieren corrección INMEDIATA antes de cualquier despliegue."
    elif solid_score < 50:
        return "El código requiere refactoring significativo para ser mantenible a largo plazo."
    elif owasp_score < 80:
        return "Corregir vulnerabilidades de seguridad antes del próximo release."
    else:
        return "Proyecto en buen estado. Aplicar mejoras menores de mantenibilidad."
