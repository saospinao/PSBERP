
---

## Resumen de Documentación Clave del Proyecto (Carácter Informativo)

Este apartado ofrece una visión general de los documentos más importantes del repositorio, con el objetivo de socializar las tecnologías, la estructura y las convenciones del nuevo proyecto.

### 📄 [ESTRUCTURA_PROYECTO.md]()
> Este documento describe una estructura de proyecto integral para un microservicio, enfatizando un enfoque de Arquitectura Limpia con .NET 8, PostgreSQL y un frontend Next.js/React/TailwindCSS.
>
> **Componentes Clave y Estructura:**
>
> 1.  **Monorepo (`/microservicio-nombre/`):** Contiene todo lo necesario para un microservicio, incluyendo `backend`, `frontend`, `infra`, `.github` (CI/CD), `docs` y `bmad` (artefactos aislados del método BMAD).
> 2.  **Backend (.NET 8):** Sigue la Arquitectura Limpia con capas distintas: `Api`, `Application`, `Domain`, `Infrastructure`, `CrossCutting` y `tests`.
> 3.  **Frontend (Next.js 14, React, TailwindCSS):** Un microfrontend que consume las APIs del backend.
> 4.  **Infraestructura (`infra/`):** Incluye `terraform` (IaC), `helm` (Kubernetes manifests), `dapr/components` y `docker` (local dev).
> 5.  **CI/CD (`.github/workflows/`):** Acciones de GitHub para automatizar build, test y deploy.
> 6.  **Documentación (`docs/`):** Arquitectura, guías de configuración local, etc.
> 7.  **BMAD (`bmad/`):** Artefactos aislados del método BMAD.
>
> El documento proporciona descripciones detalladas, ejemplos de código y referencias, junto con un checklist de archivos mínimos y ejemplos prácticos para ejecutar localmente.

### 📄 [general-naming-conventions.md]()
> Este documento describe un conjunto integral de convenciones de nomenclatura para un entorno tecnológico full-stack que utiliza C#, PostgreSQL y TypeScript. El principio fundamental es utilizar el estilo de nomenclatura idiomático de cada lenguaje y automatizar el mapeo entre ellos.
>
> **Resumen de Convenciones por Capa:**
>
> *   **C# (Backend):** `PascalCase` para la mayoría de los elementos, `UPPER_SNAKE_CASE` para constantes. Acrónimos en mayúsculas completas dentro de `PascalCase`.
> *   **PostgreSQL (Base de datos):** `snake_case` para esquemas, tablas, columnas, índices y restricciones. Claves primarias `id` e identificadores de negocio `code`.
> *   **TypeScript (Frontend):** `PascalCase` para interfaces/tipos/componentes, `camelCase` para propiedades/funciones/variables, `UPPER_SNAKE_CASE` para constantes.
> *   **API y JSON:** URLs de endpoints en `kebab-case`, parámetros de consulta y claves JSON en `camelCase`.
> *   **Mapeo con EF Core:** Uso de `SnakeCaseNamingConvention` para traducir automáticamente propiedades C# `PascalCase` a columnas PostgreSQL `snake_case`.
> *   **Tablas de Proyección:** Nomenclatura específica con prefijo de 4 letras del servicio de origen y sufijo `_prj` para datos entre microservicios.
>
> El documento también proporciona un checklist de implementación, configuraciones de herramientas (EditorConfig, ESLint) y un historial detallado de cambios.

### 📄 [SIESA-UI-KIT.MD]()
> Este documento describe el "Siesa UI Kit", un conjunto de componentes de interfaz de usuario establecido para el proyecto. Se especifica la instalación (`npm -i siesa-ui-kit`) y las tecnologías clave utilizadas, que incluyen React 19 como framework UI, TypeScript 5 para tipado estático, Tailwind CSS 3.4 para estilos, Storybook 10 para documentación de componentes y Vite 7 como herramienta de construcción.

### 📄 [MANEJODESESSION.md]()
> Este documento detalla el modelo de manejo de sesiones para el ERP, utilizando una combinación de **JSON Web Tokens (JWT)** para *Access Tokens*, *Refresh Tokens* almacenados en **Cookies HttpOnly**, y un **Almacenamiento Centralizado (Redis)** para gestionar la persistencia y revocación instantánea de sesiones. La arquitectura incluye un **flujo de autenticación** (login, validación con middleware en Next.js, refresco de token y logout con revocación en Redis), y mecanismos de **seguridad y auditoría**. Estos últimos abarcan control de acceso basado en roles (**RBAC**), revocación instantánea de tokens a través de Redis, registro de acciones sensibles en `audit_logs`, y medidas de *hardening* adicional (Cookies SameSite=Strict, Rate Limiting, HSTS, verificación de IP/UserAgent). Finalmente, se especifica la **sincronización del estado en el frontend** con Next.js/React utilizando React Query y Zustand/Context.

### 📄 [ESTRUCTURA DE CARPETAS v2.md]()
> Este documento describe una estructura de monorepo detallada, diseñada para organizar microservicios, microfrontends, infraestructura y recursos compartidos. El objetivo principal es mejorar la productividad mediante el versionamiento único, la visibilidad centralizada, la reutilización de plantillas y pipelines uniformes.
>
> La estructura se divide en:
> 1.  **`/platform/`**: Piezas reutilizables y configuraciones de plataforma (plantillas, flujos de trabajo con Google Cloud Workflows, malla de servicios con Anthos Service Mesh, observabilidad con OpenTelemetry, Prometheus y Grafana, documentación para ingenieros de plataforma).
> 2.  **`/services/`**: Agrupa microservicios independientes, cada uno con su backend (.NET Clean Architecture, adaptadores Pub/Sub/Workflows, OpenTelemetry), microfrontend (Next.js + TailwindCSS) e infraestructura específica.
> 3.  **`/frontends/`**: Portales compartidos que integran microfrontends.
> 4.  **`/infra/`**: Infraestructura global del monorepo (Terraform para GCP, Helm charts, manifiestos K8s base, Docker para dev local).
> 5.  **`.github/workflows/`**: Pipelines CI/CD para GitHub Actions.
> 6.  **`docs/`**: Documentación general del proyecto.
> 7.  **`bmad/`**: Artefactos del método BMAD.

### 📄 [Guia Bmad.md]()
---


