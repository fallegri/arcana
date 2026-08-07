"""
Requirements Engineer — Fase de Elicitación de Requisitos.

Antes de generar NADA, actúa como Ingeniero de Software Senior:
1. Analiza lo que el usuario dijo
2. Identifica qué NO sabe o NO entiende
3. Genera preguntas específicas para completar la información
4. Propone entidades y pide confirmación
5. Solo cuando tiene TODO claro → pasa al Builder

Técnicas de elicitación implementadas:
- Cuestionario dirigido (preguntas por categoría)
- Análisis de dominio (detectar entidades y relaciones)
- Grupo focal simulado (perspectivas: usuario, admin, auditor)
- Validación de completitud (¿falta algo?)
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple


@dataclass
class RequirementsAnalysis:
    """Resultado del análisis de requisitos."""

    # Lo que SÍ entendimos
    understood: Dict[str, str] = field(default_factory=dict)

    # Lo que NO sabemos y necesitamos preguntar
    questions: List[Dict[str, str]] = field(default_factory=list)

    # Entidades propuestas (para confirmar con el usuario)
    proposed_entities: List[Dict] = field(default_factory=list)

    # Relaciones detectadas entre entidades
    proposed_relations: List[str] = field(default_factory=list)

    # Reglas de negocio detectadas
    detected_rules: List[str] = field(default_factory=list)

    # Gaps (información faltante crítica)
    gaps: List[str] = field(default_factory=list)

    # Completitud (0-100%)
    completeness: float = 0.0

    # ¿Está listo para generar?
    ready_to_build: bool = False


class RequirementsEngineer:
    """
    Ingeniero de Requisitos — Fase de elicitación.

    Personalidad: Ingeniero de Software Senior que NO asume nada.
    "Antes de construir, necesito entender EXACTAMENTE qué necesitás."

    Técnicas:
    1. Análisis semántico del texto del usuario
    2. Detección de entidades y atributos
    3. Identificación de gaps
    4. Generación de preguntas dirigidas
    5. Validación de completitud
    """

    # Categorías de preguntas que el ingeniero debe cubrir
    CATEGORIES = [
        "domain",       # ¿Qué es el sistema? ¿Qué problema resuelve?
        "entities",     # ¿Qué "cosas" maneja? ¿Qué datos tienen?
        "actors",       # ¿Quién lo usa? ¿Qué roles hay?
        "operations",   # ¿Qué operaciones se hacen sobre cada cosa?
        "rules",        # ¿Qué restricciones hay? ¿Qué NO se puede hacer?
        "security",     # ¿Quién puede hacer qué? ¿Hay datos sensibles?
        "integrations", # ¿Se conecta con algo externo?
        "ux",           # ¿Cómo interactúa el usuario? ¿CLI, web, API?
    ]

    def analyze(self, user_input: str, project_name: str = "") -> RequirementsAnalysis:
        """
        Analiza lo que el usuario proporcionó y determina qué falta.

        Returns:
            RequirementsAnalysis con lo entendido, preguntas, y entidades propuestas
        """
        analysis = RequirementsAnalysis()

        # 1. Extraer lo que SÍ entendemos
        analysis.understood = self._extract_understood(user_input)

        # 2. Detectar entidades
        analysis.proposed_entities = self._detect_entities(user_input)

        # 3. Detectar relaciones
        analysis.proposed_relations = self._detect_relations(user_input, analysis.proposed_entities)

        # 4. Detectar reglas de negocio
        analysis.detected_rules = self._detect_rules(user_input)

        # 5. Identificar gaps (qué falta)
        analysis.gaps = self._identify_gaps(user_input, analysis)

        # 6. Generar preguntas para completar
        analysis.questions = self._generate_questions(user_input, analysis)

        # 7. Calcular completitud
        analysis.completeness = self._calculate_completeness(analysis)
        analysis.ready_to_build = analysis.completeness >= 80.0

        return analysis

    def generate_questionnaire(self, analysis: RequirementsAnalysis) -> str:
        """
        Genera un cuestionario formateado para el usuario.

        El cuestionario es lo que el MCP retorna para que la IA
        le pregunte al usuario.
        """
        lines = [
            "## 🔮 Arcana — Ingeniería de Requisitos",
            "",
            f"**Completitud actual: {analysis.completeness:.0f}%**",
            "",
        ]

        if analysis.completeness >= 80:
            lines.append("✅ Tengo suficiente información para comenzar.")
            lines.append("Pero estas preguntas opcionales mejorarían el resultado:")
            lines.append("")
        else:
            lines.append("⚠️ Necesito más información antes de construir.")
            lines.append("Por favor respondé estas preguntas:")
            lines.append("")

        # Mostrar lo que entendimos
        if analysis.understood:
            lines.append("### ✅ Lo que entendí:")
            lines.append("")
            for key, value in analysis.understood.items():
                lines.append(f"- **{key}**: {value}")
            lines.append("")

        # Entidades propuestas
        if analysis.proposed_entities:
            lines.append("### 📦 Entidades que voy a crear:")
            lines.append("")
            for entity in analysis.proposed_entities:
                fields_str = ", ".join(entity.get("fields", []))
                lines.append(f"- **{entity['name']}** ({fields_str})")
            lines.append("")
            lines.append("*¿Son correctas? ¿Falta alguna? ¿Sobra alguna?*")
            lines.append("")

        # Reglas detectadas
        if analysis.detected_rules:
            lines.append("### 📋 Reglas de negocio detectadas:")
            lines.append("")
            for rule in analysis.detected_rules:
                lines.append(f"- {rule}")
            lines.append("")

        # Preguntas
        if analysis.questions:
            lines.append("### ❓ Preguntas:")
            lines.append("")
            for i, q in enumerate(analysis.questions, 1):
                category_icon = {
                    "domain": "🏢", "entities": "📦", "actors": "👥",
                    "operations": "⚙️", "rules": "📋", "security": "🔒",
                    "integrations": "🔌", "ux": "🖥️",
                }.get(q["category"], "❓")
                priority = "⚡" if q.get("priority") == "high" else ""
                lines.append(f"{i}. {category_icon} {priority} **{q['question']}**")
                if q.get("hint"):
                    lines.append(f"   *Pista: {q['hint']}*")
                lines.append("")

        # Gaps críticos
        if analysis.gaps:
            lines.append("### 🚨 Información faltante crítica:")
            lines.append("")
            for gap in analysis.gaps:
                lines.append(f"- ⚠️ {gap}")
            lines.append("")

        return "\n".join(lines)

    def refine(self, analysis: RequirementsAnalysis, user_answers: str) -> RequirementsAnalysis:
        """
        Refina el análisis con las respuestas del usuario.

        Se llama DESPUÉS de que el usuario respondió las preguntas.
        Actualiza entidades, reglas, y recalcula completitud.
        """
        # Agregar lo nuevo al entendimiento
        new_entities = self._detect_entities(user_answers)
        for entity in new_entities:
            if entity not in analysis.proposed_entities:
                analysis.proposed_entities.append(entity)

        new_rules = self._detect_rules(user_answers)
        for rule in new_rules:
            if rule not in analysis.detected_rules:
                analysis.detected_rules.append(rule)

        # Recalcular
        combined = " ".join(analysis.understood.values()) + " " + user_answers
        analysis.gaps = self._identify_gaps(combined, analysis)
        analysis.completeness = self._calculate_completeness(analysis)
        analysis.ready_to_build = analysis.completeness >= 80.0

        return analysis

    # ═══════════════════════════════════════════════════════════════
    # MÉTODOS INTERNOS DE ANÁLISIS
    # ═══════════════════════════════════════════════════════════════

    def _extract_understood(self, text: str) -> Dict[str, str]:
        """Extrae lo que entendemos del texto."""
        understood = {}
        text_lower = text.lower()

        # Tipo de sistema
        system_types = {
            "calculadora": "Calculadora / sistema de cálculo",
            "inventario": "Sistema de gestión de inventario",
            "reserva": "Sistema de reservas",
            "pedido": "Sistema de pedidos / e-commerce",
            "expediente": "Sistema de gestión documental/legal",
            "receta": "Sistema de recetas / gastronomía",
            "tarea": "Sistema de gestión de tareas",
            "factur": "Sistema de facturación",
            "blog": "Sistema de contenido / blog",
            "chat": "Sistema de mensajería",
            "tienda": "E-commerce / tienda online",
            "clínica": "Sistema de gestión clínica",
            "escuela": "Sistema de gestión educativa",
            "hotel": "Sistema de gestión hotelera",
        }

        for keyword, desc in system_types.items():
            if keyword in text_lower:
                understood["Tipo de sistema"] = desc
                break

        # Operaciones mencionadas
        operations = []
        op_keywords = {
            "sumar": "suma", "restar": "resta", "multiplicar": "multiplicación",
            "dividir": "división", "crear": "creación", "eliminar": "eliminación",
            "listar": "listado", "buscar": "búsqueda", "reservar": "reserva",
            "comprar": "compra", "vender": "venta", "registrar": "registro",
            "calcular": "cálculo", "generar": "generación", "exportar": "exportación",
        }
        for kw, op in op_keywords.items():
            if kw in text_lower:
                operations.append(op)
        if operations:
            understood["Operaciones"] = ", ".join(operations)

        # Usuarios mencionados
        actors = []
        actor_keywords = ["usuario", "admin", "cliente", "vendedor", "gerente",
                          "almacenero", "auditor", "comprador", "chef", "abogado"]
        for actor in actor_keywords:
            if actor in text_lower:
                actors.append(actor)
        if actors:
            understood["Actores"] = ", ".join(actors)

        # Restricciones explícitas
        restrictions = []
        for line in text.split("\n"):
            line_lower = line.lower().strip()
            if any(w in line_lower for w in ["no se puede", "debe", "máximo", "mínimo", "solo", "obligatorio"]):
                restrictions.append(line.strip().lstrip("- •*"))
        if restrictions:
            understood["Restricciones"] = f"{len(restrictions)} reglas detectadas"

        return understood

    def _detect_entities(self, text: str) -> List[Dict]:
        """Detecta entidades del dominio con campos sugeridos."""
        text_lower = text.lower()
        entities = []

        # Mapa ampliado de entidades
        entity_map = {
            # Operaciones/Cálculos
            "calculadora": {"name": "Operation", "fields": ["id", "operacion", "operando_a", "operando_b", "resultado", "user_id", "fecha"]},
            "operacion": {"name": "Operation", "fields": ["id", "tipo", "operando_a", "operando_b", "resultado", "user_id", "fecha"]},
            "historial": {"name": "OperationHistory", "fields": ["id", "operation_id", "user_id", "fecha", "expresion", "resultado"]},
            # Inventario
            "producto": {"name": "Product", "fields": ["id", "sku", "nombre", "descripcion", "categoria", "precio", "stock", "stock_minimo", "stock_maximo"]},
            "bodega": {"name": "Warehouse", "fields": ["id", "nombre", "direccion", "capacidad", "ocupacion"]},
            "movimiento": {"name": "Movement", "fields": ["id", "product_id", "warehouse_id", "tipo", "cantidad", "motivo", "referencia", "user_id", "fecha"]},
            "proveedor": {"name": "Supplier", "fields": ["id", "nombre", "ruc", "contacto", "email", "telefono", "condiciones_pago"]},
            # Reservas
            "reserva": {"name": "Reservation", "fields": ["id", "fecha", "hora", "personas", "mesa_id", "cliente_id", "estado", "notas"]},
            "mesa": {"name": "Table", "fields": ["id", "numero", "capacidad", "ubicacion", "estado"]},
            # Comercio
            "pedido": {"name": "Order", "fields": ["id", "cliente_id", "items", "total", "estado", "fecha", "direccion_envio"]},
            "carrito": {"name": "Cart", "fields": ["id", "user_id", "items", "total"]},
            # Personas
            "cliente": {"name": "Client", "fields": ["id", "nombre", "email", "telefono", "direccion", "documento"]},
            "usuario": {"name": "User", "fields": ["id", "nombre", "email", "password_hash", "rol", "activo", "intentos_fallidos"]},
            # Documentos
            "expediente": {"name": "Case", "fields": ["id", "numero", "titulo", "descripcion", "estado", "cliente_id", "abogado_id", "fecha_apertura"]},
            "factura": {"name": "Invoice", "fields": ["id", "numero", "cliente_id", "items", "subtotal", "impuesto", "total", "estado", "fecha"]},
            # Contenido
            "tarea": {"name": "Task", "fields": ["id", "titulo", "descripcion", "estado", "prioridad", "user_id", "fecha_limite"]},
            "receta": {"name": "Recipe", "fields": ["id", "nombre", "ingredientes", "instrucciones", "porciones", "tiempo_minutos", "dificultad"]},
            "ingrediente": {"name": "Ingredient", "fields": ["id", "nombre", "unidad", "stock", "precio_unitario"]},
        }

        # Siempre incluir User
        entities.append(entity_map["usuario"])

        # Detectar por keywords
        for keyword, entity in entity_map.items():
            if keyword in text_lower and entity["name"] not in [e["name"] for e in entities]:
                entities.append(entity)

        # Si habla de "historial" o "registro" sin entidad específica
        if ("historial" in text_lower or "registro" in text_lower) and not any(e["name"] == "OperationHistory" for e in entities):
            if "calculadora" in text_lower or "operacion" in text_lower:
                entities.append(entity_map["historial"])

        return entities

    def _detect_relations(self, text: str, entities: List[Dict]) -> List[str]:
        """Detecta relaciones entre entidades."""
        relations = []
        entity_names = [e["name"] for e in entities]

        # Relaciones comunes
        if "User" in entity_names and "Operation" in entity_names:
            relations.append("User 1──N Operation (un usuario tiene muchas operaciones)")
        if "User" in entity_names and "OperationHistory" in entity_names:
            relations.append("User 1──N OperationHistory (historial por usuario)")
        if "Product" in entity_names and "Movement" in entity_names:
            relations.append("Product 1──N Movement (un producto tiene muchos movimientos)")
        if "Client" in entity_names and "Reservation" in entity_names:
            relations.append("Client 1──N Reservation (un cliente tiene muchas reservas)")
        if "Table" in entity_names and "Reservation" in entity_names:
            relations.append("Table 1──N Reservation (una mesa tiene muchas reservas)")
        if "Client" in entity_names and "Order" in entity_names:
            relations.append("Client 1──N Order (un cliente tiene muchos pedidos)")
        if "Client" in entity_names and "Invoice" in entity_names:
            relations.append("Client 1──N Invoice (un cliente tiene muchas facturas)")

        return relations

    def _detect_rules(self, text: str) -> List[str]:
        """Extrae reglas de negocio explícitas."""
        rules = []
        for line in text.split("\n"):
            line_stripped = line.strip().lstrip("- •*")
            if not line_stripped:
                continue
            line_lower = line_stripped.lower()
            if any(w in line_lower for w in [
                "no se puede", "no puede", "debe", "solo", "máximo", "mínimo",
                "obligatorio", "nunca", "siempre", "no permitir", "no exceder",
                "antes de", "después de", "requiere", "validar",
            ]):
                rules.append(line_stripped)
        return rules

    def _identify_gaps(self, text: str, analysis: RequirementsAnalysis) -> List[str]:
        """Identifica información faltante crítica."""
        gaps = []
        text_lower = text.lower()

        # ¿Tiene entidades claras?
        if len(analysis.proposed_entities) <= 1:
            gaps.append("No se detectaron entidades específicas del dominio (solo User genérico)")

        # ¿Tiene operaciones claras?
        if "Operaciones" not in analysis.understood:
            gaps.append("No se identificaron operaciones concretas (CRUD, cálculos, etc.)")

        # ¿Tiene roles/actores?
        if "Actores" not in analysis.understood:
            gaps.append("No se identificaron roles de usuario (¿quién usa el sistema?)")

        # ¿Tiene reglas de negocio?
        if len(analysis.detected_rules) == 0:
            gaps.append("No se detectaron reglas de negocio ni restricciones")

        # ¿Falta información de interfaz?
        if not any(w in text_lower for w in ["api", "web", "cli", "móvil", "interfaz", "pantalla"]):
            gaps.append("No se especificó el tipo de interfaz (API REST, web, CLI, móvil)")

        return gaps

    def _generate_questions(self, text: str, analysis: RequirementsAnalysis) -> List[Dict[str, str]]:
        """Genera preguntas inteligentes basadas en los gaps."""
        questions = []
        text_lower = text.lower()

        # Preguntas por gaps detectados
        if len(analysis.proposed_entities) <= 1:
            questions.append({
                "category": "entities",
                "question": "¿Qué 'cosas' principales maneja tu sistema? (ej: productos, pedidos, clientes...)",
                "hint": "Pensá en las 'tablas' que necesitarías en una base de datos",
                "priority": "high",
            })

        if "Actores" not in analysis.understood:
            questions.append({
                "category": "actors",
                "question": "¿Quiénes usan el sistema? ¿Hay roles diferentes? (ej: admin, vendedor, cliente)",
                "hint": "Cada rol puede tener permisos diferentes",
                "priority": "high",
            })

        if len(analysis.detected_rules) == 0:
            questions.append({
                "category": "rules",
                "question": "¿Qué restricciones o reglas tiene tu negocio? (ej: stock no puede ser negativo, máximo 10 por pedido)",
                "hint": "Pensá: ¿qué NO debería poder pasar en el sistema?",
                "priority": "high",
            })

        # Preguntas específicas del dominio
        if "calculadora" in text_lower:
            if "historial" not in text_lower:
                questions.append({
                    "category": "operations",
                    "question": "¿Necesitás que guarde un historial de operaciones realizadas?",
                    "hint": "Útil para auditoría o para que el usuario vea sus cálculos anteriores",
                    "priority": "medium",
                })
            if not any(w in text_lower for w in ["avanzad", "científic", "potencia", "raíz"]):
                questions.append({
                    "category": "domain",
                    "question": "¿Solo operaciones básicas (+ - × ÷) o también avanzadas (potencia, raíz, porcentaje)?",
                    "hint": "",
                    "priority": "medium",
                })

        if "inventario" in text_lower:
            if "bodega" not in text_lower and "almacén" not in text_lower:
                questions.append({
                    "category": "entities",
                    "question": "¿Manejás una sola bodega/almacén o varias? ¿Necesitás transferencias entre ellas?",
                    "hint": "",
                    "priority": "medium",
                })
            if "vencimiento" not in text_lower and "caducidad" not in text_lower:
                questions.append({
                    "category": "rules",
                    "question": "¿Los productos tienen fecha de vencimiento? ¿Necesitás alertas?",
                    "hint": "",
                    "priority": "low",
                })

        # Preguntas genéricas de completitud
        if not any(w in text_lower for w in ["reporte", "informe", "dashboard", "estadístic"]):
            questions.append({
                "category": "operations",
                "question": "¿Necesitás reportes o dashboards? ¿Cuáles? (ej: ventas del mes, stock bajo)",
                "hint": "",
                "priority": "low",
            })

        if not any(w in text_lower for w in ["notificación", "alerta", "email", "aviso"]):
            questions.append({
                "category": "integrations",
                "question": "¿El sistema debe enviar notificaciones o alertas? ¿Por qué canal? (email, SMS, push)",
                "hint": "",
                "priority": "low",
            })

        return questions

    def _calculate_completeness(self, analysis: RequirementsAnalysis) -> float:
        """Calcula qué tan completa está la información."""
        score = 0.0
        max_score = 100.0

        # Entidades (30 puntos)
        entity_count = len(analysis.proposed_entities)
        if entity_count >= 3:
            score += 30
        elif entity_count >= 2:
            score += 20
        elif entity_count >= 1:
            score += 10

        # Reglas de negocio (20 puntos)
        rule_count = len(analysis.detected_rules)
        if rule_count >= 5:
            score += 20
        elif rule_count >= 3:
            score += 15
        elif rule_count >= 1:
            score += 10

        # Actores/Roles (15 puntos)
        if "Actores" in analysis.understood:
            score += 15
        elif any(e["name"] == "User" for e in analysis.proposed_entities):
            score += 8

        # Operaciones claras (20 puntos)
        if "Operaciones" in analysis.understood:
            score += 20
        elif "Tipo de sistema" in analysis.understood:
            score += 10

        # Sin gaps críticos (15 puntos)
        gap_count = len(analysis.gaps)
        if gap_count == 0:
            score += 15
        elif gap_count <= 2:
            score += 8

        return min(score, max_score)
