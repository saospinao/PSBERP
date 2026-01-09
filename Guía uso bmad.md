
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

## 📘 Glosario de Comandos Bmad

| Comando         | Significado                                                             | ¿Quién lo usa? |
| --------------- | ----------------------------------------------------------------------- | -------------- |
| `*CREATE-PRD`   | Crea el documento de requerimientos (la biblia del producto).           | PM             |
| `*SHARD-DOC`    | **Fragmentar**. Divide un documento largo en piezas pequeñas (stories). | PO             |
| `*DRAFT`        | Crea el esqueleto inicial de las tareas de desarrollo.                  | SM             |
| `*RISK-PROFILE` | Analiza qué puede fallar en una historia específica.                    | QA             |
| `*TEST-DESIGN`  | Define cómo se probará la tarea antes de programarla.                   | QA             |
| `*DEVELOP`      | Ejecución de código basada en el contexto de la tarea.                  | DEV            |
| `*REVIEW`       | Validación final de que el desarrollo cumple con el diseño.             | QA             |
 >*Nota:*  Los comandos con asterisco (`*`) suelen ser disparadores de automatizaciones o plantillas en bmad.

---

## 🏗️ Fase 1: Definición y Diseño (Discovery)

En esta etapa se sientan las bases del proyecto. El objetivo es transformar una necesidad de negocio en una estructura técnica sólida.

| Rol            | Acción / Comando                  | Descripción                                                                                                        |
| -------------- | --------------------------------- | --------------------------------------------------------------------------------------------                       |
| **Analista**   | `BRIEF`                           | El punto de partida. Se definen los objetivos generales y el alcance del proyecto definiendo "qué" y el "por qué". |
| **PM**         | `*CREATE-PRD`                     | Genera el Documento de Requerimientos del Producto (PRD) detallando el "como" y el Stack Tecnológico.              |
| **Arquitecto** | `*CREATE-FULL-STACK-ARCHITECTURE` | Define la estructura técnica, stack, bases de datos y flujo de datos.                                              |

>Nota: El brief no tiene ninguna información técnica, al momento de crear el prd es donde se contextualiza para que después el arquitecto continúe con la definición.

---

## 🧩 Fase 2: Fragmentación y Refinamiento

Una vez aprobados el PRD y la Arquitectura, el **Product Owner (PO)** debe "romper" la información en piezas accionables.

1. **Validación de Calidad:**
* **PO:** `*EXECUTE CHECKLIST PO` (Asegura que la definición previa cumple con los estándares mínimos).


2. **Fragmentación (Sharding):**
* **PO:** `*SHARD-DOC DOCS/PRD.MD, DOCS/PRD`
* **PO:** `*SHARD-DOC DOCS/ARCHITECTURE.MD, DOCS/ARCHITECTURE`


> **Nota:** Este paso es vital para que las historias de usuario (stories) sean pequeñas, manejables y específicas.



---

## 💻 Fase 3: Ciclo de Desarrollo (Delivery)

Aquí es donde el equipo ejecuta sobre cada **#STORY** individual.

### A. Preparación y Validación

* **SM (Scrum Master):** `*DRAFT` -> Crea el borrador de las tareas/historias.
* **QA:** `*RISK-PROFILE #STORY` -> Identifica posibles puntos ciegos o riesgos técnicos.
* **QA:** `*TEST-DESIGN #STORY` -> Crea el plan de pruebas antes de que se escriba una sola línea de código.
* **PO:** `*VALIDATE-STORY-DRAFT #STORY` -> El PO da el visto bueno final al diseño de la tarea.
* **Manual:** Editar el estado de la historia a **APROBADO**.

### B. Ejecución y Cierre

* **DEV:** `*DEVELOP #STORY` -> El desarrollador ejecuta la lógica basada en el PRD y la Arquitectura fragmentada.
* **QA:** `*REVIEW #STORY` -> Revisión de calidad para asegurar que lo desarrollado cumple con el diseño de pruebas previo.
* **Manual:** Editar el estado de la historia a **DONE**.

---

## 🤝 Trabajo en Equipo: ¿Cómo evita BMAD el caos?

Cuando muchas personas generan código al mismo tiempo, **BMAD Core** garantiza el orden mediante la **Contextualización**. En lugar de que todos toquen todo, el sistema aplica tres filtros:

### 1. El Contrato de Arquitectura (`*CREATE-ARCHITECTURE`)

Antes de programar, se crea un "molde" único. Aunque 10 personas trabajen a la vez, todas deben respetar las interfaces y estructuras definidas aquí. Esto asegura que, al final, las piezas encajen perfectamente.

### 2. Aislamiento por Fragmentación (`*SHARD-DOC`)

Esta es la parte clave del **Core**. El PO y el Arquitecto dividen el proyecto en fragmentos pequeños (Historias).

* **Resultado:** Cada desarrollador recibe solo la información y los archivos que necesita.
* **Beneficio:** Se minimizan los "choques" o conflictos de código (merge conflicts) porque el sistema intenta que cada historia trabaje en áreas separadas.

### 3. Sincronización mediante el Contexto (`*DEVELOP`)

Al ejecutar el comando de desarrollo sobre una `#STORY` específica:

* El desarrollador trabaja en un "entorno protegido" con el contexto exacto de esa tarea.
* El sistema mantiene la coherencia entre lo que hace el **Dev A** y el **Dev B** basándose en los fragmentos asignados.

> **En resumen:** BMAD Core no gestiona personas, gestiona **contextos**. Si el proyecto está bien fragmentado (`SHARDING`), 20 personas pueden codear simultáneamente sin pisarse, porque cada una es dueña de un fragmento lógico distinto.
