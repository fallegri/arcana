"""
Stakeholder Detector — Identifica quiénes deben participar en la elicitación.

Según el tipo de sistema, determina:
- Qué áreas/roles deben ser consultados
- Qué información específica necesita de cada uno
- En qué orden consultar (dependencias)
- Quién es decisor vs informador vs validador
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional


@dataclass
class Stakeholder:
    """Un stakeholder identificado."""
    id: str
    role: str               # "gerente_finanzas", "jefe_rrhh", etc.
    area: str               # "Finanzas", "RRHH", "TI", etc.
    name: Optional[str] = None  # Se completa cuando el usuario da nombres
    email: Optional[str] = None
    type: str = "informador"    # "decisor", "informador", "validador", "usuario_final"
    priority: str = "alta"      # "alta", "media", "baja"
    description: str = ""
    topics: List[str] = field(default_factory=list)  # Temas a consultar


# Mapa de stakeholders por tipo de sistema
STAKEHOLDER_MAPS = {
    "erp": {
        "description": "Sistema ERP — Requiere input de todas las áreas operativas",
        "stakeholders": [
            Stakeholder(id="SH-01", role="Gerente General", area="Dirección", type="decisor", priority="alta",
                        description="Define alcance, presupuesto y prioridades",
                        topics=["Alcance del proyecto", "Presupuesto disponible", "Prioridades de negocio", "Plazos"]),
            Stakeholder(id="SH-02", role="Director de Finanzas/CFO", area="Finanzas", type="decisor", priority="alta",
                        description="Define procesos financieros, reportes y compliance",
                        topics=["Plan de cuentas", "Proceso de cierre", "Reportes regulatorios", "Multi-moneda", "Centros de costo"]),
            Stakeholder(id="SH-03", role="Jefe de RRHH", area="Recursos Humanos", type="informador", priority="alta",
                        description="Define procesos de personal, nómina, asistencia",
                        topics=["Estructura organizacional", "Tipos de contrato", "Proceso de nómina", "Licencias/vacaciones", "Evaluación de desempeño"]),
            Stakeholder(id="SH-04", role="Jefe de Ventas/Comercial", area="Ventas", type="informador", priority="alta",
                        description="Define procesos de venta, comisiones, clientes",
                        topics=["Proceso de venta", "Tipos de cliente", "Comisiones", "Metas", "Territorios"]),
            Stakeholder(id="SH-05", role="Jefe de Compras", area="Compras", type="informador", priority="alta",
                        description="Define procesos de adquisición, proveedores",
                        topics=["Proceso de compra", "Aprobaciones", "Evaluación proveedores", "Contratos"]),
            Stakeholder(id="SH-06", role="Jefe de Logística/Almacén", area="Logística", type="informador", priority="alta",
                        description="Define procesos de inventario, despacho",
                        topics=["Proceso de recepción", "Despacho", "Inventario físico", "Ubicaciones", "Lotes/series"]),
            Stakeholder(id="SH-07", role="Director de TI/CTO", area="Tecnología", type="validador", priority="alta",
                        description="Define infraestructura, integraciones, seguridad",
                        topics=["Infraestructura actual", "Integraciones necesarias", "Seguridad", "Backup", "Capacitación"]),
            Stakeholder(id="SH-08", role="Contador/Auditor", area="Auditoría", type="validador", priority="media",
                        description="Valida cumplimiento normativo y trazabilidad",
                        topics=["Requisitos de auditoría", "Retención de datos", "Trazabilidad", "Normativa fiscal"]),
        ],
    },
    "sgsi": {
        "description": "Sistema de Gestión de Seguridad de la Información — ISO 27001",
        "stakeholders": [
            Stakeholder(id="SH-01", role="Director General/CEO", area="Dirección", type="decisor", priority="alta",
                        description="Compromiso de la dirección (requisito ISO 27001)",
                        topics=["Compromiso con SGSI", "Presupuesto", "Alcance organizacional"]),
            Stakeholder(id="SH-02", role="CISO / Responsable de Seguridad", area="Seguridad", type="decisor", priority="alta",
                        description="Define políticas, controles y gestión de riesgos",
                        topics=["Políticas actuales", "Activos de información", "Análisis de riesgos", "Controles existentes", "Incidentes previos"]),
            Stakeholder(id="SH-03", role="Director de TI", area="Tecnología", type="informador", priority="alta",
                        description="Infraestructura, redes, sistemas actuales",
                        topics=["Inventario de sistemas", "Arquitectura de red", "Backup/DR", "Parches", "Accesos"]),
            Stakeholder(id="SH-04", role="Responsable de Mesa de Ayuda", area="Soporte", type="informador", priority="media",
                        description="Incidentes, problemas reportados, usuarios",
                        topics=["Tipos de incidentes", "SLAs actuales", "Herramientas", "Escalamiento"]),
            Stakeholder(id="SH-05", role="Asesor Legal", area="Legal", type="validador", priority="alta",
                        description="Normativa de protección de datos, contratos",
                        topics=["Normativa de datos personales", "Contratos con terceros", "SLAs legales", "Jurisdicción"]),
            Stakeholder(id="SH-06", role="Responsable de RRHH", area="RRHH", type="informador", priority="media",
                        description="Concientización, roles, accesos de personal",
                        topics=["Proceso de alta/baja", "Capacitación en seguridad", "Acuerdos de confidencialidad"]),
            Stakeholder(id="SH-07", role="Auditor Interno", area="Auditoría", type="validador", priority="media",
                        description="Auditorías previas, hallazgos, planes de acción",
                        topics=["Auditorías realizadas", "No conformidades abiertas", "Plan de tratamiento"]),
            Stakeholder(id="SH-08", role="Jefes de Área (Operaciones)", area="Operaciones", type="informador", priority="media",
                        description="Procesos operativos que manejan información sensible",
                        topics=["Información que manejan", "Procesos críticos", "Dependencia de TI"]),
        ],
    },
    "ecommerce": {
        "description": "Plataforma de Comercio Electrónico",
        "stakeholders": [
            Stakeholder(id="SH-01", role="Gerente/Dueño", area="Dirección", type="decisor", priority="alta",
                        description="Visión del negocio, catálogo, posicionamiento",
                        topics=["Catálogo de productos", "Mercado objetivo", "Diferenciación", "Presupuesto"]),
            Stakeholder(id="SH-02", role="Marketing", area="Marketing", type="informador", priority="alta",
                        description="SEO, campañas, landing pages, analytics",
                        topics=["SEO requerido", "Integraciones de analytics", "Email marketing", "Redes sociales"]),
            Stakeholder(id="SH-03", role="Operaciones/Logística", area="Logística", type="informador", priority="alta",
                        description="Envíos, stock, devoluciones",
                        topics=["Zonas de envío", "Transportistas", "Tiempos de entrega", "Política de devoluciones"]),
            Stakeholder(id="SH-04", role="Atención al Cliente", area="Soporte", type="informador", priority="media",
                        description="Canales de atención, FAQ, quejas frecuentes",
                        topics=["Canales actuales", "Preguntas frecuentes", "Proceso de reclamos"]),
            Stakeholder(id="SH-05", role="Finanzas", area="Finanzas", type="validador", priority="alta",
                        description="Pasarela de pago, facturación, impuestos",
                        topics=["Medios de pago", "Facturación electrónica", "Impuestos por zona", "Conciliación"]),
        ],
    },
    "sistema_medico": {
        "description": "Sistema de Gestión de Salud / Historia Clínica",
        "stakeholders": [
            Stakeholder(id="SH-01", role="Director Médico", area="Dirección", type="decisor", priority="alta",
                        description="Define protocolos médicos y flujos clínicos",
                        topics=["Protocolos", "Especialidades", "Flujo de pacientes"]),
            Stakeholder(id="SH-02", role="Médicos (por especialidad)", area="Médica", type="informador", priority="alta",
                        description="Uso diario del sistema, prescripciones, diagnósticos",
                        topics=["Datos de consulta", "Prescripciones", "Interconsultas", "Órdenes médicas"]),
            Stakeholder(id="SH-03", role="Enfermería", area="Enfermería", type="informador", priority="alta",
                        description="Signos vitales, medicación, evolución",
                        topics=["Registro de signos", "Administración de medicamentos", "Evolución del paciente"]),
            Stakeholder(id="SH-04", role="Administración", area="Administrativa", type="informador", priority="media",
                        description="Turnos, facturación, obras sociales",
                        topics=["Agenda de turnos", "Facturación", "Autorizaciones", "Obras sociales/seguros"]),
            Stakeholder(id="SH-05", role="Responsable de Datos/Privacidad", area="Legal", type="validador", priority="alta",
                        description="HIPAA/ley de datos de salud, consentimiento",
                        topics=["Normativa de datos de salud", "Consentimiento informado", "Retención", "Accesos"]),
        ],
    },
    "sistema_educativo": {
        "description": "Sistema de Gestión Educativa / LMS",
        "stakeholders": [
            Stakeholder(id="SH-01", role="Director/Rector", area="Dirección", type="decisor", priority="alta",
                        description="Políticas académicas, presupuesto",
                        topics=["Normativa académica", "Presupuesto", "Integración con otros sistemas"]),
            Stakeholder(id="SH-02", role="Coordinador Académico", area="Académica", type="informador", priority="alta",
                        description="Plan de estudios, evaluaciones, promoción",
                        topics=["Malla curricular", "Sistema de calificación", "Requisitos de promoción", "Asistencia"]),
            Stakeholder(id="SH-03", role="Docentes (muestra)", area="Docente", type="informador", priority="alta",
                        description="Carga de notas, asistencia, materiales",
                        topics=["Proceso de evaluación", "Tipos de actividad", "Rúbricas", "Comunicación con padres"]),
            Stakeholder(id="SH-04", role="Secretaría/Administración", area="Administrativa", type="informador", priority="media",
                        description="Matrícula, certificados, trámites",
                        topics=["Proceso de matrícula", "Documentos que emite", "Trámites frecuentes"]),
            Stakeholder(id="SH-05", role="Padres/Tutores (muestra)", area="Comunidad", type="usuario_final", priority="media",
                        description="Qué información necesitan ver",
                        topics=["Notas del hijo", "Asistencia", "Comunicados", "Pagos"]),
        ],
    },
}


class StakeholderDetector:
    """Detecta stakeholders necesarios según el tipo de proyecto."""

    def detect(self, project_description: str) -> Dict:
        """
        Analiza la descripción y retorna stakeholders necesarios.

        Returns:
            Dict con tipo_sistema, stakeholders, y recomendaciones
        """
        text_lower = project_description.lower()

        # Detectar tipo de sistema
        system_type = self._detect_system_type(text_lower)

        if system_type and system_type in STAKEHOLDER_MAPS:
            data = STAKEHOLDER_MAPS[system_type]
            stakeholders = data["stakeholders"]
            description = data["description"]
        else:
            # Genérico
            stakeholders = [
                Stakeholder(id="SH-01", role="Sponsor/Dueño del proyecto", area="Dirección", type="decisor",
                            priority="alta", topics=["Alcance", "Presupuesto", "Plazos"]),
                Stakeholder(id="SH-02", role="Usuarios principales", area="Operaciones", type="informador",
                            priority="alta", topics=["Procesos actuales", "Problemas", "Expectativas"]),
                Stakeholder(id="SH-03", role="TI / Responsable técnico", area="Tecnología", type="validador",
                            priority="media", topics=["Infraestructura", "Integraciones", "Seguridad"]),
            ]
            description = "Sistema genérico"
            system_type = "generic"

        return {
            "system_type": system_type,
            "description": description,
            "stakeholders": [
                {
                    "id": s.id,
                    "role": s.role,
                    "area": s.area,
                    "type": s.type,
                    "priority": s.priority,
                    "description": s.description,
                    "topics": s.topics,
                }
                for s in stakeholders
            ],
            "total_stakeholders": len(stakeholders),
            "recommendation": self._generate_recommendation(system_type, stakeholders),
        }

    def _detect_system_type(self, text: str) -> Optional[str]:
        """Detecta el tipo de sistema."""
        type_triggers = {
            "erp": ["erp", "enterprise resource", "planificación de recursos", "módulos de empresa"],
            "sgsi": ["sgsi", "iso 27001", "seguridad de la información", "gestión de seguridad"],
            "ecommerce": ["e-commerce", "ecommerce", "tienda online", "tienda virtual", "marketplace"],
            "sistema_medico": ["hospital", "clínica", "historia clínica", "paciente", "médico"],
            "sistema_educativo": ["escuela", "universidad", "educativo", "lms", "academia", "colegio"],
        }

        for sys_type, triggers in type_triggers.items():
            if any(t in text for t in triggers):
                return sys_type
        return None

    def _generate_recommendation(self, system_type: str, stakeholders: list) -> str:
        """Genera recomendación de cómo proceder."""
        high_priority = [s for s in stakeholders if s.priority == "alta"]
        return (
            f"Se identificaron {len(stakeholders)} stakeholders. "
            f"Prioridad ALTA: {len(high_priority)} personas a consultar primero. "
            f"Recomendación: empezar por los decisores, luego informadores, finalmente validadores."
        )
