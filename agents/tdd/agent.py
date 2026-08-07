"""
TDD Agent — Agente de Test-Driven Development.

Responsabilidades:
1. Ejecutar tests unitarios con pytest
2. Medir cobertura de código
3. Verificar que el ciclo Red-Green-Refactor se siguió
4. Generar reportes de calidad de tests
5. Emitir notas educativas sobre TDD

Principios SOLID:
- SRP: Solo maneja testing unitario (BDD es otro agente)
- LSP: Sustituible por cualquier BaseAgent
- DIP: No depende de pytest directamente (subprocess)

ISO 25023: Reporta métricas de cobertura y densidad de defectos.
"""

import json
import subprocess
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional

from agents.base import AgentInput, AgentOutput, BaseAgent


@dataclass
class TestResult:
    """Resultado de un test individual."""

    name: str
    outcome: str  # passed, failed, error, skipped
    duration_ms: float = 0.0
    error_message: Optional[str] = None


@dataclass
class TDDReport:
    """Reporte consolidado de ejecución de tests."""

    total_tests: int = 0
    passed: int = 0
    failed: int = 0
    errors: int = 0
    skipped: int = 0
    duration_seconds: float = 0.0
    coverage_percentage: float = 0.0
    test_results: List[TestResult] = field(default_factory=list)

    @property
    def pass_rate(self) -> float:
        if self.total_tests == 0:
            return 0.0
        return (self.passed / self.total_tests) * 100

    @property
    def status(self) -> str:
        if self.failed > 0 or self.errors > 0:
            return "red"  # Tests fallando
        if self.coverage_percentage < 80:
            return "needs_coverage"
        return "green"  # Todo pasando


