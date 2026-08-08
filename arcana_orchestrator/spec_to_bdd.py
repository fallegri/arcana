"""
Spec to BDD — Generador automático de escenarios Gherkin desde Spec Document.

Flujo: Spec Document → Escenarios BDD (Gherkin)

Para cada entidad del Spec genera:
- Feature de CRUD (crear, listar, obtener, eliminar)
- Feature de reglas de negocio (cada RN → escenario)
- Feature de seguridad/permisos (cada rol → qué puede/no puede)

Para cada regla de negocio genera:
- Escenario del happy path (la regla se cumple)
- Escenario del error path (la regla se viola → error claro)
"""

from dataclasses import dataclass
from typing import Dict, List
from pathlib import Path


@dataclass
class GeneratedFeature:
    """Un archivo .feature generado."""
    filename: str
    content: str
    scenarios_count: int


class SpecToBDD:
    """Convierte un Spec Document en escenarios BDD (Gherkin)."""

    def generate(
        self,
        entities: List[Dict],
        rules: List[str],
        roles: List[Dict],
        project_name: str,
        output_path: Path,
    ) -> List[GeneratedFeature]:
        """
        Genera archivos .feature desde la especificación.

        Args:
            entities: Entidades con campos
            rules: Reglas de negocio (RN01, RN02...)
            roles: Roles con permisos
            project_name: Nombre del proyecto
            output_path: Dónde crear los .feature

        Returns:
            Lista de features generados
        """
        features_dir = output_path / "features"
        features_dir.mkdir(parents=True, exist_ok=True)

        generated = []

        # 1. Feature de auth (siempre)
        auth_feature = self._generate_auth_feature(roles)
        (features_dir / "auth.feature").write_text(auth_feature.content, encoding="utf-8")
        generated.append(auth_feature)

        # 2. Feature CRUD por entidad
        for entity in entities:
            if entity["name"] == "User":
                continue
            crud_feature = self._generate_crud_feature(entity, roles)
            filename = f"{entity['name'].lower()}_crud.feature"
            (features_dir / filename).write_text(crud_feature.content, encoding="utf-8")
            generated.append(crud_feature)

        # 3. Feature de reglas de negocio
        if rules:
            rules_feature = self._generate_rules_feature(rules, entities, project_name)
            (features_dir / "reglas_negocio.feature").write_text(rules_feature.content, encoding="utf-8")
            generated.append(rules_feature)

        # 4. Feature de permisos/seguridad
        if roles and len(roles) > 1:
            perms_feature = self._generate_permissions_feature(roles, entities)
            (features_dir / "permisos.feature").write_text(perms_feature.content, encoding="utf-8")
            generated.append(perms_feature)

        return generated

    def _generate_auth_feature(self, roles: List[Dict]) -> GeneratedFeature:
        """Feature de autenticación."""
        roles_str = ", ".join(r["name"] for r in roles) if roles else "usuario"

        content = f"""# language: es
Característica: Autenticación y Registro
  Como usuario del sistema
  Quiero registrarme e iniciar sesión de forma segura
  Para acceder a las funcionalidades según mi rol

  Antecedentes:
    Dado que el sistema está operativo

  Escenario: Registro exitoso con datos válidos
    Cuando me registro con nombre, email y contraseña válida
    Entonces mi cuenta se crea exitosamente
    Y recibo confirmación de bienvenida
    Y puedo iniciar sesión inmediatamente

  Escenario: Registro con email duplicado falla
    Dado que ya existe un usuario con email "test@ejemplo.com"
    Cuando intento registrarme con el mismo email
    Entonces recibo error "Este email ya está registrado"
    Y no se crea cuenta duplicada

  Escenario: Contraseña debe cumplir requisitos de seguridad
    Cuando intento registrarme con contraseña "123"
    Entonces recibo error indicando los requisitos
    Y el mensaje menciona: mínimo 8 caracteres, mayúscula, número, especial

  Escenario: Login exitoso retorna token
    Dado que soy un usuario registrado
    Cuando inicio sesión con credenciales correctas
    Entonces recibo un token de sesión válido
    Y puedo acceder a los endpoints protegidos

  Escenario: Login fallido no revela información
    Cuando inicio sesión con credenciales incorrectas
    Entonces recibo error genérico "Credenciales inválidas"
    Y el mensaje NO revela si el email existe o no

  Escenario: Bloqueo por intentos fallidos consecutivos
    Cuando fallo el login 5 veces seguidas
    Entonces mi cuenta se bloquea temporalmente
    Y recibo mensaje indicando el bloqueo
"""
        return GeneratedFeature(
            filename="auth.feature",
            content=content,
            scenarios_count=6,
        )

    def _generate_crud_feature(self, entity: Dict, roles: List[Dict]) -> GeneratedFeature:
        """Feature CRUD para una entidad."""
        name = entity["name"]
        name_lower = name.lower()
        fields = entity.get("fields", [])

        # Determinar campos principales para los escenarios
        main_fields = [f for f in fields if f not in ("id", "user_id", "eliminado")][:4]
        fields_str = ", ".join(main_fields)

        # Rol que puede hacer CRUD
        crud_role = "usuario autenticado"
        if roles:
            crud_role = roles[0]["name"]

        content = f"""# language: es
Característica: Gestión de {name}
  Como {crud_role}
  Quiero gestionar {name_lower}s en el sistema
  Para mantener la información actualizada

  Antecedentes:
    Dado un {crud_role} autenticado en el sistema

  Escenario: Crear {name_lower} con datos válidos
    Cuando creo un {name_lower} con {fields_str}
    Entonces el {name_lower} se registra exitosamente
    Y recibo confirmación con el ID asignado
    Y el {name_lower} aparece en mi lista

  Escenario: Crear {name_lower} sin datos obligatorios falla
    Cuando intento crear un {name_lower} sin datos requeridos
    Entonces recibo error de validación claro
    Y el mensaje indica qué campo falta
    Y no se crea ningún registro

  Escenario: Listar {name_lower}s muestra solo los activos
    Dado que existen {name_lower}s activos y eliminados
    Cuando consulto la lista de {name_lower}s
    Entonces veo solo los activos
    Y los eliminados no aparecen

  Escenario: Obtener {name_lower} por ID
    Dado que existe un {name_lower} con ID conocido
    Cuando lo consulto por ID
    Entonces recibo sus datos completos

  Escenario: Obtener {name_lower} inexistente retorna error
    Cuando consulto un {name_lower} con ID que no existe
    Entonces recibo error 404
    Y el mensaje dice "{name} no encontrado"

  Escenario: Actualizar {name_lower}
    Dado que existe un {name_lower} registrado
    Cuando modifico sus datos
    Entonces los cambios se guardan correctamente
    Y la información actualizada se refleja al consultarlo

  Escenario: Eliminar {name_lower} es soft delete
    Dado que existe un {name_lower} activo
    Cuando lo elimino
    Entonces el {name_lower} ya no aparece en la lista
    Pero sus datos se preservan internamente
    Y es recuperable por el administrador

  Escenario: Eliminar {name_lower} inexistente retorna error
    Cuando intento eliminar un {name_lower} que no existe
    Entonces recibo error 404
"""
        return GeneratedFeature(
            filename=f"{name_lower}_crud.feature",
            content=content,
            scenarios_count=8,
        )

    def _generate_rules_feature(self, rules: List[str], entities: List[Dict], project_name: str) -> GeneratedFeature:
        """Feature de reglas de negocio."""
        scenarios = []

        for i, rule in enumerate(rules, 1):
            # Generar escenario para la regla
            scenario_title = rule[:60].rstrip(".")
            rule_lower = rule.lower()

            # Determinar si es restricción negativa o requisito positivo
            if any(w in rule_lower for w in ["no se puede", "no puede", "no permitir", "nunca"]):
                # Escenario de ERROR: intentar violar la regla
                scenarios.append(f"""
  Escenario: RN{i:02d} — {scenario_title}
    Dado un usuario autenticado
    Cuando intenta una operación que viola: "{rule}"
    Entonces el sistema rechaza la operación
    Y muestra un mensaje de error claro explicando la restricción
    Y no se modifica ningún dato""")
            elif any(w in rule_lower for w in ["debe", "siempre", "obligatorio"]):
                # Escenario de REQUISITO: verificar que se cumple
                scenarios.append(f"""
  Escenario: RN{i:02d} — {scenario_title}
    Dado un usuario autenticado
    Cuando realiza una operación normal
    Entonces el sistema verifica que: "{rule}"
    Y la operación se completa exitosamente""")
            else:
                # Escenario genérico
                scenarios.append(f"""
  Escenario: RN{i:02d} — {scenario_title}
    Dado las condiciones normales del sistema
    Cuando se evalúa la regla: "{rule}"
    Entonces el sistema se comporta según lo especificado""")

        content = f"""# language: es
Característica: Reglas de Negocio — {project_name}
  Como sistema
  Debo aplicar las reglas de negocio definidas
  Para mantener la integridad de los datos y procesos
{"".join(scenarios)}
"""
        return GeneratedFeature(
            filename="reglas_negocio.feature",
            content=content,
            scenarios_count=len(rules),
        )

    def _generate_permissions_feature(self, roles: List[Dict], entities: List[Dict]) -> GeneratedFeature:
        """Feature de permisos por rol."""
        scenarios = []
        entity_names = [e["name"] for e in entities if e["name"] != "User"]

        for role in roles:
            role_name = role["name"]
            scenarios.append(f"""
  Escenario: {role_name} accede solo a lo que tiene permiso
    Dado un usuario con rol "{role_name}"
    Cuando intenta acceder a funcionalidades del sistema
    Entonces solo puede realizar las operaciones de su rol
    Y las operaciones no autorizadas retornan error 403""")

        # Escenario de aislamiento de datos
        if len(roles) > 1:
            scenarios.append(f"""
  Escenario: Un usuario no puede ver datos de otro usuario
    Dado dos usuarios con el mismo rol
    Cuando el usuario A consulta sus datos
    Entonces NO puede ver los datos del usuario B
    Y cada usuario solo accede a su propia información""")

        # Escenario de admin
        if any(r["name"] in ("admin", "administrador") for r in roles):
            scenarios.append(f"""
  Escenario: Admin puede ver todos los datos
    Dado un usuario con rol "admin"
    Cuando consulta el sistema
    Entonces puede ver datos de todos los usuarios
    Y puede realizar operaciones de gestión""")

        content = f"""# language: es
Característica: Control de Acceso y Permisos
  Como sistema seguro
  Debo verificar los permisos en cada operación
  Para que cada usuario solo haga lo que su rol permite
{"".join(scenarios)}
"""
        return GeneratedFeature(
            filename="permisos.feature",
            content=content,
            scenarios_count=len(scenarios),
        )
