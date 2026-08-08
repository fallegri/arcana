"""
Skill Matcher — Detecta y activa skills según el contexto del proyecto.

Analiza el texto del usuario y determina qué skills cargar.
Cada skill activado aporta: templates, prompts expertos, y reglas.
"""

from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional
import yaml


@dataclass
class SkillConfig:
    """Configuración de un skill."""
    name: str
    description: str
    triggers: List[str]
    category: str
    dependencies: List[str] = field(default_factory=list)
    priority: int = 5  # 1-10, mayor = más prioritario


@dataclass
class ActiveSkill:
    """Un skill activado con su contenido cargado."""
    config: SkillConfig
    templates: Dict[str, str] = field(default_factory=dict)
    prompts: Dict[str, str] = field(default_factory=dict)
    design_rules: List[str] = field(default_factory=list)


class SkillMatcher:
    """
    Detecta qué skills activar según el contexto del proyecto.

    Flujo:
    1. Recibe texto del usuario (descripción del proyecto)
    2. Busca triggers que coincidan
    3. Carga los skills activados (templates + prompts)
    4. Retorna lista de ActiveSkills para que el Builder/Orchestrator use
    """

    def __init__(self, skills_dir: Optional[Path] = None):
        self._skills_dir = skills_dir or Path(__file__).parent
        self._skills: Dict[str, SkillConfig] = {}
        self._load_skills()

    def _load_skills(self):
        """Carga configuración de todos los skills disponibles."""
        for skill_dir in self._skills_dir.iterdir():
            if not skill_dir.is_dir() or skill_dir.name.startswith("_"):
                continue
            yaml_file = skill_dir / "skill.yaml"
            if yaml_file.exists():
                try:
                    data = yaml.safe_load(yaml_file.read_text(encoding="utf-8"))
                    self._skills[skill_dir.name] = SkillConfig(**data)
                except Exception:
                    pass

    def match(self, user_input: str) -> List[ActiveSkill]:
        """
        Detecta skills que deben activarse según el input del usuario.

        Returns:
            Lista de ActiveSkills ordenados por prioridad
        """
        text_lower = user_input.lower()
        activated = []

        for skill_name, config in self._skills.items():
            # Verificar si algún trigger coincide
            if any(trigger in text_lower for trigger in config.triggers):
                skill = self._load_skill_content(skill_name, config)
                activated.append(skill)

        # Ordenar por prioridad (mayor primero)
        activated.sort(key=lambda s: s.config.priority, reverse=True)
        return activated

    def _load_skill_content(self, skill_name: str, config: SkillConfig) -> ActiveSkill:
        """Carga templates y prompts de un skill."""
        skill_dir = self._skills_dir / skill_name
        skill = ActiveSkill(config=config)

        # Cargar templates
        templates_dir = skill_dir / "templates"
        if templates_dir.exists():
            for tf in templates_dir.glob("*"):
                if tf.is_file():
                    try:
                        skill.templates[tf.stem] = tf.read_text(encoding="utf-8")
                    except Exception:
                        pass

        # Cargar prompts
        prompts_dir = skill_dir / "prompts"
        if prompts_dir.exists():
            for pf in prompts_dir.glob("*.md"):
                try:
                    skill.prompts[pf.stem] = pf.read_text(encoding="utf-8")
                except Exception:
                    pass

        return skill

    def list_available(self) -> List[SkillConfig]:
        """Lista todos los skills disponibles."""
        return list(self._skills.values())

    def get_skill_summary(self, activated: List[ActiveSkill]) -> str:
        """Genera resumen de skills activados para mostrar al usuario."""
        if not activated:
            return "No se activaron skills adicionales."

        lines = ["### 🎯 Skills Activados:", ""]
        for skill in activated:
            lines.append(f"- **{skill.config.name}** — {skill.config.description}")
            if skill.prompts:
                lines.append(f"  Templates: {len(skill.templates)} | Prompts: {len(skill.prompts)}")
        return "\n".join(lines)