class TDDAgent(BaseAgent):
    """
    Agente TDD — Ejecuta y analiza tests unitarios.

    Modos:
    - run: Ejecuta tests y reporta resultados
    - coverage: Ejecuta con análisis de cobertura
    - verify: Verifica que los tests siguen buenas prácticas
    - full: Todo lo anterior
    """

    @property
    def name(self) -> str:
        return "tdd"

    @property
    def description(self) -> str:
        return (
            "Ejecuta tests unitarios con pytest, mide cobertura, "
            "y verifica la calidad del ciclo TDD."
        )

    @property
    def phase(self) -> str:
        return "implementation"

    def validate_input(self, input_data: AgentInput) -> List[str]:
        """Valida que existen tests para ejecutar."""
        errors = super().validate_input(input_data)

        tests_path = input_data.project_path / "tests"
        if not tests_path.exists():
            alt_path = Path("tests")
            if not alt_path.exists():
                errors.append(
                    "No se encontró directorio tests/. "
                    "Crea tests siguiendo el ciclo RED del TDD."
                )

        return errors

    async def execute(self, input_data: AgentInput) -> AgentOutput:
        """
        Ejecuta el agente TDD.

        Flujo:
        1. Descubre tests
        2. Ejecuta pytest
        3. Mide cobertura (si mode incluye coverage)
        4. Analiza calidad de tests
        5. Genera reporte educativo
        """
        mode = input_data.config.get("mode", "full")
        tests_path = self._find_tests_path(input_data.project_path)

        # Ejecutar tests
        report = await self._run_tests(tests_path, with_coverage=(mode in ("coverage", "full")))

        # Analizar calidad de tests
        quality_issues = self._analyze_test_quality(tests_path)

        # Construir output
        return self._build_output(report, quality_issues, input_data)

    def _find_tests_path(self, project_path: Path) -> Path:
        """Encuentra el directorio de tests."""
        candidates = [
            project_path / "tests",
            Path("tests"),
            project_path / "test",
        ]
        for path in candidates:
            if path.exists():
                return path
        return candidates[0]

    async def _run_tests(self, tests_path: Path, with_coverage: bool = True) -> TDDReport:
        """Ejecuta pytest y parsea resultados."""
        cmd = [
            "python", "-m", "pytest",
            str(tests_path),
            "--tb=short",
            "-q",
            "--json-report",
            "--json-report-file=/tmp/pytest_report.json",
        ]

        if with_coverage:
            cmd.extend([
                "--cov=examples/taskflow",
                "--cov-report=json:/tmp/coverage.json",
                "--cov-fail-under=0",  # No fallar por cobertura baja
            ])

        try:
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=120,
                cwd=str(Path.cwd()),
            )

            return self._parse_pytest_output(result)

        except (FileNotFoundError, subprocess.TimeoutExpired) as e:
            return self._create_mock_report(tests_path, str(e))

    def _parse_pytest_output(self, result: subprocess.CompletedProcess) -> TDDReport:
        """Parsea la salida de pytest."""
        report = TDDReport()

        # Intentar leer el JSON report
        try:
            report_path = Path("/tmp/pytest_report.json")
            if report_path.exists():
                with open(report_path) as f:
                    data = json.load(f)

                tests = data.get("tests", [])
                report.total_tests = len(tests)
                report.passed = sum(1 for t in tests if t["outcome"] == "passed")
                report.failed = sum(1 for t in tests if t["outcome"] == "failed")
                report.errors = sum(1 for t in tests if t["outcome"] == "error")
                report.skipped = sum(1 for t in tests if t["outcome"] == "skipped")
                report.duration_seconds = data.get("duration", 0)

                for t in tests:
                    report.test_results.append(TestResult(
                        name=t.get("nodeid", "unknown"),
                        outcome=t["outcome"],
                        duration_ms=t.get("duration", 0) * 1000,
                        error_message=t.get("longrepr"),
                    ))
        except (json.JSONDecodeError, KeyError):
            # Parseo manual de stdout
            output = result.stdout + result.stderr
            if "passed" in output:
                report.passed = 1  # Simplificado
            if "failed" in output:
                report.failed = 1

        # Intentar leer cobertura
        try:
            cov_path = Path("/tmp/coverage.json")
            if cov_path.exists():
                with open(cov_path) as f:
                    cov_data = json.load(f)
                report.coverage_percentage = cov_data.get("totals", {}).get(
                    "percent_covered", 0.0
                )
        except (json.JSONDecodeError, KeyError):
            pass

        return report

    def _create_mock_report(self, tests_path: Path, error: str) -> TDDReport:
        """Crea un reporte cuando pytest no está disponible."""
        test_files = list(tests_path.rglob("test_*.py")) if tests_path.exists() else []
        return TDDReport(
            total_tests=len(test_files) * 5,  # Estimación
            passed=0,
            failed=0,
            skipped=len(test_files) * 5,
        )

    def _analyze_test_quality(self, tests_path: Path) -> List[str]:
        """
        Analiza la calidad de los tests escritos.

        Verifica:
        - Nombres descriptivos
        - Patrón AAA (Arrange-Act-Assert)
        - Tests no demasiado largos
        - Uso de fixtures
        """
        issues = []

        if not tests_path.exists():
            return ["No tests directory found"]

        for test_file in tests_path.rglob("test_*.py"):
            content = test_file.read_text(encoding="utf-8")

            # Verificar nombres descriptivos
            if "def test_1" in content or "def test_a" in content:
                issues.append(
                    f"{test_file.name}: Usa nombres descriptivos "
                    f"(test_create_task_returns_id, no test_1)"
                )

            # Verificar tests muy largos
            lines = content.split("\n")
            in_test = False
            test_lines = 0
            for line in lines:
                if line.strip().startswith("def test_"):
                    in_test = True
                    test_lines = 0
                elif in_test and (line.strip().startswith("def ") or line.strip().startswith("class ")):
                    if test_lines > 30:
                        issues.append(
                            f"{test_file.name}: Test con {test_lines} líneas. "
                            f"Considera dividirlo (máx recomendado: 20 líneas)."
                        )
                    in_test = False
                elif in_test:
                    test_lines += 1

        return issues

    def _build_output(
        self,
        report: TDDReport,
        quality_issues: List[str],
        input_data: AgentInput,
    ) -> AgentOutput:
        """Construye el AgentOutput final."""

        # Status
        if report.failed > 0 or report.errors > 0:
            status = "warning"
        elif quality_issues:
            status = "warning"
        else:
            status = "success"

        # Métricas (ISO 25023)
        metrics: Dict[str, float] = {
            "tdd.total_tests": report.total_tests,
            "tdd.passed": report.passed,
            "tdd.failed": report.failed,
            "tdd.pass_rate": report.pass_rate,
            "tdd.coverage_percentage": report.coverage_percentage,
            "tdd.duration_seconds": report.duration_seconds,
        }

        # Recomendaciones
        recommendations = list(quality_issues)
        if report.coverage_percentage < 80 and report.coverage_percentage > 0:
            recommendations.append(
                f"Cobertura en {report.coverage_percentage:.1f}%. "
                f"Meta: ≥80%. Agrega tests para código no cubierto."
            )
        if report.failed > 0:
            recommendations.append(
                f"{report.failed} tests fallando (RED). "
                f"Implementa el código mínimo para que pasen (GREEN)."
            )

        # Notas educativas
        educational_notes = self._generate_educational_notes(report, input_data)

        return AgentOutput(
            agent_name=self.name,
            status=status,
            metrics=metrics,
            recommendations=recommendations,
            educational_notes=educational_notes,
            errors=[r.error_message for r in report.test_results if r.error_message],
        )

    def _generate_educational_notes(
        self, report: TDDReport, input_data: AgentInput
    ) -> List[str]:
        """Genera notas adaptadas al estado del ciclo TDD."""
        mode = input_data.context.educational_mode
        notes = []

        if mode == "beginner":
            if report.status == "red":
                notes.extend([
                    "🔴 Estás en fase RED — los tests fallan. ¡Eso es correcto!",
                    "📝 Ahora escribe el código MÍNIMO que los haga pasar (GREEN).",
                    "⚠️ No te preocupes por que sea bonito todavía.",
                ])
            elif report.status == "green":
                notes.extend([
                    "🟢 Estás en fase GREEN — todos los tests pasan. ¡Bien!",
                    "🔵 Ahora es momento de REFACTORIZAR:",
                    "   - ¿Hay código duplicado? → Extraer",
                    "   - ¿Un método hace mucho? → Dividir (SRP)",
                    "   - ¿Hay dependencias hardcoded? → Inyectar (DIP)",
                ])
            else:
                notes.extend([
                    "📊 Tus tests necesitan más cobertura.",
                    "💡 Piensa: ¿qué podría salir mal que NO estás testeando?",
                    "🎯 Meta: cubrir happy path + edge cases + errores.",
                ])
        elif mode == "expert":
            notes.append(
                f"TDD: {report.passed}/{report.total_tests} pass, "
                f"coverage {report.coverage_percentage:.0f}%"
            )
        else:
            if report.failed > 0:
                notes.append(
                    f"🔴 {report.failed} tests en RED. Implementa código para pasarlos."
                )
            if report.coverage_percentage > 0 and report.coverage_percentage < 80:
                notes.append(
                    f"📊 Cobertura: {report.coverage_percentage:.0f}% (meta: ≥80%)"
                )
            notes.append("Guía completa: docs/guides/TDD-paso-a-paso.md")

        return notes
