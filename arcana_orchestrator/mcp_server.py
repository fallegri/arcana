"""
Arcana Orchestrator — MCP Server.

Tools:
- orchestrator_start: Recibe requerimientos, genera plan
- orchestrator_step: Retorna instrucción del paso actual
- orchestrator_verify: Verifica implementación del paso
- orchestrator_status: Muestra progreso general
"""

import sys
import os
from pathlib import Path

# CRÍTICO: Redirigir stderr para que no contamine stdout (MCP usa stdout)
# No redirigimos stdout porque MCP lo necesita limpio
os.environ["PYTHONDONTWRITEBYTECODE"] = "1"

# Agregar el directorio padre al path para imports
sys.path.insert(0, str(Path(__file__).parent.parent))

import asyncio
import json
from typing import Optional

from arcana_orchestrator.planner import Planner, DevelopmentPlan
from arcana_orchestrator.verifier import Verifier

try:
    from mcp.server import Server
    from mcp.server.stdio import stdio_server
    from mcp.types import Tool, TextContent
    HAS_MCP = True
except ImportError:
    HAS_MCP = False

# Estado global del plan activo
_active_plan: Optional[DevelopmentPlan] = None
_planner = Planner()
_verifier = Verifier()


async def do_start(project_name: str, requirements: str, output_path: str) -> dict:
    """Inicia un nuevo plan de desarrollo."""
    global _active_plan
    plan = _planner.create_plan(project_name, requirements, Path(output_path))
    _active_plan = plan

    first_instruction = _planner.get_step_instruction(plan)

    return {
        "plan_id": plan.id,
        "project_name": plan.project_name,
        "total_steps": plan.total_steps,
        "entities_detected": [e["name"] for e in plan.entities],
        "business_rules": plan.business_rules,
        "requirements_parsed": len(plan.requirements),
        "message": f"Plan generado: {plan.total_steps} pasos para completar el sistema.",
        "first_step": first_instruction,
    }


async def do_step() -> dict:
    """Retorna la instrucción del paso actual."""
    global _active_plan
    if _active_plan is None:
        return {"error": "No hay plan activo. Llama a orchestrator_start primero."}

    instruction = _planner.get_step_instruction(_active_plan)
    if instruction is None:
        return {
            "message": "🎉 ¡PLAN COMPLETADO! Todos los pasos fueron implementados.",
            "progress": "100%",
            "status": "DONE",
        }

    return {
        "step": _active_plan.current_step + 1,
        "total": _active_plan.total_steps,
        "progress": f"{_active_plan.progress_percentage:.0f}%",
        "instruction": instruction,
    }


async def do_verify(project_path: str) -> dict:
    """Verifica que el paso actual fue implementado correctamente."""
    global _active_plan
    if _active_plan is None:
        return {"error": "No hay plan activo."}

    step = _active_plan.current_step_obj
    if step is None:
        return {"message": "Plan completado. No hay más pasos."}

    result = _verifier.verify_step(step, Path(project_path))

    if result["passed"]:
        _active_plan.advance()

        # Si completamos el último paso → generar documentación técnica
        if _active_plan.current_step >= len(_active_plan.steps):
            from arcana_orchestrator.doc_generator import TechnicalDocGenerator
            doc_gen = TechnicalDocGenerator()
            doc_path = doc_gen.generate(Path(project_path), _active_plan.project_name)
            result["documentation"] = str(doc_path)
            result["message"] = (
                "🎉 ¡PLAN COMPLETADO! Sistema listo para deploy. "
                f"Documentación técnica generada: {doc_path}"
            )
            result["progress"] = "100%"
            result["status"] = "COMPLETED"
        else:
            next_instruction = _planner.get_step_instruction(_active_plan)
            result["next_step"] = next_instruction
            result["progress"] = f"{_active_plan.progress_percentage:.0f}%"
    else:
        result["progress"] = f"{_active_plan.progress_percentage:.0f}%"
        result["message"] += " Corrige y vuelve a llamar orchestrator_verify."

    return result


async def do_status() -> dict:
    """Retorna el estado general del plan."""
    global _active_plan
    if _active_plan is None:
        return {"status": "idle", "message": "No hay plan activo."}

    return _active_plan.to_dict()


# ═══════════════════════════════════════════════════════════════
# MCP SERVER
# ═══════════════════════════════════════════════════════════════

if HAS_MCP:
    app = Server("arcana-orchestrator")

    @app.list_tools()
    async def list_tools() -> list[Tool]:
        return [
            Tool(
                name="orchestrator_start",
                description=(
                    "Inicia un plan de desarrollo completo. Recibe los requerimientos "
                    "del sistema y genera un plan paso a paso que la IA debe ejecutar. "
                    "Arcana genera BDD, TDD y guía la implementación con SOLID + OWASP "
                    "hasta tener un sistema COMPLETO listo para deploy."
                ),
                inputSchema={
                    "type": "object",
                    "properties": {
                        "project_name": {"type": "string", "description": "Nombre del proyecto"},
                        "requirements": {"type": "string", "description": "Requerimientos completos en texto libre (historias, reglas, contexto)"},
                        "output_path": {"type": "string", "description": "Directorio donde se creará el proyecto"},
                    },
                    "required": ["project_name", "requirements", "output_path"],
                },
            ),
            Tool(
                name="orchestrator_step",
                description=(
                    "Retorna las instrucciones DETALLADAS del paso actual del plan. "
                    "Incluye: qué archivos crear, qué código implementar, qué estándares "
                    "cumplir, y qué criterios verificará Arcana."
                ),
                inputSchema={"type": "object", "properties": {}},
            ),
            Tool(
                name="orchestrator_verify",
                description=(
                    "Verifica que el paso actual fue implementado correctamente. "
                    "Chequea: archivos existen, sintaxis correcta, tests pasan. "
                    "Si PASA: avanza al siguiente paso. Si FALLA: retorna correcciones."
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
                name="orchestrator_status",
                description="Muestra el progreso general del plan de desarrollo.",
                inputSchema={"type": "object", "properties": {}},
            ),
        ]

    @app.call_tool()
    async def call_tool(name: str, arguments: dict) -> list[TextContent]:
        if name == "orchestrator_start":
            result = await do_start(
                arguments["project_name"],
                arguments["requirements"],
                arguments["output_path"],
            )
        elif name == "orchestrator_step":
            result = await do_step()
        elif name == "orchestrator_verify":
            result = await do_verify(arguments["project_path"])
        elif name == "orchestrator_status":
            result = await do_status()
        else:
            result = {"error": f"Unknown tool: {name}"}

        return [TextContent(type="text", text=json.dumps(result, indent=2, default=str))]

    async def main():
        async with stdio_server() as (read_stream, write_stream):
            await app.run(read_stream, write_stream, app.create_initialization_options())

else:
    async def main():
        # Sin MCP: modo silencioso (no print a stdout)
        import sys
        sys.stderr.write("⚠️ MCP library not installed. pip install mcp\n")
        sys.stderr.write("   Running in demo mode (output to stderr)...\n\n")
        result = await do_start(
            "demo-inventario",
            "Como almacenero quiero registrar productos con SKU y stock",
            "./output/demo"
        )
        import json
        sys.stderr.write(json.dumps(result, indent=2, ensure_ascii=False))
        sys.stderr.write("\n")


if __name__ == "__main__":
    asyncio.run(main())
