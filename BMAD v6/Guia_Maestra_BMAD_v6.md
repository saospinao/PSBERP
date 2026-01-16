
# 📘 Guía Maestra BMAD v6: Ecosistema Completo

Esta guía cubre la **totalidad** de las capacidades instaladas en tu sistema BMAD, incluyendo flujos de trabajo avanzados, herramientas creativas (CIS), desarrollo rápido (Quick Flow) y arquitectura de pruebas (TestArch).

---

# 1. Instalación y Estructura

```zsh
npx siesa-agents
```

### Estructura de carpetas
BMAD genera un entorno estructurado. Es vital respetar estas carpetas:
- **`.bmad-core/`**: El cerebro del sistema.
- **`.gemini/`**: Comandos y configuraciones para tu agente actual.
- **`.github/`**: Workflows de CI/CD.

---

# 2. Modos de Trabajo

BMAD no es rígido. Elige el modo que se adapte a tu situación actual:

| Modo | Ideal para... | Agentes Clave | Workflows Clave |
| :--- | :--- | :--- | :--- |
| **A. Estándar (BMM)** | Equipos, proyectos grandes, ciclo completo. | PM, Architect, Dev | `create-prd`, `sprint-planning` |
| **B. Rápido (Quick)** | Freelancers, prototipos, "Solo Devs". | Solo-Dev, Quick-Flow | `quick-dev`, `create-tech-spec` |
| **C. Creativo (CIS)** | Ideación, innovación, diseño previo. | Storyteller, Brainstorming Coach | `cis-design-thinking`, `cis-storytelling` |
| **D. Calidad (TestArch)** | Automatización de pruebas, QA robusto. | Test Architect (TEA) | `testarch-automate`, `testarch-ci` |

---

# 3. Catálogo Completo de Agentes

## 🛠️ Gestión y Desarrollo (BMM)
| Agente | Comando | Función |
| :--- | :--- | :--- |
| **Product Owner** | `/po` | Visión y priorización de negocio. |
| **Project Manager** | `/pm` | Gestión de cronograma y PRDs. |
| **Architect** | `/architect` | Estructura técnica y decisiones de stack. |
| **Developer** | `/dev` | Implementación estándar bajo historias. |
| **Scrum Master** | `/sm` | Facilitador y gestión de tareas. |
| **Test Architect** | `/tea` | **(Nuevo)** Estrategia de pruebas y calidad. |
| **Tech Writer** | `/tech-writer` | **(Nuevo)** Documentación técnica profesional. |
| **UX Designer** | `/ux-designer` | **(Nuevo)** Diseño de experiencia e interfaces. |
| **Solo Dev** | `/quick-flow-solo-dev` | **(Nuevo)** Todoterreno para desarrollo rápido. |

## 🎨 Creatividad e Innovación (CIS) - **NUEVO**
| Agente | Comando | Descripción |
| :--- | :--- | :--- |
| **Brainstorming Coach** | `/brainstorming-coach` | Facilita sesiones de lluvia de ideas. |
| **Storyteller** | `/storyteller` | Crea narrativas y mensajes impactantes. |
| **Innovation Strategist**| `/innovation-strategist`| Detecta oportunidades disruptivas de negocio. |
| **Creative Solver** | `/creative-problem-solver`| Resuelve problemas bloqueantes con metodología TRIZ/Lateral. |
| **Presentation Master** | `/presentation-master` | Diseña presentaciones visuales efectivas. |
| **Design Thinking Coach**| `/design-thinking-coach`| Guía procesos de empatía y diseño centrado en usuario. |

## 🏗️ Constructores (BMB)
| Agente | Comando | Descripción |
| :--- | :--- | :--- |
| **Agent Builder** | `/agent-builder` | Crea nuevos agentes personalizados. |
| **Workflow Builder** | `/workflow-builder` | Diseña nuevos flujos de trabajo. |

---

# 4. Flujos de Trabajo (Comandos Detallados)

