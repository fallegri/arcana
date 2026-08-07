#!/usr/bin/env python3
"""
Arcana Tutor — CLI independiente.

Uso:
  python -m arcana_tutor --topic owasp --level beginner
  python -m arcana_tutor --topic solid --level intermediate --type fix_code
  python -m arcana_tutor --evaluate ./mi-solucion.py --challenge CH-001
  python -m arcana_tutor --hint --challenge CH-001
  python -m arcana_tutor --solution --challenge CH-001
"""

import sys
sys.path.insert(0, str(__import__('pathlib').Path(__file__).parent.parent))

import argparse
import asyncio
from pathlib import Path

from arcana_tutor.engine import TutorEngine

P = '\033[35m'; C = '\033[36m'; G = '\033[32m'
Y = '\033[33m'; R = '\033[31m'; B = '\033[1m'
D = '\033[2m'; X = '\033[0m'


def parse_args():
    parser = argparse.ArgumentParser(
        prog='arcana-tutor',
        description='🔮 Arcana Tutor — Aprende con retos interactivos',
    )
    parser.add_argument('--topic', '-t',
                        choices=['owasp', 'solid', 'tdd', 'bdd', 'api_resilience'],
                        help='Tema del reto')
    parser.add_argument('--level', '-l',
                        choices=['beginner', 'intermediate', 'advanced'],
                        default='beginner', help='Nivel de dificultad')
    parser.add_argument('--type', choices=[
                        'fix_code', 'identify_bug', 'write_test',
                        'code_review', 'multiple_choice'],
                        default='fix_code', help='Tipo de ejercicio')
    parser.add_argument('--subtopic', help='Subtema específico (ej: A03, SRP)')
    parser.add_argument('--context', help='Contexto profesional (ej: "soy abogado")')
    parser.add_argument('--evaluate', '-e', help='Archivo con tu solución para evaluar')
    parser.add_argument('--challenge', help='ID del reto (para evaluate/hint/solution)')
    parser.add_argument('--hint', action='store_true', help='Pedir pista')
    parser.add_argument('--solution', action='store_true', help='Ver solución completa')
    return parser.parse_args()


async def main():
    args = parse_args()
    engine = TutorEngine()

    print(f"{P}{B}")
    print("╭──────────────────────────────────────────────────────────────╮")
    print("│  🔮 ARCANA TUTOR — Aprende desarrollo profesional con retos   │")
    print("╰──────────────────────────────────────────────────────────────╯")
    print(f"{X}")

    # MODO: Pedir pista
    if args.hint and args.challenge:
        hint = engine.get_hint(args.challenge)
        print(f"\n  {Y}💡 Pista para {args.challenge}:{X}")
        print(f"  {C}{hint}{X}\n")
        return

    # MODO: Ver solución
    if args.solution and args.challenge:
        solution = engine.get_solution(args.challenge)
        print(f"\n  {G}✅ Solución de {args.challenge}:{X}\n")
        print(f"{solution}\n")
        return

    # MODO: Evaluar solución del alumno
    if args.evaluate and args.challenge:
        solution_path = Path(args.evaluate)
        if not solution_path.exists():
            print(f"{R}❌ Archivo no encontrado: {args.evaluate}{X}")
            sys.exit(1)

        student_code = solution_path.read_text(encoding="utf-8")
        result = await engine.evaluate(args.challenge, student_code)

        score_color = G if result["score"] >= 8 else Y if result["score"] >= 5 else R
        print(f"\n  {B}📝 Evaluación de tu solución:{X}\n")
        print(f"  Score: {score_color}{B}{result['score']}/{result['max_score']}{X}")
        print(f"  Estado: {'✅ APROBADO' if result['passed'] else '❌ Necesita mejoras'}")
        print()

        if result["feedback"]:
            print(f"  {G}Lo que hiciste bien:{X}")
            for f in result["feedback"]:
                print(f"    ✅ {f}")

        if result["missing"]:
            print(f"\n  {Y}Lo que te faltó:{X}")
            for m in result["missing"]:
                print(f"    ⚠️ {m}")

        if result["extra_credit"]:
            print(f"\n  {C}🌟 Extra credit:{X}")
            for e in result["extra_credit"]:
                print(f"    🌟 {e}")

        print()
        return

    # MODO: Generar reto nuevo
    if not args.topic:
        print(f"  {Y}Necesito un tema. Opciones: owasp, solid, tdd, bdd, api_resilience{X}")
        print(f"  Ejemplo: python -m arcana_tutor --topic owasp --level beginner")
        return

    challenge = engine.generate_challenge(
        topic=args.topic,
        level=args.level,
        subtopic=args.subtopic,
        exercise_type=args.type,
        context=args.context,
    )

    print(f"  {D}Tema:{X} {args.topic} | {D}Nivel:{X} {args.level} | {D}Tipo:{X} {args.type}")
    print(f"  {D}ID del reto:{X} {B}{challenge['id']}{X}")
    print()
    print(f"  {B}═══ RETO: {challenge['title']} ═══{X}")
    print()
    print(f"  {C}{challenge['description']}{X}")
    print()
    print(f"  {D}{'─' * 60}{X}")
    print(f"  {B}Código con problema:{X}")
    print()
    for line in challenge['bad_code'].split('\n'):
        print(f"    {line}")
    print()
    print(f"  {D}{'─' * 60}{X}")
    print(f"  {Y}📝 Tu trabajo:{X} Corrige el código y guárdalo en un archivo.")
    print(f"  {Y}   Luego evalúa:{X} python -m arcana_tutor --evaluate ./tu-fix.py --challenge {challenge['id']}")
    if challenge.get('hints_available'):
        print(f"  {C}💡 Pistas:{X} python -m arcana_tutor --hint --challenge {challenge['id']}")
    print()
    print(f"{P}  \"Dime qué quieres aprender. Yo te guío.\"{X}")
    print()


if __name__ == '__main__':
    asyncio.run(main())
