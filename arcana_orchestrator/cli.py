#!/usr/bin/env python3
"""
Arcana Orchestrator — CLI.

Uso:
  python -m arcana_orchestrator --name "mi-sistema" --requirements reqs.md
"""

import sys
sys.path.insert(0, str(__import__('pathlib').Path(__file__).parent.parent))

import argparse
import asyncio
import json
from pathlib import Path
from arcana_orchestrator.planner import Planner

P = '\033[35m'; C = '\033[36m'; G = '\033[32m'
Y = '\033[33m'; B = '\033[1m'; D = '\033[2m'; X = '\033[0m'


async def main():
    parser = argparse.ArgumentParser(
        prog='arcana-orchestrator',
        description='🔮 Arcana Orchestrator — Director de desarrollo completo',
    )
    parser.add_argument('--name', '-n', required=True)
    parser.add_argument('--requirements', '-r', required=True,
                        help='Archivo con requerimientos o texto directo')
    parser.add_argument('--output', '-o', default='./output')
    args = parser.parse_args()

    # Cargar requerimientos
    req_path = Path(args.requirements)
    if req_path.exists():
        requirements = req_path.read_text(encoding="utf-8")
    else:
        requirements = args.requirements

    print(f"{P}{B}")
    print("╭──────────────────────────────────────────────────────────────╮")
    print("│  🔮 ARCANA ORCHESTRATOR — Director de Desarrollo              │")
    print("╰──────────────────────────────────────────────────────────────╯")
    print(f"{X}")

    planner = Planner()
    plan = planner.create_plan(args.name, requirements, Path(args.output) / args.name)

    print(f"  {D}Proyecto:{X} {B}{args.name}{X}")
    print(f"  {D}Requerimientos:{X} {len(plan.requirements)}")
    print(f"  {D}Entidades:{X} {[e['name'] for e in plan.entities]}")
    print(f"  {D}Reglas de negocio:{X} {len(plan.business_rules)}")
    print(f"  {D}Total pasos:{X} {B}{plan.total_steps}{X}")
    print()
    print(f"  {B}Plan de Desarrollo:{X}")
    print()
    for step in plan.steps:
        print(f"    {C}{step.number:2d}.{X} [{step.phase:<12}] {step.title}")
        for std in step.standards[:2]:
            print(f"        {D}↳ {std}{X}")
    print()
    print(f"  {G}Para ejecutar con MCP (opencode/cursor):{X}")
    print(f"    1. Configura arcana-orchestrator en mcp.json")
    print(f"    2. Llama: orchestrator_start con estos requerimientos")
    print(f"    3. Sigue las instrucciones paso a paso")
    print()

    # Guardar plan como JSON
    plan_path = Path(args.output) / args.name / "arcana_plan.json"
    plan_path.parent.mkdir(parents=True, exist_ok=True)
    plan_path.write_text(json.dumps(plan.to_dict(), indent=2, ensure_ascii=False))
    print(f"  {G}📄 Plan guardado:{X} {plan_path}")
    print()
    print(f"{P}  \"Dame los requerimientos. Yo dirijo hasta que el sistema esté COMPLETO.\"{X}")
    print()


if __name__ == '__main__':
    asyncio.run(main())
