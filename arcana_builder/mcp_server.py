"""
Arcana Builder — MCP Server independiente.

Tools:
- builder_create: Genera proyecto desde historias de usuario
- builder_add_feature: Agrega funcionalidad a proyecto existente
"""

import sys
sys.path.insert(0, str(__import__('pathlib').Path(__file__).parent.parent))

import asyncio
import json
from pathlib import Path

from arcana_builder.engine import BuilderEngine

try:
    from mcp.server import Server
    from mcp.server.stdio import stdio_server
    from mcp.types import Tool, TextContent
    HAS_MCP = True
except ImportError:
    HAS_MCP = False


if HAS_MCP:
    app = Server("arcana-builder")
    engine = BuilderEngine()

    @app.list_tools()
    async def list_tools() -> list[Tool]:
        return [
            Tool(
                name="builder_requirements",
                description=(
                    "FASE 1: Ingeniería de Requisitos. Analiza lo que el usuario describió, "
                    "detecta entidades, reglas de negocio, y genera preguntas para completar "
                    "la información faltante. Llamar ANTES de builder_create."
                ),
                inputSchema={
                    "type": "object",
                    "properties": {
                        "project_name": {"type": "string", "description": "Nombre del proyecto"},
                        "description": {"type": "string", "description": "Lo que el usuario describió del sistema"},
                    },
                    "required": ["project_name", "description"],
                },
            ),
            Tool(
                name="builder_refine",
                description=(
                    "FASE 1b: Refinar requisitos con las respuestas del usuario. "
                    "Llamar después de que el usuario respondió las preguntas de builder_requirements."
                ),
                inputSchema={
                    "type": "object",
                    "properties": {
                        "project_name": {"type": "string"},
                        "original_description": {"type": "string", "description": "Descripción original"},
                        "user_answers": {"type": "string", "description": "Respuestas del usuario a las preguntas"},
                    },
                    "required": ["project_name", "original_description", "user_answers"],
                },
            ),
            Tool(
                name="builder_create",
                description=(
                    "FASE 2: Genera un proyecto completo desde historias de usuario. "
                    "Aplica BDD, TDD, SOLID y OWASP automáticamente. "
                    "Llamar DESPUÉS de que builder_requirements diga ready_to_build=true."
                ),
                inputSchema={
                    "type": "object",
                    "properties": {
                        "project_name": {"type": "string"},
                        "user_stories": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Historias de usuario en formato libre",
                        },
                        "business_context": {"type": "string", "description": "Contexto del negocio"},
                        "output_path": {"type": "string", "description": "Directorio de salida"},
                    },
                    "required": ["project_name", "user_stories"],
                },
            ),
        ]

    @app.call_tool()
    async def call_tool(name: str, arguments: dict) -> list[TextContent]:
        if name == "builder_requirements":
            from arcana_builder.requirements_engineer import RequirementsEngineer
            eng = RequirementsEngineer()
            analysis = eng.analyze(arguments["description"], arguments["project_name"])
            questionnaire = eng.generate_questionnaire(analysis)
            data = {
                "completeness": analysis.completeness,
                "ready_to_build": analysis.ready_to_build,
                "entities": [e["name"] for e in analysis.proposed_entities],
                "rules_detected": analysis.detected_rules,
                "questionnaire": questionnaire,
            }
        elif name == "builder_refine":
            from arcana_builder.requirements_engineer import RequirementsEngineer
            eng = RequirementsEngineer()
            analysis = eng.analyze(arguments["original_description"], arguments["project_name"])
            analysis = eng.refine(analysis, arguments["user_answers"])
            questionnaire = eng.generate_questionnaire(analysis)
            data = {
                "completeness": analysis.completeness,
                "ready_to_build": analysis.ready_to_build,
                "entities": [{"name": e["name"], "fields": e.get("fields", [])} for e in analysis.proposed_entities],
                "rules": analysis.detected_rules,
                "questionnaire": questionnaire if not analysis.ready_to_build else "✅ Listo para construir. Llama a builder_create.",
            }
        elif name == "builder_create":
            result = await engine.build(
                project_name=arguments["project_name"],
                user_stories=arguments["user_stories"],
                business_context=arguments.get("business_context", ""),
                output_path=Path(arguments.get("output_path", f"./output/{arguments['project_name']}")),
            )
            data = result
        else:
            data = {"error": f"Unknown tool: {name}"}

        return [TextContent(type="text", text=json.dumps(data, indent=2, default=str))]

    async def main():
        async with stdio_server() as (read_stream, write_stream):
            await app.run(read_stream, write_stream, app.create_initialization_options())
else:
    async def main():
        print("MCP not installed. pip install mcp")

if __name__ == "__main__":
    asyncio.run(main())