## 🏎️ Modo Rápido (Quick Flow)
*Para cuando necesitas código YA, sin pasar por toda la burocracia.*

| Comando | Descripción |
| :--- | :--- |
| `quick-dev` | **El comando estrella.** Ejecuta tareas de desarrollo directamente. Puede recibir instrucciones directas o especificaciones técnicas. |
| `create-tech-spec` | Crea una especificación técnica rápida mediante conversación, lista para ser consumida por `quick-dev`. |

## 🧩 Modo Estándar (Ciclo BMM)
*El flujo completo para asegurar calidad y mantenibilidad.*

**Fase 1: Descubrimiento**
- `workflow-init`: Inicializa el proyecto.
- `create-product-brief`: Resumen ejecutivo.
- `bmm-research`: Investigación de mercado/técnica.

**Fase 2: Planeación**
- `create-prd`: Documento maestro de requerimientos.
- `create-ux-design`: Diseño de interfaces (requiere UX Designer).

**Fase 3: Solución**
- `create-architecture`: Definición técnica del sistema.
- `create-epics-and-stories`: Desglose masivo de historias.
- `check-implementation-readiness`: **(Crítico)** Valida que TODO esté listo antes de codificar. *Nota: Antes llamado implementation-readiness.*
- `generate-project-context`: Crea el archivo de contexto vital para la IA.

**Fase 4: Implementación**
- `sprint-planning`: Organiza el trabajo del sprint.
- `create-story`: Detalla una historia específica.
- `dev-story`: Codifica la historia.
- `code-review`: Revisión adversarial de código.
- `sprint-status`: Reporte de estado.

## 💡 Modo Creativo (CIS Workflows)
*Para desbloquear ideas y definir el "qué" antes del "cómo".*

| Comando | Descripción |
| :--- | :--- |
| `cis-design-thinking` | Proceso completo: Empatizar -> Definir -> Idear -> Prototipar. |
| `cis-innovation-strategy`| Análisis estratégico de modelos de negocio. |
| `cis-problem-solving` | Metodología estructurada para resolver problemas complejos. |
| `cis-storytelling` | Creación de narrativas para pitch, marketing o visión. |
| `core-brainstorming` | Sesión guiada de generación de ideas. |

## 🛡️ Arquitectura de Pruebas (TestArch)
*Asegura que tu software no se rompa.*

| Comando | Descripción |
| :--- | :--- |
| `testarch-framework` | Inicializa el framework de pruebas (ej. Playwright/Cypress). |
| `testarch-atdd` | Genera pruebas de aceptación que fallan (TDD) antes de codificar. |
| `testarch-automate` | Automatiza pruebas sobre código existente. |
| `testarch-ci` | Crea pipelines de Integración Continua (CI/CD). |
| `testarch-nfr` | Evalúa requisitos no funcionales (rendimiento, seguridad). |

## ✏️ Herramientas Visuales (Excalidraw)
| Comando | Descripción |
| :--- | :--- |
| `create-excalidraw-diagram` | Crea diagramas generales de arquitectura/técnicos. |
| `create-excalidraw-flowchart`| Crea diagramas de flujo lógicos. |
| `create-excalidraw-wireframe`| Crea bocetos de interfaz (wireframes). |
| `create-excalidraw-dataflow` | Crea diagramas de flujo de datos (DFD). |

---

# 5. Consejos de Oro

1.  **¿Solo en el proyecto?** Usa el agente `/quick-flow-solo-dev` y el comando `quick-dev`. Ahorrarás horas.
2.  **¿Bloqueado creativamente?** Llama a `/brainstorming-coach` antes de intentar escribir un PRD.
3.  **¿Código frágil?** Ejecuta `testarch-atdd` antes de `dev-story` para garantizar que cumples los requisitos.
4.  **Nombres de Comandos:** Si un comando falla, intenta anteponer su prefijo de módulo (ej. `bmm-`, `cis-`, `core-`) tal como aparece en la carpeta `.gemini/commands`.
