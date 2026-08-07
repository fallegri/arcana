"""
Arcana Auditor — MCP Server independiente.

Tools:
- auditor_analyze: Analiza código (criterios NO negociables)
- auditor_fix: Corrige + verifica (acción correctiva)
- auditor_report: Genera reporte formal de auditoría
"""

import sys
sys.path.insert(0, str(__import__('pathlib').Path(__file__).parent.parent))

import asyncio
import json
from pathlib import Path

from arcana_auditor.engine import AuditorEngine

try:
    from mcp.server import Server
    from mcp.server.stdio import stdio_server
    from mcp.types import Tool, TextContent
    HAS_MCP = True
except ImportError:
    HAS_MCP = False


if HAS_MCP:
    app = Server("arcana-auditor")
    engine = AuditorEngine()

    @app.list_tools()
    async def list_tools() -> list[Tool]:
        return [
            Tool(
                name="auditor_analyze",
                description=(
                    "Analiza un proyecto contra estándares SOLID y OWASP. "
                    "Criterios NO negociables. Retorna veredicto CONFORME/NO CONFORME."
                ),
                inputSchema={
                    "type": "object",
                    "properties": {
                        "project_path": {"type": "string", "description": "Ruta al proyecto"},
                    },
                    "required": ["project_path"],
                },
            ),
            Tool(
                name="auditor_fix",
                description=(
                    "Analiza y CORRIGE automáticamente. Genera backup. "
                    "Retorna correcciones aplicadas + verificación post-fix."
                ),
                inputSchema={
                    "type": "object",
                    "properties": {
                        "project_path": {"type": "string", "description": "Ruta al proyecto"},
                    },
                    "required": ["project_path"],
                },
            ),
            Tool(
                name="auditor_report",
                description=(
                    "Genera reporte formal de auditoría: ISO 27001, COBIT, ISO 19011, ISO 25010."
                ),
                inputSchema={
                    "type": "object",
                    "properties": {
                        "project_path": {"type": "string", "description": "Ruta al proyecto"},
                        "format": {"type": "string", "enum": ["summary", "audit", "full"]},
                    },
                    "required": ["project_path"],
                },
            ),
        ]

    @app.call_tool()
    async def call_tool(name: str, arguments: dict) -> list[TextContent]:
        path = arguments["project_path"]

        if name == "auditor_analyze":
            result = await engine.analyze(Path(path))
            data = {"status": result.overall_status, "scores": result.scores,
                    "findings": len(result.findings), "critical": result.critical_count}

        elif name == "auditor_fix":
            analysis = await engine.analyze(Path(path))
            fix_result = await engine.fix(Path(path), analysis)
            data = {"fixes_applied": len(fix_result.fixes_applied),
                    "files_modified": fix_result.files_modified}

        elif name == "auditor_report":
            analysis = await engine.analyze(Path(path))
            report_path = engine.generate_report(Path(path), analysis, arguments.get("format", "audit"))
            data = {"report_path": str(report_path)}

        else:
            data = {"error": f"Unknown tool: {name}"}

        return [TextContent(type="text", text=json.dumps(data, indent=2, default=str))]

    async def main():
        async with stdio_server() as (read_stream, write_stream):
            await app.run(read_stream, write_stream, app.create_initialization_options())

else:
    async def main():
        print("⚠️ MCP library not installed. pip install mcp")

if __name__ == "__main__":
    asyncio.run(main())
