#!/usr/bin/env python3
"""
Arcana Builder — CLI independiente.

Uso:
  python -m arcana_builder --name "mi-app" --describe "Sistema de pedidos para cafetería"
  python -m arcana_builder --name "mi-app" --stories historias.txt
  python -m arcana_builder --name "mi-app" --stories historias.txt --output ./output/
"""

import sys
sys.path.insert(0, str(__import__('pathlib').Path(__file__).parent.parent))

import argparse
import asyncio
from pathlib import Path

from arcana_builder.engine import BuilderEngine

P = '\033[35m'; C = '\033[36m'; G = '\033[32m'
Y = '\033[33m'; R = '\033[31m'; B = '\033[1m'
D = '\033[2m'; X = '\033[0m'


def parse_args():
    parser = argparse.ArgumentParser(
        prog='arcana-builder',
        description='🔮 Arcana Builder — Genera software con estándares profesionales',
    )
    parser.add_argument('--name', '-n', required=True,
                        help='Nombre del proyecto a generar')
    parser.add_argument('--describe', '-d',
                        help='Descripción del sistema en lenguaje natural')
    parser.add_argument('--stories', '-s',
                        help='Archivo con historias de usuario (una por línea)')
    parser.add_argument('--context', '-c', default='',
                        help='Contexto de negocio adicional')
    parser.add_argument('--output', '-o', default='./output',
                        help='Directorio de salida (default: ./output)')
    return parser.parse_args()


async def main():
    args = parse_args()

    if not args.describe and not args.stories:
        print(f"{R}❌ Error: Necesito --describe o --stories (o ambos){X}")
        print(f"   Ejemplo: python -m arcana_builder --name mi-app --describe 'Sistema de pedidos'")
        sys.exit(1)

    # Cargar historias de usuario
    stories = []
    if args.stories:
        stories_path = Path(args.stories)
        if stories_path.exists():
            stories = [l.strip() for l in stories_path.read_text().split("\n") if l.strip()]
        else:
            print(f"{R}❌ Archivo no encontrado: {args.stories}{X}")
            sys.exit(1)

    if args.describe:
        stories.insert(0, args.describe)

    print(f"{P}{B}")
    print("╭──────────────────────────────────────────────────────────────╮")
    print("│  🔮 ARCANA BUILDER — Generador de Software Profesional        │")
    print("╰──────────────────────────────────────────────────────────────╯")
    print(f"{X}")
    print(f"  {D}Proyecto:{X} {B}{args.name}{X}")
    print(f"  {D}Historias:{X} {len(stories)}")
    print(f"  {D}Output:{X} {args.output}")
    print()

    engine = BuilderEngine()
    output_path = Path(args.output) / args.name

    # Ejecutar pipeline de generación
    result = await engine.build(
        project_name=args.name,
        user_stories=stories,
        business_context=args.context,
        output_path=output_path,
    )

    # Mostrar resultado
    print(f"\n{G}{B}  ✅ Proyecto generado exitosamente{X}\n")
    print(f"  {D}Ubicación:{X} {B}{output_path}{X}")
    print(f"  {D}Archivos generados:{X} {result['files_created']}")
    print(f"  {D}Escenarios BDD:{X} {result['bdd_scenarios']}")
    print(f"  {D}Tests TDD:{X} {result['tdd_tests']}")
    print(f"  {D}Endpoints API:{X} {result['api_endpoints']}")
    print()
    print(f"  {D}Estructura:{X}")
    for line in result['structure'][:15]:
        print(f"    {line}")
    print()
    print(f"  {C}💡 Siguiente paso:{X}")
    print(f"    cd {output_path}")
    print(f"    pip install -e .")
    print(f"    pytest tests/ -v")
    print()
    print(f"{P}  \"Dime QUÉ necesitas. El CÓMO es mi trabajo.\"{X}")
    print()


if __name__ == '__main__':
    asyncio.run(main())
