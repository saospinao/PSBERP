## Estructura monorepo

```
/monorepo/
│
├── platform/                            # Plantillas, políticas y recursos compartidos
│   ├── templates/                       # Templates de proyectos (backend, frontend)
│   ├── workflows/                       # Workflows YAML reutilizables (Cloud Workflows)
│   │   └── order-created-workflow.yaml
│   ├── service-mesh/                    # Reglas e infra de Anthos Service Mesh
│   │   ├── namespace-labels.yaml
│   │   ├── peer-authentication.yaml
│   │   ├── destination-rule.yaml
│   │   ├── virtual-service.yaml
│   │   └── authorization-policy.yaml
│   ├── observability/                   # OpenTelemetry, Prometheus rules, dashboards
│   └── docs/                            # How-to para platform engineers
│
├── services/
│   ├── ventas/                          # ejemplo de microservicio "ventas"
│   │   ├── backend/
│   │   │   ├── Microservicio.sln
│   │   │   ├── src/
│   │   │   │   ├── Microservicio.Api/
│   │   │   │   │   ├── Controllers/
│   │   │   │   │   ├── Endpoints/
│   │   │   │   │   ├── Middlewares/
│   │   │   │   │   ├── Filters/
│   │   │   │   │   ├── DI/
│   │   │   │   │   ├── Program.cs
│   │   │   │   │   └── appsettings*.json
│   │   │   │   ├── Microservicio.Application/
│   │   │   │   ├── Microservicio.Domain/
│   │   │   │   ├── Microservicio.Infrastructure/
│   │   │   │   │   ├── Persistence/
│   │   │   │   │   │   ├── EF/
│   │   │   │   │   │   │   ├── DbContexts/AppDbContext.cs
│   │   │   │   │   │   │   ├── Configurations/ (IEntityTypeConfiguration)
│   │   │   │   │   │   │   └── Migrations/
│   │   │   │   │   │   ├── Repositories/
│   │   │   │   │   │   └── UnitOfWork/
│   │   │   │   │   ├── Messaging/                # reemplaza Dapr
│   │   │   │   │   │   ├── PubSub/               # Pub/Sub publisher/subscriber adapters
│   │   │   │   │   │   │   ├── PubSubPublisher.cs
│   │   │   │   │   │   │   └── PubSubSubscriber.cs
│   │   │   │   │   │   └── WorkflowsClient/      # Workflows invoker
│   │   │   │   │   │       └── WorkflowsService.cs
│   │   │   │   │   ├── Observability/            # OpenTelemetry traces & metrics
│   │   │   │   │   └── Security/                 # mTLS, IAM helpers
│   │   │   │   └── Microservicio.Infrastructure.csproj
│   │   │   └── tests/
│   │   ├── frontend/                             # microfrontend de ventas (Next.js + Tailwind)
│   │   │   ├── package.json
│   │   │   ├── next.config.mjs
│   │   │   ├── tailwind.config.js
│   │   │   ├── src/
│   │   │   └── Dockerfile
│   │   └── infra/                                # despliegue específico del servicio
│   │       ├── helm/
│   │       │   └── Chart.yaml
│   │       │   └── templates/
│   │       │        ├── deployment.yaml
│   │       │        ├── service.yaml
│   │       │        ├── hpa.yaml
│   │       │        └── configmap.yaml
│   │       ├── k8s/
│   │       │   ├── kustomization.yaml
│   │       │   └── postgres-secret.yaml
│   │       └── terraform/                        # optional per-service IaC
│   │
│   └── inventario/  (otro microservicio, idéntica estructura)
│
├── frontends/                                    # portales compartidos / host apps
│   ├── portal-admin/
│   └── pos-web/
│
├── infra/                                         # platform-level infra
│   ├── terraform/
│   │   ├── modules/
│   │   │   ├── gke/
│   │   │   ├── cloudsql-postgres/
│   │   │   ├── pubsub/
│   │   │   ├── service-mesh/                      # habilita ASM
│   │   │   └── workflows/
│   │   ├── envs/
│   │   │   ├── dev/
│   │   │   ├── qa/
│   │   │   └── prod/
│   │   └── main.tf
│   ├── helm/                                      # umbrella charts, shared values
│   ├── k8s/                                       # base manifests (namespaces, secrets)
│   │   ├── namespaces.yaml
│   │   ├── mesh/                                  # platform mesh resources
│   │   │   ├── peer-authentication.yaml
│   │   │   ├── destination-rule.yaml
│   │   │   ├── virtual-service.yaml
│   │   │   └── authorization-policy.yaml
│   │   └── secrets/                               # base secrets templates for k8s (sealed secrets)
│   └── docker/                                    # local dev
│       ├── backend.Dockerfile
│       ├── frontend.Dockerfile
│       └── docker-compose.yaml
│
├── .github/
│   └── workflows/
│       ├── platform-ci.yml
│       ├── service-ci.yml
│       └── deploy-to-gke.yml
│
├── docs/
│   ├── architecture/
│   ├── run-local.md
│   └── asm-and-workflows.md
│
└── bmad/
    └── (BMAD artifacts: ubiquitous language, events, commands, scenarios)
```

