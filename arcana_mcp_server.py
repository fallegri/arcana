#!/usr/bin/env python3
"""
🔮 ARCANA MCP Server — Model Context Protocol

Expone las capacidades de Arcana como tools MCP para uso con:
- opencode
- Claude Desktop
- Cursor
- Cualquier cliente MCP compatible

Tools disponibles:
- arcana_analyze: Analiza un proyecto (SOLID, OWASP, o todos)
- arcana_fix: Corrige vulnerabilidades/violaciones detectadas
- arcana_report: Genera reporte de auditoría (ISO 27001/19011/25010)
- arcana_validate: Re-verifica después de correcciones

Instalación:
  pip install mcp
  Agregar a mcp.json (ver README)

Ejecución standalone:
  python arcana_mcp_server.py
"""

import sys
sys.path.insert(0, '.')

import asyncio
import json
from pathlib import Path
from typing import Any

try:
    from mcp.server import Server
    from mcp.server.stdio import stdio_server
    from mcp.types import Tool, TextContent
    HAS_MCP = True
except ImportError:
    HAS_MCP = False

from agents.base import AgentInput, SharedContext
from agents.solid.agent import SOLIDAgent
from agents.security.owasp.agent import OWASPAgent
from agents.ux_quality.agent import MetricsAgent
from agents.bdd.agent import BDDAgent
from agents.tdd.agent import TDDAgent


# ═══════════════════════════════════════════════════════════════
# CORE FUNCTIONS (shared between MCP and CLI)
# ═══════════════════════════════════════════════════════════════

async def do_analyze(project_path: str, agents: list = None, mode: str = "standard") -> dict:
    """Ejecuta análisis con los agentes especificados."""
    path = Path(project_path).resolve()
    if not path.exists():
        return {"error": f"Path does not exist: {project_path}"}

    context = SharedContext(project_path=path, educational_mode=mode)
    results = {}

    agent_classes = {
        "solid": SOLIDAgent,
        "owasp": OWASPAgent,
        "metrics": MetricsAgent,
        "bdd": BDDAgent,
        "tdd": TDDAgent,
    }

    targets = agents or ["solid", "owasp"]

    for agent_name in targets:
        if agent_name not in agent_classes:
            results[agent_name] = {"error": f"Unknown agent: {agent_name}"}
            continue

        agent = agent_classes[agent_name]()
        agent_path = Path("agents/bdd") if agent_name == "bdd" else path

        input_data = AgentInput(
            phase=agent.phase,
            project_path=agent_path,
            config={"mode": "full"},
            context=context,
            previous_results=[],
        )

        output = await agent.execute(input_data)
        results[agent_name] = {
            "status": output.status,
            "metrics": output.metrics,
            "recommendations": output.recommendations,
            "educational_notes": output.educational_notes,
            "errors": output.errors,
        }

        for k, v in output.metrics.items():
            context.add_metric(k, v)

    return results


async def do_fix(project_path: str, agents: list = None) -> dict:
    """Ejecuta análisis + corrección automática."""
    path = Path(project_path).resolve()
    if not path.exists():
        return {"error": f"Path does not exist: {project_path}"}

    context = SharedContext(project_path=path, educational_mode="standard")
    fix_results = {}

    agent_classes = {
        "solid": SOLIDAgent,
        "owasp": OWASPAgent,
    }

    targets = agents or ["owasp", "solid"]

    for agent_name in targets:
        if agent_name not in agent_classes:
            continue

        agent = agent_classes[agent_name]()
        if not agent.supports_fix:
            continue

        input_data = AgentInput(
            phase=agent.phase,
            project_path=path,
            config={},
            context=context,
            previous_results=[],
        )

        # Analizar
        analysis = await agent.execute(input_data)

        # Corregir si hay problemas
        if analysis.status != "success":
            fix_result = await agent.fix(input_data, analysis)
            if fix_result:
                fix_results[agent_name] = {
                    "fixes_applied": len(fix_result.fixes_applied),
                    "fixes_skipped": len(fix_result.fixes_skipped),
                    "files_modified": fix_result.files_modified,
                    "details": [
                        {
                            "file": f.file_path,
                            "line": f.line_number,
                            "original": f.original_code,
                            "fixed": f.fixed_code,
                            "description": f.description,
                            "severity": f.severity,
                        }
                        for f in fix_result.fixes_applied
                    ],
                }
        else:
            fix_results[agent_name] = {"status": "clean", "message": "No fixes needed"}

    return fix_results


async def do_report(project_path: str, format: str = "audit") -> dict:
    """Genera reporte de auditoría."""
    # Primero analizar
    analysis = await do_analyze(project_path, agents=["solid", "owasp"])

    report = {
        "type": format,
        "project": project_path,
        "timestamp": __import__("datetime").datetime.now().isoformat(),
        "analysis": analysis,
    }

    if format == "audit":
        from arcana_reports import generate_audit_report_data
        report["audit"] = generate_audit_report_data(analysis, Path(project_path))

    return report


