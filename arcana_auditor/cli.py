#!/usr/bin/env python3
"""
Arcana Auditor — CLI independiente.

Uso:
  python -m arcana_auditor --project ./mi-app/
  python -m arcana_auditor --project ./mi-app/ --fix
  python -m arcana_auditor --project ./mi-app/ --report audit
"""

import sys
sys.path.insert(0, str(__import__('pathlib').Path(__file__).parent.parent))

import argparse
import asyncio
from pathlib import Path

from arcana_auditor.engine import AuditorEngine

P = '\033[35m'; C = '\033[36m'; G = '\033[32m'
Y = '\033[33m'; R = '\033[31m'; B = '\033[1m'
D = '\033[2m'; X = '\033[0m'


def parse_args():
    parser = argparse.ArgumentParser(
        prog='arcana-auditor',
        description='🔮 Arcana Auditor — Auditoría de Software (criterios NO negociables)',
    )
    parser.add_argument('--project', '-p', required=True,
                        help='Ruta al proyecto a auditar')
    parser.add_argument('--fix', '-f', action='store_true',
                        help='Aplicar correcciones automáticas (acción correctiva)')
    parser.add_argument('--report', '-r', choices=['summary', 'audit', 'full'],
                        default='summary', help='Formato de reporte')
    return parser.parse_args()


async def main():
    args = parse_args()
    project_path = Path(args.project).resolve()

    if not project_path.exists():
        print(f"{R}❌ Error: '{args.project}' no existe.{X}")
        sys.exit(1)

    print(f"{P}{B}")
    print("╭──────────────────────────────────────────────────────────────╮")
    print("│  🔮 ARCANA AUDITOR — Criterios NO negociables                 │")
    print("╰──────────────────────────────────────────────────────────────╯")
    print(f"{X}")
    print(f"  {D}Proyecto:{X} {B}{project_path}{X}")
    print(f"  {D}Modo fix:{X} {'🔧 Activado' if args.fix else '❌ Solo reporte'}")
    print()

    engine = AuditorEngine()

    # PASO 1: Analizar (siempre)
    print(f"{C}  ▶ Analizando...{X}")
    result = await engine.analyze(project_path)

    # Mostrar scores
    solid = result.scores.get("solid", 0)
    owasp = result.scores.get("owasp", 0)
    sc = G if solid >= 80 else Y if solid >= 50 else R
    oc = G if owasp >= 80 else Y if owasp >= 50 else R
    print(f"    SOLID: {sc}{solid:.1f}/100{X}")
    print(f"    OWASP: {oc}{owasp:.1f}/100{X}")
    print(f"    Hallazgos: {len(result.findings)} ({result.critical_count} critical)")
    print(f"    Veredicto: {B}{result.overall_status}{X}")
    print()

    if result.findings:
        print(f"  {D}Hallazgos:{X}")
        for f in result.findings[:10]:
            sev = {"critical": f"{R}🔴", "high": f"{Y}🟠", "medium": f"{Y}🟡", "low": f"{G}🟢"}
            print(f"    {sev.get(f.severity, '⚪')} [{f.category}] {f.description[:70]}{X}")
        print()

    # PASO 2: Fix (solo si --fix)
    if args.fix and not result.is_conforming:
        print(f"{G}{B}  ▶ Aplicando correcciones...{X}")
        fix_result = await engine.fix(project_path, result)
        print(f"    Correcciones aplicadas: {len(fix_result.fixes_applied)}")
        print(f"    Archivos modificados: {len(fix_result.files_modified)}")
        for fa in fix_result.fixes_applied[:5]:
            print(f"    {G}🔧 {fa.file_path}:{fa.line_number} → {fa.description[:50]}{X}")
        print()

        # PASO 2b: Verificar
        print(f"{C}  ▶ Verificando correcciones...{X}")
        post_result = await engine.analyze(project_path)
        ps = post_result.scores.get("solid", 0)
        po = post_result.scores.get("owasp", 0)
        print(f"    SOLID: {solid:.1f} → {ps:.1f} ({ps-solid:+.1f})")
        print(f"    OWASP: {owasp:.1f} → {po:.1f} ({po-owasp:+.1f})")
        print()
    else:
        fix_result = None

    # PASO 3: Reporte (si --report audit o full)
    if args.report in ("audit", "full"):
        print(f"{C}  ▶ Generando reporte de auditoría...{X}")
        report_path = engine.generate_report(project_path, result, args.report, fix_result)
        print(f"    {G}📄 Reporte: {report_path}{X}")
        print()

    # Footer
    print(f"{P}  ═══════════════════════════════════════════════════════════════")
    print(f"  \"El estándar es el estándar. No se negocia.\"{X}")
    print()


if __name__ == '__main__':
    asyncio.run(main())
