Este documento describe una estructura de proyecto integral para un microservicio, enfatizando un enfoque de Arquitectura Limpia con .NET 8, PostgreSQL y un frontend Next.js/React/TailwindCSS.

**Componentes Clave y Estructura:**

1.  **Monorepo (`/microservicio-nombre/`):** Contiene todo lo necesario para un microservicio, incluyendo `backend`, `frontend`, `infra`, `.github` (CI/CD), `docs` y `bmad` (artefactos aislados del método BMAD).
2.  **Backend (.NET 8):** Sigue la Arquitectura Limpia con capas distintas:
    *   `Api`: Maneja solicitudes HTTP, suscripciones Dapr, configuración de DI, middlewares y filtros.
    *   `Application`: Contiene casos de uso, DTOs e interfaces para la lógica de negocio, orquestando llamadas a `Domain` e `Infrastructure`.
    *   `Domain`: El núcleo, independiente de preocupaciones externas, que alberga entidades, objetos de valor, eventos de dominio y reglas de negocio estructurales.
    *   `Infrastructure`: Implementa interfaces definidas en `Application` utilizando tecnologías específicas (EF Core para persistencia, Dapr para mensajería, adaptadores de servicios externos).
    *   `CrossCutting`: Utilidades compartidas como logging, monitoreo y ayudantes de seguridad.
    *   `tests`: Organizado en `UnitTests`, `IntegrationTests`, `SecurityTests` y `PerformanceTests`.
3.  **Frontend (Next.js 14, React, TailwindCSS):** Un microfrontend que consume las APIs del backend, con una clara separación de componentes, librerías y estilos.
4.  **Infraestructura (`infra/`):**
    *   `terraform`: Infraestructura como Código (IaC) para el aprovisionamiento de recursos en la nube (GKE, CloudSQL).
    *   `helm`: Gráficos para manifiestos de Kubernetes con plantillas.
    *   `dapr/components`: Configuraciones de componentes Dapr (pubsub, statestore).
    *   `docker`: Dockerfiles para backend/frontend y `docker-compose.yaml` para desarrollo local.
5.  **CI/CD (`.github/workflows/`):** Acciones de GitHub para automatizar los procesos de construcción, prueba y despliegue tanto para el backend como para el frontend.
6.  **Documentación (`docs/`):** Arquitectura, guías de configuración local, etc.
7.  **BMAD (`bmad/`):** Artefactos aislados del método BMAD para diseño y análisis.

El documento proporciona descripciones detalladas para cada carpeta, archivos clave, ejemplos de código y referencias, junto con una lista de verificación de los archivos mínimos requeridos para una configuración funcional y ejemplos prácticos sobre cómo ejecutar localmente. Enfatiza las convenciones, las buenas prácticas y la gestión de dependencias.