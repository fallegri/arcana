"""
Arcana Tutor — MCP Server independiente.

Tools:
- tutor_challenge: Genera un reto
- tutor_evaluate: Evalúa solución del alumno
- tutor_hint: Da pista progresiva
- tutor_solution: Muestra solución completa
"""

import sys
sys.path.insert(0, str(__import__('pathlib').Path(__file__).parent.parent))

import asyncio
import json

from arcana_tutor.engine import TutorEngine

try:
    from mcp.server import Server
    from mcp.server.stdio import stdio_server
    from mcp.types import Tool, TextContent
    HAS_MCP = True
except ImportError:
    HAS_MCP = False

if HAS_MCP:
    app = Server("arcana-tutor")
    engine = TutorEngine()

    @app.list_tools()
    async def list_tools() -> list[Tool]:
        return [
            Tool(
                name="tutor_challenge",
                description="Genera un reto de código según tema y nivel.",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "topic": {"type": "string", "enum": ["owasp", "solid", "tdd", "bdd"]},
                        "level": {"type": "string", "enum": ["beginner", "intermediate", "advanced"]},
                        "subtopic": {"type": "string"},
                    },
                    "required": ["topic"],
                },
            ),
            Tool(
                name="tutor_evaluate",
                description="Evalúa la solución del alumno. Score 0-10 + feedback.",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "challenge_id": {"type": "string"},
                        "student_code": {"type": "string"},
                    },
                    "required": ["challenge_id", "student_code"],
                },
            ),
            Tool(
                name="tutor_hint",
                description="Da pista progresiva sin resolver.",
                inputSchema={
                    "type": "object",
                    "properties": {"challenge_id": {"type": "string"}},
                    "required": ["challenge_id"],
                },
            ),
            Tool(
                name="tutor_solution",
                description="Muestra la solución completa explicada.",
                inputSchema={
                    "type": "object",
                    "properties": {"challenge_id": {"type": "string"}},
                    "required": ["challenge_id"],
                },
            ),
        ]

    @app.call_tool()
    async def call_tool(name: str, arguments: dict) -> list[TextContent]:
        if name == "tutor_challenge":
            data = engine.generate_challenge(
                topic=arguments["topic"],
                level=arguments.get("level", "beginner"),
                subtopic=arguments.get("subtopic"),
            )
        elif name == "tutor_evaluate":
            data = await engine.evaluate(arguments["challenge_id"], arguments["student_code"])
        elif name == "tutor_hint":
            data = {"hint": engine.get_hint(arguments["challenge_id"])}
        elif name == "tutor_solution":
            data = {"solution": engine.get_solution(arguments["challenge_id"])}
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