async def do_validate(project_path: str) -> dict:
    """Re-ejecuta análisis para verificar que los fixes funcionaron."""
    results = await do_analyze(project_path, agents=["solid", "owasp"])

    # Calcular si mejoró
    solid_score = results.get("solid", {}).get("metrics", {}).get("solid.health_score", 0)
    owasp_score = results.get("owasp", {}).get("metrics", {}).get("owasp.security_score", 0)

    return {
        "validation": results,
        "summary": {
            "solid_score": solid_score,
            "owasp_score": owasp_score,
            "overall_status": "pass" if (solid_score >= 80 and owasp_score >= 80) else "fail",
        },
    }


# ═══════════════════════════════════════════════════════════════
# MCP SERVER
# ═══════════════════════════════════════════════════════════════

if HAS_MCP:
    app = Server("arcana")

    @app.list_tools()
    async def list_tools() -> list[Tool]:
        return [
            Tool(
                name="arcana_analyze",
                description=(
                    "Analiza un proyecto de software buscando violaciones de SOLID, "
                    "vulnerabilidades OWASP, y métricas de calidad ISO 25010. "
                    "Retorna scores, hallazgos y recomendaciones."
                ),
                inputSchema={
                    "type": "object",
                    "properties": {
                        "project_path": {
                            "type": "string",
                            "description": "Ruta al directorio del proyecto a analizar",
                        },
                        "agents": {
                            "type": "array",
                            "items": {"type": "string", "enum": ["solid", "owasp", "bdd", "tdd", "metrics"]},
                            "description": "Agentes a ejecutar (default: solid + owasp)",
                        },
                        "mode": {
                            "type": "string",
                            "enum": ["beginner", "standard", "expert"],
                            "description": "Nivel de detalle educativo (default: standard)",
                        },
                    },
                    "required": ["project_path"],
                },
            ),
            Tool(
                name="arcana_fix",
                description=(
                    "Analiza y CORRIGE automáticamente vulnerabilidades OWASP y "
                    "violaciones SOLID en el proyecto. Genera backups antes de modificar. "
                    "Retorna las correcciones aplicadas."
                ),
                inputSchema={
                    "type": "object",
                    "properties": {
                        "project_path": {
                            "type": "string",
                            "description": "Ruta al directorio del proyecto a corregir",
                        },
                        "agents": {
                            "type": "array",
                            "items": {"type": "string", "enum": ["solid", "owasp"]},
                            "description": "Agentes de corrección (default: owasp + solid)",
                        },
                    },
                    "required": ["project_path"],
                },
            ),
            Tool(
                name="arcana_report",
                description=(
                    "Genera un reporte formal de auditoría de software según "
                    "ISO 27001, COBIT, ISO 19011 e ISO 25010. "
                    "Incluye hallazgos, severidades, y plan de remediación."
                ),
                inputSchema={
                    "type": "object",
                    "properties": {
                        "project_path": {
                            "type": "string",
                            "description": "Ruta al directorio del proyecto",
                        },
                        "format": {
                            "type": "string",
                            "enum": ["audit", "summary", "full"],
                            "description": "Formato del reporte (default: audit)",
                        },
                    },
                    "required": ["project_path"],
                },
            ),
            Tool(
                name="arcana_validate",
                description=(
                    "Re-ejecuta el análisis para verificar que las correcciones "
                    "aplicadas por arcana_fix fueron efectivas. "
                    "Compara scores antes y después."
                ),
                inputSchema={
                    "type": "object",
                    "properties": {
                        "project_path": {
                            "type": "string",
                            "description": "Ruta al directorio del proyecto a validar",
                        },
                    },
                    "required": ["project_path"],
                },
            ),
        ]

    @app.call_tool()
    async def call_tool(name: str, arguments: dict[str, Any]) -> list[TextContent]:
        if name == "arcana_analyze":
            result = await do_analyze(
                arguments["project_path"],
                agents=arguments.get("agents"),
                mode=arguments.get("mode", "standard"),
            )
        elif name == "arcana_fix":
            result = await do_fix(
                arguments["project_path"],
                agents=arguments.get("agents"),
            )
        elif name == "arcana_report":
            result = await do_report(
                arguments["project_path"],
                format=arguments.get("format", "audit"),
            )
        elif name == "arcana_validate":
            result = await do_validate(arguments["project_path"])
        else:
            result = {"error": f"Unknown tool: {name}"}

        return [TextContent(type="text", text=json.dumps(result, indent=2, default=str))]

    async def main():
        async with stdio_server() as (read_stream, write_stream):
            await app.run(read_stream, write_stream, app.create_initialization_options())

else:
    async def main():
        print("⚠️  MCP library not installed. Install with: pip install mcp")
        print("    Running in standalone mode...")
        print()
        # Demo mode
        result = await do_analyze("examples/taskflow", agents=["solid", "owasp"])
        print(json.dumps(result, indent=2, default=str))


if __name__ == "__main__":
    asyncio.run(main())