---

# 📁 **/monorepo/**

### **Descripción general**

Es el repositorio raíz que organiza todos los microservicios, microfrontends, infraestructura, documentación y recursos compartidos. Este tipo de repositorio se conoce como **monorepo** (single repository for multiple projects).
Referencia:
[https://monorepo.tools/](https://monorepo.tools/)

### **Objetivo**

Centralizar:

* código backend
* código frontend
* infraestructura
* CI/CD
* políticas compartidas
* Workflows
* Service Mesh
* BMAD artifacts

Este enfoque mejora la productividad gracias a:

* versionamiento único
* visibilidad central
* reuso de plantillas
* pipelines uniformes

---

# 📁 **platform/**

### **¿Qué es?**

Contiene **todas las piezas reutilizables** por todos los equipos y servicios, como:

* Plantillas de proyectos
* Workflows reutilizables
* Configuraciones de malla de servicios
* Observabilidad
* Documentación para DevOps / Platform Engineers

Este directorio define **la plataforma**, no las aplicaciones.

---

## 📁 **platform/templates/**

### **Propósito**

Plantillas de código base usadas para generar automáticamente nuevos microservicios o microfrontends.

Ejemplo: plantilla backend con `.NET`, limpia, hexagonal con Application/Domain/Infrastructure.

### **Ejemplo**

```
templates/
  ├── dotnet-backend/
  │   ├── template.json
  │   └── src/...
  └── nextjs-frontend/
      ├── template.json
      └── src/...
```

### **Más información**

Templates en .NET:
[https://learn.microsoft.com/en-us/dotnet/core/tools/custom-templates](https://learn.microsoft.com/en-us/dotnet/core/tools/custom-templates)

---

## 📁 **platform/workflows/**

### **Propósito**

Workflows **YAML** reutilizables para orquestación con **Google Cloud Workflows**.

Los Workflows permiten ejecutar procesos multi-servicio mediante pasos secuenciales, paralelos, retries, etc.

Referencia oficial:
[https://cloud.google.com/workflows](https://cloud.google.com/workflows)

### **Ejemplo: `order-created-workflow.yaml`**

```yaml
main:
  params: [event]
  steps:
    - logEvent:
        call: http.post
        args:
          url: https://logging.service/process
          body:
            event: ${event}
    - notifyBilling:
        call: http.post
        args:
          url: https://billing.service/bill
          body:
            orderId: ${event.orderId}
    - returnSuccess:
        return: "OK"
```

---

## 📁 **platform/service-mesh/**

### **Propósito**

Archivos de configuración para **Anthos Service Mesh (ASM)** o **Istio**, que proveen:

* mTLS automático
* Encriptación de tráfico entre servicios
* Retries, timeouts, circuit breakers
* Políticas de seguridad
* Control de tráfico

Estas configuraciones aplican a todos los microservicios del monorepo.

**Referencia ASM:**
[https://cloud.google.com/service-mesh](https://cloud.google.com/service-mesh)

---

### 📄 **namespace-labels.yaml**

Etiqueta namespaces para habilitar la inyección automática del sidecar (proxy Envoy).

Ejemplo:

```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: ventas
  labels:
    istio-injection: enabled
```

---

### 📄 **peer-authentication.yaml**

Define el nivel de mTLS (Mutual Transport Layer Security) entre pods.

Ejemplo:

```yaml
apiVersion: security.istio.io/v1beta1
kind: PeerAuthentication
metadata:
  name: default
spec:
  mtls:
    mode: STRICT
```

---

### 📄 **destination-rule.yaml**

Define reglas de balanceo, retries y subsets (versiones A/B).

Ejemplo:

```yaml
apiVersion: networking.istio.io/v1beta1
kind: DestinationRule
metadata:
  name: ventas-service
spec:
  host: ventas-service
  trafficPolicy:
    loadBalancer:
      simple: ROUND_ROBIN
    outlierDetection:
      consecutiveErrors: 5
```

---

### 📄 **virtual-service.yaml**

Define rutas HTTP, canary releases o A/B testing.

```yaml
apiVersion: networking.istio.io/v1beta1
kind: VirtualService
metadata:
  name: ventas-service
spec:
  hosts:
  - ventas-service
  http:
  - route:
    - destination:
        host: ventas-service
        subset: v1
      weight: 80
    - destination:
        host: ventas-service
        subset: v2
      weight: 20
```

---

### 📄 **authorization-policy.yaml**

Controla qué servicios pueden llamarse entre sí.

---

## 📁 **platform/observability/**

Incluye configuraciones de:

* **OpenTelemetry**
  [https://opentelemetry.io/](https://opentelemetry.io/)
* **Prometheus**
  [https://prometheus.io/](https://prometheus.io/)
* **Grafana dashboards**
  [https://grafana.com/](https://grafana.com/)

Se almacenan dashboards JSON, reglas, exporters y configuraciones reutilizables.

---

## 📁 **platform/docs/**

Documentación dirigida a Platform Engineers:

* Cómo crear un nuevo servicio
* Cómo usar los templates
* Cómo desplegar con Helm
* Cómo usar Workflows
* Cómo monitorear con OpenTelemetry

---

---

# 📁 **services/**

Contiene **todos los microservicios independientes**, cada uno con:

* Backend `.NET`
* Microfrontend Next.js
* Infraestructura (Helm, Kustomize, Terraform opcional)

Cada servicio es autónomo.

---

# 📁 **services/ventas/**

Este es un ejemplo de microservicio completo.

---

# 📁 **services/ventas/backend/**

Contiene todo el código backend en una solución .NET.

---

## 📄 **Microservicio.sln**

Archivo de solución de Visual Studio.

---

# 📁 **src/**

La arquitectura sigue **Clean Architecture / DDD**:

```
Api → Application → Domain → Infrastructure
```

---

# 📁 **Microservicio.Api/**

Contiene el API HTTP (Controllers, minimal APIs, Middlewares).

### **Ejemplo de `Program.cs`**

```csharp
var builder = WebApplication.CreateBuilder(args);

builder.Services.AddControllers();
builder.Services.AddOpenTelemetry();

var app = builder.Build();
app.MapControllers();
app.Run();
```

### **appsettings.json (configuración base)**

```json
{
  "ConnectionStrings": {
    "Default": "Host=postgres;Database=ventas;Username=app;Password=123"
  }
}
```

---

# 📁 **Microservicio.Application/**

Capa de casos de uso (CQRS, Commands, Queries).

# 📁 **Microservicio.Domain/**

Entidades, ValueObjects, Events.

### Ejemplo Value Object:

```csharp
public record Email(string Value)
{
    public Email
    {
        if(!Value.Contains("@"))
            throw new ArgumentException("Invalid email");
    }
}
```

---

# 📁 **Microservicio.Infrastructure/**

Implementación de persistencia, mensajería, seguridad, observabilidad.

---

## 📁 **Persistence/EF/**

Entity Framework Core (ORM de .NET).
[https://learn.microsoft.com/en-us/ef/](https://learn.microsoft.com/en-us/ef/)

### **DbContext ejemplo**

```csharp
public class AppDbContext : DbContext
{
    public DbSet<Pedido> Pedidos => Set<Pedido>();
}
```

---

## 📁 **Configurations/**

Implementa **IEntityTypeConfiguration**.

Ejemplo:

```csharp
public class PedidoConfig : IEntityTypeConfiguration<Pedido>
{
    public void Configure(EntityTypeBuilder<Pedido> builder)
    {
        builder.ToTable("pedidos");
        builder.HasKey(x => x.Id);
    }
}
```

---

## 📁 **Migrations/**

Migraciones EF Core.

---

# 📁 **Messaging/PubSub/**

Adaptadores de Google Pub/Sub.

Publisher:

```csharp
await publisher.PublishAsync("topic", new { id = 123 });
```

Referencia Pub/Sub:
[https://cloud.google.com/pubsub](https://cloud.google.com/pubsub)

---

# 📁 **Messaging/WorkflowsClient/**

Cliente para invocar Google Cloud Workflows.

Referencia:
[https://cloud.google.com/workflows/docs/reference/rest](https://cloud.google.com/workflows/docs/reference/rest)

---

# 📁 **Observability/**

Configuración de OpenTelemetry (tracing y métricas).

---

# 📁 **Security/**

Implementación de:

* mTLS
* Validación JWT
* IAM Service Accounts

---

# 📁 **services/ventas/tests/**

Pruebas unitarias y de integración.

---

# 📁 **services/ventas/frontend/**

Microfrontend (Next.js + Tailwind).

### Ejemplo `page.tsx`

```tsx
export default function Home() {
  return <h1 className="text-3xl font-bold">Ventas</h1>;
}
```

---

# 📁 **services/ventas/infra/**

Infraestructura específica de este servicio.

---

# 📁 **helm/**

Chart Helm del servicio.
[https://helm.sh/](https://helm.sh/)

---

# 📁 **k8s/**

Manifiestos Kustomize del servicio.
[https://kustomize.io/](https://kustomize.io/)

---

# 📁 **terraform/**

Infra propia del servicio.

---

---

# 📁 **frontends/**

Agrupa portales que integran microfrontends.

Ejemplo:

* portal de administración
* punto de venta

---

# 📁 **infra/**

Infraestructura global del monorepo (GKE, CloudSQL, ASM, PubSub, Workflows).

---

# 📁 **bmad/**

Aquí se almacena todo lo referente a **BMAD Method**:

* Lenguaje ubicuo
* Eventos de dominio
* Políticas
* Escenarios
* Story Modeling

Repositorio oficial:
[https://github.com/bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD)

---

# 📄 **.github/workflows/**

Pipelines CI/CD (GitHub Actions).
[https://docs.github.com/en/actions](https://docs.github.com/en/actions)

---

# 📁 **docs/**

Documentación del proyecto.


