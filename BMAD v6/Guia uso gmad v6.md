
---
# *Instalación*

```zsh
npx siesa-agents
```

El paquete instala las siguientes carpetas en tu directorio actual:

- **`.bmad-core/`** - Archivos principales del sistema BMAD
- **`.vscode/`** - Configuración de Visual Studio Code
- **`.github/`** - Configuración de GitHub Actions y workflows
- **`.claude/`** - Configuración de Claude Code Commands y workflows
- **`.gemini/`** - Configuración de Gemini Commands y workflows

### Estructura de carpetas recomendada.

Al crear las carpetas, se debe crear una carpeta apps, también se deben contextualizar a la IA sobre esa carpeta.

![[Pasted image 20260102094852.png]]

>*Nota:* También se debe contextualizar a la IA sobre los archivos package-lock.json y package.json que debe tener en cuenta son los ubicados dentro de la carpeta apps donde tengas un projecto que los requiera, esto para evitar que instale dependencias en la raiz donde bmad genera sus archivos.

---
## 🤖 Lista de agentes

| Agentes              | Descripcion                                                                                                                                                                                                               |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `/po`                | **(Product Owner):** Se encarga de la **visión del producto**. Define el "qué" y el "por qué", prioriza las funcionalidades basándose en el valor de negocio y asegura que el equipo trabaje en los requisitos correctos. |
| `/pm`                | **(Project Manager):** Enfocado en la **gestión de tiempos y recursos**. Organiza las tareas, gestiona los bloqueos del equipo y asegura que el proyecto avance según el cronograma previsto.                             |
| `/analyst`           | Especialista en **análisis de requerimientos**. Traduce las ideas del PO en especificaciones técnicas detalladas y casos de uso, asegurando que no haya ambigüedades antes de empezar a programar                         |
| `/architect`         | Diseña la **estructura técnica**. Define la jerarquía de archivos, la selección de librerías, la estructura de la base de datos y cómo se comunicarán los diferentes módulos.                                             |
| `/bmad-orchestrator` | Actúa como el **director de flujo**. Coordina la comunicación entre los otros agentes, decidiendo qué agente debe intervenir en cada momento para resolver una tarea compleja.                                            |
| `/bmad-master`       | Es el **agente supervisor** o punto de entrada principal. Mantiene el contexto global del proyecto y asegura que todos los agentes sigan los estándares generales del ecosistema BMad.                                    |
| `/dev`               | Un agente de **desarrollo generalista**. Capaz de realizar tareas transversales de programación y scripting.                                                                                                              |
| `/frontend`          | Especialista en la **interfaz de usuario**. Se encarga de la lógica del cliente, componentes visuales, estados de UI y la experiencia de usuario (UX).                                                                    |
| `/backend`           | Especialista en la **lógica de servidor**. Se encarga de la API, las integraciones con bases de datos, la seguridad y el procesamiento de datos del lado del servidor.                                                    |

## 📘 Glosario de Comandos Bmad (Nuevas Fases)

| Comando                      | Significado                                                                 | Fase                  |
| ---------------------------- | --------------------------------------------------------------------------- | --------------------- |
| `workflow-init`              | Inicializa el flujo de trabajo del proyecto.                                | Descubrimiento        |
| `create-product-brief`       | Genera el brief inicial del producto.                                       | Descubrimiento        |
| `create-prd`                 | Crea el Documento de Requerimientos del Producto (PRD).                     | Planeación            |
| `create-ux-design`           | (Opcional) Genera el diseño de experiencia de usuario.                      | Planeación            |
| `create-architecture`        | Define la arquitectura técnica del sistema.                                 | Solución              |
| `generate-project-context`   | Genera el contexto necesario para el desarrollo del proyecto.               | Solución              |
| `create-epics-and-stories`   | Desglosa el proyecto en épicas e historias de usuario.                      | Solución              |
| `implementation-readiness`   | Verifica que todo esté listo para comenzar la implementación.               | Solución              |
| `sprint-planning`            | Planifica el sprint con las historias seleccionadas.                        | Implementación        |
| `create-story`               | Detalla una historia de usuario específica.                                 | Implementación        |
| `dev-story`                  | Ejecuta el desarrollo de una historia de usuario.                           | Implementación        |
| `code-review`                | Realiza la revisión de código (incluye `validate-story`).                   | Implementación        |
| `sprint-status`              | Revisa el estado del sprint (al final de la épica).                         | Implementación        |

---

## 🏗️ Fase 1: Descubrimiento (Opcional)

En esta etapa inicial se define el alcance y objetivos generales.

*   `workflow-init`: Configuración inicial del flujo de trabajo y selección de herramientas.
*   `create-product-brief`: Creación del resumen ejecutivo del producto para alinear la visión del equipo.

## 🧩 Fase 2: Planeación

Se detallan los requerimientos y el diseño del producto para asegurar una base sólida.

*   `create-prd`: El PM genera el Documento de Requerimientos del Producto (PRD) detallado.
*   `create-ux-design`: (Opcional) Definición de la experiencia de usuario, flujos e interfaces visuales.

## 🛠️ Fase 3: Solución

Transformación de requerimientos en una solución técnica y estructurada.

*   `create-architecture`: El Arquitecto define el stack tecnológico, base de datos y estructura del sistema.
*   `generate-project-context`: Preparación del contexto global para que los agentes y desarrolladores entiendan el proyecto.
*   `create-epics-and-stories`: Desglose del trabajo en unidades manejables (Épicas e Historias de Usuario).
*   `implementation-readiness`: Validación final de que todos los artefactos necesarios están listos antes de codificar.

## 💻 Fase 4: Implementación

Ciclo de desarrollo iterativo donde se construye el software.

*   `sprint-planning`: Selección y organización de las historias a realizar en el sprint actual.
*   `create-story`: Definición detallada y técnica de cada historia individual antes de su desarrollo.
*   `dev-story`: Ejecución del desarrollo y codificación de la historia por parte de los Devs.
*   `code-review`: Revisión de calidad, pruebas y validación de la historia (incluye el paso `validate-story`).
*   `sprint-status`: Revisión del progreso y estado general al finalizar las tareas de una épica.

---

## 🤝 Trabajo en Equipo: Contextualización BMAD

BMAD asegura la coherencia mediante flujos de trabajo estructurados. A diferencia del caos habitual, aquí cada agente (PO, PM, Arquitecto, Dev) interviene en el momento preciso con el contexto adecuado.

1.  **Definición Clara:** No se escribe código hasta que la fase de **Solución** (Arquitectura, Historias) esté sólida.
2.  **Desglose Estructurado:** `create-epics-and-stories` asegura que el trabajo esté dividido en piezas independientes pero coherentes.
3.  **Contexto Preservado:** Comandos como `generate-project-context` y `dev-story` aseguran que el desarrollador (o agente) tenga toda la información necesaria sin ruido externo.
