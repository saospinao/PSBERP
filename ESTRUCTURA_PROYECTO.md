# ✅ **1. ESTRUCTURA DE CARPETAS**

Incluye:

✔ Backend .NET 8\
✔ EF Core (DbContext, Migrations, Repositories)\
✔ Tests (unit, integration, security, performance)\
✔ Dapr (Pub/Sub)\
✔ Terraform + Helm para GKE + CloudSQL Postgres\
✔ Dockerfiles + docker-compose\
✔ Microfrontend **React + Next.js 14 + TailwindCSS**\
✔ Conexión del frontend al backend vía `.env`\
✔ GitHub Actions CI/CD\
✔ Carpeta BMAD (sin mezclarse)

📌 **Sin lógica de negocio**, sólo base técnica 100% funcional.

---

# 📁 **ESTRUCTURA COMPLETA DEL PROYECTO**

```
/microservicio-nombre/
│
├── backend/
│   ├── Microservicio.sln
│   └── src/
│       ├── Microservicio.Api/
│       │   ├── Controllers/
│       │   │   └── HealthController.cs
│       │   ├── Endpoints/
│       │   │   └── HealthEndpoint.cs
│       │   ├── Filters/
│       │   │   └── GlobalExceptionFilter.cs
│       │   ├── Middlewares/
│       │   │   └── CorrelationMiddleware.cs
│       │   ├── DI/
│       │   │   └── DependencyInjection.cs
│       │   ├── Program.cs
│       │   ├── appsettings.json
│       │   ├── appsettings.Development.json
│       │   ├── Microservicio.Api.csproj
│       │   └── Properties/
│       │       └── launchSettings.json
│       │
│       ├── Microservicio.Application/
│       │   ├── Interfaces/
│       │   │   └── IClienteService.cs
│       │   ├── Dtos/
│       │   │   └── ClienteDto.cs
│       │   ├── Behaviors/
│       │   │   └── ValidationBehavior.cs
│       │   ├── Services/
│       │   │   └── ClienteService.cs
│       │   ├── Microservicio.Application.csproj
│       │   └── DependencyInjection.cs
│       │
│       ├── Microservicio.Domain/
│       │   ├── Entities/
│       │   │   └── Cliente.cs
│       │   ├── ValueObjects/
│       │   │   └── Email.cs
│       │   ├── Events/
│       │   │   └── ClienteCreadoEvent.cs
│       │   ├── Repositories/
│       │   │   └── IClienteRepository.cs
│       │   └── Microservicio.Domain.csproj
│       │
│       ├── Microservicio.Infrastructure/
│       │   ├── Persistence/
│       │   │   ├── EF/
│       │   │   │   ├── DbContexts/
│       │   │   │   │   └── AppDbContext.cs
│       │   │   │   ├── Configurations/
│       │   │   │   │   └── ClienteConfiguration.cs
│       │   │   │   ├── Migrations/
│       │   │   │   │   └── (migraciones generadas automáticamente)
│       │   │   │   └── Seeds/
│       │   │   │       └── InitialSeed.cs
│       │   │   └── Repositories/
│       │   │       └── ClienteRepository.cs
│       │   ├── Messaging/
│       │   │   └── DaprPubSubService.cs
│       │   ├── Configuration/
│       │   │   └── PostgresOptions.cs
│       │   ├── DependencyInjection.cs
│       │   └── Microservicio.Infrastructure.csproj
│       │
│       ├── Microservicio.CrossCutting/
│       │   ├── Logging/
│       │   │   └── SerilogConfiguration.cs
│       │   ├── Authorization/
│       │   │   └── PermissionChecker.cs
│       │   ├── Constants/
│       │   │   └── AppConstants.cs
│       │   └── Microservicio.CrossCutting.csproj
│
│   └── tests/
│       ├── UnitTests/
│       │   └── ClienteServiceTests.cs
│       ├── IntegrationTests/
│       │   └── ClienteApiTests.cs
│       ├── SecurityTests/
│       │   └── JwtSecurityTests.cs
│       └── PerformanceTests/
│           └── ClienteBenchmark.cs
│
├── frontend/
│   ├── next.config.mjs
│   ├── package.json
│   ├── tailwind.config.js
│   ├── postcss.config.js
│   ├── tsconfig.json
│   ├── public/
│   │   └── favicon.ico
│   ├── src/
│   │   ├── app/
│   │   │   ├── layout.tsx
│   │   │   └── page.tsx
│   │   ├── components/
│   │   │   └── Header.tsx
│   │   ├── lib/
│   │   │   └── api.ts
│   │   └── styles/
│   │       └── globals.css
│   ├── .env.local
│   └── Dockerfile
│
├── infra/
│   ├── terraform/
│   │   ├── main.tf
│   │   ├── variables.tf
│   │   ├── outputs.tf
│   │   └── gke/
│   │       └── cluster.tf
│   ├── helm/
│   │   └── chart/
│   │       ├── Chart.yaml
│   │       ├── values.yaml
│   │       └── templates/
│   │           ├── deployment.yaml
│   │           ├── service.yaml
│   │           └── configmap.yaml
│   ├── dapr/
│   │   └── components/
│   │       └── pubsub.yaml
│   └── docker/
│       ├── backend.Dockerfile
│       ├── frontend.Dockerfile
│       └── docker-compose.yaml
│
├── bmad/
│   └── (archivos BMAD method aquí, aislados)
│
├── .github/
│   └── workflows/
│       ├── backend-ci.yml
│       ├── frontend-ci.yml
│       └── deploy.yml
│
└── docs/
    └── arquitectura.md
```

---

# 1) Visión general del repositorio

Raíz: `/microservicio-nombre/` — un repositorio monorepo que contiene todo lo necesario para desarrollar, testear y desplegar un microservicio completo:

```
/microservicio-nombre/
├─ backend/           # Código .NET 8 (Clean Architecture)
├─ frontend/          # Next.js + React + Tailwind microfrontend
├─ infra/             # IaC (Terraform) + Helm + K8s + Dapr components + Docker
├─ .github/           # GitHub Actions: CI/CD
├─ docs/              # Documentación, ADRs, diagramas
└─ bmad/              # BMAD method artifacts (aislados)
```

Propósito: separar claramente código (backend/frontend) de infraestructura y documentación, manteniendo Clean Architecture dentro del backend.

---

# 2) Convenciones y buenas prácticas generales

* Todos los proyectos .NET usan **TargetFramework** `net8.0`.
* Nombres PascalCase para proyectos y clases (ej. `Microservicio.Api`, `AppDbContext`).
* Cada librería/proyecto .NET tiene su propio `.csproj`. La solución `Microservicio.sln` incluye todos.
* **No** poner reglas de negocio en `Domain` (reglas puras), ni lógica de infraestructura en `Domain` o `Application`.
* `Infrastructure` contiene EF Core, migraciones, Dapr adapters y todo lo que depende de un proveedor.
* `infra/` (raíz) contiene Terraform, Helm charts y YAMLs de Dapr/K8s — estos son archivos de plataforma, no forman parte de la capa `Infrastructure` del código.
* Usar `appsettings.{Environment}.json` para configuración por ambiente; inyectar secretos de producción con Secret Manager / Kubernetes Secrets.
* Tests: `tests/UnitTests` (rápidos y aislados), `tests/IntegrationTests` (usando Testcontainers o real DB), `tests/SecurityTests`, `tests/PerformanceTests`.

---

# 3) Descripción detallada (por carpeta y archivo)

> Cada subsección incluye: propósito, qué archivos incluir, ejemplo mínimo y referencia(s).

---

## A — `backend/` (raíz de backend)

**Propósito:** contener la solución .NET y todos los proyectos que forman el backend siguiendo Clean Architecture (Api, Application, Domain, Infrastructure, CrossCutting) + tests.

### Contenido esperado

```
backend/
├─ Microservicio.sln
├─ src/
│  ├─ Microservicio.Api/
│  ├─ Microservicio.Application/
│  ├─ Microservicio.Domain/
│  ├─ Microservicio.Infrastructure/
│  └─ Microservicio.CrossCutting/
└─ tests/
   ├─ Microservicio.UnitTests/
   ├─ Microservicio.IntegrationTests/
   ├─ Microservicio.SecurityTests/
   └─ Microservicio.PerformanceTests/
```

### Archivo clave: `Microservicio.sln`

* **Qué es:** archivo de solución que agrupa proyectos .NET.
* **Por qué:** facilita abrir todo en Visual Studio/VS Code y compilar en CI.
* **Ejemplo:** generado por `dotnet new sln` y `dotnet sln add`.

**Referencia:** [https://learn.microsoft.com/dotnet/core/tools/dotnet-sln](https://learn.microsoft.com/dotnet/core/tools/dotnet-sln)

---

### `backend/src/Microservicio.Api/` — **Capa de presentación / API**

**Propósito:** Exponer la lógica mediante HTTP (REST) y endpoints Dapr (Cloud Events / pubsub subscriptions). Contiene configuración de DI (inyección de dependencias), middlewares, filtros, swagger, CORS, health checks, Dapr middleware.

#### Archivos y carpetas (detallados)

1. **`Program.cs`**

   * **Qué contiene:** bootstrap de la aplicación (registro de servicios, middlewares, routing, swagger, endpoints).
   * **Ejemplo mínimo:**

     ```csharp
     var builder = WebApplication.CreateBuilder(args);
     builder.Services.AddControllers();
     builder.Services.AddEndpointsApiExplorer();
     builder.Services.AddSwaggerGen();

     // EF + Infrastructure
     builder.Services.AddInfrastructure(builder.Configuration);
     builder.Services.AddApplication(); // registra servicios de Application

     builder.Services.AddCors(options => options.AddPolicy("AllowAll", p => p.AllowAnyOrigin().AllowAnyMethod().AllowAnyHeader()));
     var app = builder.Build();

     app.UseSwagger(); app.UseSwaggerUI();
     app.UseHttpsRedirection();
     app.UseCors("AllowAll");
     app.UseRouting();
     app.MapControllers();
     app.MapSubscribeHandler(); // Dapr subscriptions
     app.Run();
     ```
   * **Por qué:** centraliza la configuración; punto único que CI/CD y Docker usan para arrancar.
   * **Referencia:** [https://learn.microsoft.com/aspnet/core/fundamentals/startup](https://learn.microsoft.com/aspnet/core/fundamentals/startup)

2. **`appsettings.json` / `appsettings.Development.json`**

   * **Qué contiene:** cadenas de conexión, settings Dapr, logging level, feature toggles.
   * **Ejemplo:**

     ```json
     {
       "ConnectionStrings": {
         "DefaultConnection": "Host=localhost;Port=5432;Database=micro;Username=postgres;Password=postgres"
       },
       "Dapr": { "PubSubName": "pubsub" }
     }
     ```
   * **Por qué:** separa configuración del código; en producción usar variables / secret managers.

3. **`Controllers/`**

   * **Qué contiene:** controladores MVC (clase por resource), p. ej. `HealthController.cs`, `ClientesController.cs` (sin lógica, solo invocan Application services).
   * **Ejemplo `HealthController.cs`:**

     ```csharp
     [ApiController]
     [Route("api/[controller]")]
     public class HealthController : ControllerBase
     {
         [HttpGet]
         public IActionResult Get() => Ok(new { status = "UP" });
     }
     ```
   * **Referencia:** [https://learn.microsoft.com/aspnet/core/mvc/controllers/actions](https://learn.microsoft.com/aspnet/core/mvc/controllers/actions)

4. **`Endpoints/`**

   * **Qué contiene:** minimal APIs (archivo por grupo de endpoints). Usar si prefieres `app.MapGet/...` estilo.
   * **Ejemplo `HealthEndpoint.cs`:**

     ```csharp
     public static class HealthEndpoint
     {
         public static void MapHealth(this IEndpointRouteBuilder routes)
         {
             routes.MapGet("/health", () => Results.Ok("OK"));
         }
     }
     ```

5. **`Filters/`**

   * **Qué contiene:** filtros MVC (`IActionFilter`, `IExceptionFilter`) para validación, traducción de excepciones a responses, etc.

   * **Ejemplo `GlobalExceptionFilter.cs`:**

     ```csharp
     public class GlobalExceptionFilter : IExceptionFilter
     {
         public void OnException(ExceptionContext context)
         {
             context.Result = new ObjectResult(new { error = context.Exception.Message }) { StatusCode = 500 };
         }
     }
     ```

   * **Por qué:** centraliza manejo de errores; evita repetición.

6. **`Middlewares/`**

   * **Qué contiene:** middlewares genéricos (cors, logging, correlation id, request timing).

   * **Ejemplo `CorrelationMiddleware.cs`:**

     ```csharp
     public class CorrelationMiddleware
     {
         private readonly RequestDelegate _next;
         public async Task Invoke(HttpContext context)
         {
             context.Request.Headers.TryGetValue("X-Correlation-ID", out var cid);
             if (StringValues.IsNullOrEmpty(cid))
                 context.Request.Headers["X-Correlation-ID"] = Guid.NewGuid().ToString();
             await _next(context);
         }
     }
     ```

   * **Referencia:** [https://learn.microsoft.com/aspnet/core/fundamentals/middleware](https://learn.microsoft.com/aspnet/core/fundamentals/middleware)

7. **`DI/DependencyInjection.cs`**

   * **Qué contiene:** métodos de extensión para registrar servicios del API con la `IServiceCollection`. P. ej. `AddInfrastructure()` y `AddApplication()` pueden estar aquí o en cada proyecto.
   * **Ejemplo:**

     ```csharp
     public static class DependencyInjection
     {
         public static IServiceCollection AddApi(this IServiceCollection services, IConfiguration config)
         {
             services.AddControllers();
             // registrar filtros, swagger, etc.
             return services;
         }
     }
     ```

8. **`Dapr/` (en API) — Subscribers / Bindings / Actors**

   * **Qué contiene:** endpoints que Dapr llamará para entregar eventos (suscripciones). Archivos solo con controllers o handlers marcados con atributos Dapr si se usa `Dapr.AspNetCore`.
   * **Ejemplo de suscripción:**

     ```csharp
     [Topic("pubsub", "order.created")]
     [Route("dapr-subscriptions")]
     public class DaprSubscriberController : ControllerBase
     {
         [HttpPost]
         public async Task<IActionResult> Handle([FromBody] JsonElement data) { /* dispatch to Application */ }
     }
     ```
   * **Referencia:** [https://docs.dapr.io/developing-applications/building-blocks/pubsub/howto-publish-subscribe/](https://docs.dapr.io/developing-applications/building-blocks/pubsub/howto-publish-subscribe/)

9. **`Properties/launchSettings.json`**

   * Configuración de profiles para debugging (urls, environment variables).

---

**Interacciones:** `Microservicio.Api` depende de `Microservicio.Application` (a través de interfaces), y de `Microservicio.Infrastructure` para proveer implementaciones (registradas en DI). `Api` expone HTTP y recibe mensajes Dapr que orquesta hacia Application.

**Referencias generales:**

* ASP.NET Core: [https://learn.microsoft.com/aspnet/core/](https://learn.microsoft.com/aspnet/core/)
* Dapr ASP.NET Core: [https://docs.dapr.io/developing-applications/sdks/dotnet/](https://docs.dapr.io/developing-applications/sdks/dotnet/)

---

## B — `backend/src/Microservicio.Application/` — **Lógica de aplicación / casos de uso**

**Propósito:** contener casos de uso (orquestación), DTOs y contratos que *no* tienen detalles de infraestructura. Aquí van comandos, queries, services de aplicación y mappings. Se comunica con `Domain` y con `Infrastructure` a través de interfaces.

### Carpetas y archivos clave

1. **`Commands/`**

   * **Qué:** clases que representan operaciones mutables (CQRS commands).
   * **Ejemplo `CreateClientCommand.cs`:**

     ```csharp
     public record CreateClientCommand(string Name, string Email) : IRequest<CreateClientResult>;
     ```
   * **Referencia CQRS:** [https://martinfowler.com/bliki/CQRS.html](https://martinfowler.com/bliki/CQRS.html)

2. **`Handlers/` (o `Commands/Handlers/`)**

   * **Qué:** handlers que implementan la ejecución del comando. Normalmente usando `MediatR`.
   * **Ejemplo `CreateClientHandler.cs`:**

     ```csharp
     public class CreateClientHandler : IRequestHandler<CreateClientCommand, CreateClientResult>
     {
         private readonly IClientRepository _repo;
         public async Task<CreateClientResult> Handle(CreateClientCommand cmd, CancellationToken ct)
         {
             // orquesta: valida, llama a Domain para crear entidad, usa repo (interface)
         }
     }
     ```
   * **Referencia MediatR:** [https://github.com/jbogard/MediatR](https://github.com/jbogard/MediatR)

3. **`Queries/`**

   * **Qué:** objetos de sólo lectura. Ejemplo `GetClientByIdQuery`.

4. **`DTOs/`**

   * **Qué:** objetos de transporte; p. ej `ClientDto`.

5. **`Interfaces/`**

   * **Qué:** interfaces (contratos) que la infraestructura implementará: `IClientRepository`, `IUnitOfWork`, `IPubSubPublisher`.
   * **Por qué:** invertir dependencias — Application define lo que necesita; Infrastructure provee la implementación.

6. **`Mappings/`**

   * AutoMapper profiles para mapear Entities -> DTOs.

7. **`Validators/`**

   * FluentValidation reglas para comandos / queries.

8. **`DependencyInjection.cs` (opcional)**

   * Métodos que registren servicios de Application.

**Interacciones:** Application usa Domain (para crear entidades y validar invariantes) y usa Interfaces que son implementadas por Infrastructure (repositorios, sender pubsub). Application no conoce EF Core ni Dapr.

**Referencias:**

* FluentValidation: [https://docs.fluentvalidation.net/](https://docs.fluentvalidation.net/)
* AutoMapper: [https://automapper.org/](https://automapper.org/)

---

## C — `backend/src/Microservicio.Domain/` — **Dominio**

**Propósito:** aquí viven las **reglas estructurales del negocio** (domain logic) — entidades, value objects, aggregates, domain events y especificaciones. **No** debe depender de nada externo (EF, logging, HTTP).

> Importante: esto es el núcleo que no cambia al migrar de ORM o infraestructura.

### Carpetas y archivos detallados

1. **`Entities/`**

   * **Qué:** clases que representan conceptos del dominio (ej: `Cliente`, `Orden`, `Producto`).
   * **Ejemplo `Cliente.cs`:**

     ```csharp
     public class Cliente
     {
         public Guid Id { get; private set; }
         public string Nombre { get; private set; }
         public Email Email { get; private set; }

         public Cliente(string nombre, Email email)
         {
             if (string.IsNullOrWhiteSpace(nombre)) throw new DomainException("Nombre requerido");
             Nombre = nombre; Email = email;
         }
     }
     ```
   * **Propósito:** encerrar invariantes -> if invalid, throw DomainException.

2. **`ValueObjects/`**

   * **Qué:** objetos inmutables que modelan conceptos (ej: `Email`, `Money`, `Address`).
   * **Por qué:** encapsulan validación y comportamiento asociado; igualdad por valor (no por referencia).
   * **Ejemplo `Email.cs`:**

     ```csharp
     public record Email
     {
         public string Value { get; }
         public Email(string value)
         {
             if (!value.Contains("@")) throw new DomainException("Email inválido");
             Value = value;
         }
     }
     ```
   * **Referencia patrón Value Object:** [https://martinfowler.com/bliki/ValueObject.html](https://martinfowler.com/bliki/ValueObject.html)

3. **`Aggregates/`**

   * **Qué:** root aggregates que garantizan consistencia transaccional (ej: `OrderAggregate`).
   * **Por qué:** defines boundaries for transactional consistency.

4. **`DomainEvents/`**

   * **Qué:** eventos puros (in-process) que describen algo que pasó en el dominio (ej: `OrderCreatedEvent`).
   * **Uso:** se usan para notificar handlers dentro del mismo proceso (domain events).

5. **`Specifications/`**

   * **Qué:** reglas reutilizables y combinables (ej: `CustomerHasNoPendingInvoicesSpec`).
   * **Referencia:** patterns/specification: [https://martinfowler.com/apsupp/spec.pdf](https://martinfowler.com/apsupp/spec.pdf)

6. **`Exceptions/`**

   * **Qué:** excepciones de dominio (`DomainException`) con significado para el negocio.

**Interacciones:** `Application` invoca código del Domain para crear y manipular entidades. Domain *no* depende de Application ni Infrastructure.

---

## D — `backend/src/Microservicio.Infrastructure/` — **Implementaciones técnicas**

**Propósito:** implementar contratos declarados por `Application` usando tecnologías concretas (EF Core, Dapr, integración externa). Acá sí está bien usar EF Core, Npgsql, Dapr.Client, etc.

### Estructura propuesta y detallada

```
Microservicio.Infrastructure/
 ├─ Persistence/
 │   ├─ EF/
 │   │  ├─ DbContexts/
 │   │  │   └─ AppDbContext.cs
 │   │  ├─ Configurations/
 │   │  │   └─ ClienteConfiguration.cs
 │   │  ├─ Migrations/
 │   │  └─ Seeds/
 │   ├─ Repositories/
 │   │   └─ ClienteRepository.cs
 │   └─ UnitOfWork/
 ├─ Dapr/
 │   ├─ PubSub/
 │   │  └─ DaprPubSubPublisher.cs
 │   ├─ State/
 │   └─ Bindings/
 ├─ ExternalServices/
 │   └─ EmailProviderAdapter.cs
 ├─ DependencyInjection.cs
 └─ Microservicio.Infrastructure.csproj
```

### Archivos clave (detallados)

1. **`AppDbContext.cs`**

   * **Qué:** `DbContext` de EF Core que define `DbSet<T>` para entidades del dominio que se persisten.
   * **Ejemplo:**

     ```csharp
     public class AppDbContext : DbContext
     {
         public AppDbContext(DbContextOptions<AppDbContext> options) : base(options) { }
         public DbSet<Cliente> Clientes { get; set; }
         protected override void OnModelCreating(ModelBuilder modelBuilder)
         {
            modelBuilder.ApplyConfigurationsFromAssembly(typeof(AppDbContext).Assembly);
            // modelBuilder.Seed(); // opcional
         }
     }
     ```
   * **Referencia EF Core:** [https://learn.microsoft.com/ef/core/](https://learn.microsoft.com/ef/core/)

2. **`Configurations/ClienteConfiguration.cs`**

   * **Qué:** `IEntityTypeConfiguration<Cliente>` para mapping fluent (table names, column types, keys).
   * **Ejemplo:**

     ```csharp
     public class ClienteConfiguration : IEntityTypeConfiguration<Cliente>
     {
         public void Configure(EntityTypeBuilder<Cliente> builder)
         {
             builder.ToTable("clientes");
             builder.HasKey(c => c.Id);
             builder.Property(c => c.Nombre).HasMaxLength(200).IsRequired();
         }
     }
     ```
   * **Por qué:** mantener mappings fuera del Domain.

3. **`Migrations/`**

   * **Qué:** carpeta donde EF Core genera migraciones (`dotnet ef migrations add Initial`).
   * **Contenido típico:** `*_Initial.cs`, `AppDbContextModelSnapshot.cs`.
   * **Referencia:** [https://learn.microsoft.com/ef/core/managing-schemas/migrations/](https://learn.microsoft.com/ef/core/managing-schemas/migrations/)

4. **`Seeds/InitialSeed.cs`**

   * **Qué:** optional data seed (Insert initial rows).
   * **Ejemplo:** `modelBuilder.Entity<Cliente>().HasData(new Cliente { ... });`

5. **`Repositories/ClienteRepository.cs`**

   * **Qué:** implementación concreta de `IClienteRepository` usando `AppDbContext`.
   * **Ejemplo:**

     ```csharp
     public class ClienteRepository : IClienteRepository
     {
         private readonly AppDbContext _db;
         public async Task AddAsync(Cliente c) { await _db.Clientes.AddAsync(c); await _db.SaveChangesAsync(); }
         public Task<Cliente?> GetByIdAsync(Guid id) => _db.Clientes.FirstOrDefaultAsync(x => x.Id==id);
     }
     ```

6. **`UnitOfWork/`**

   * **Qué:** (opcional) pattern to group saves; useful if not using `SaveChanges` ad-hoc. Could be implemented via `IUnitOfWork` that wraps `AppDbContext.SaveChangesAsync()`.

7. **`Dapr/PubSub/`**

   * **Qué:** publisher adapter using `Dapr.Client` to publish events to configured pubsub component.
   * **Ejemplo Dapr publisher:**

     ```csharp
     public class DaprPubSubPublisher : IPubSubPublisher
     {
         private readonly DaprClient _dapr; string _pubsubName;
         public Task PublishAsync<T>(string topic, T payload) => _dapr.PublishEventAsync(_pubsubName, topic, payload);
     }
     ```
   * **Referencia:** [https://docs.dapr.io/developing-applications/sdks/dotnet/](https://docs.dapr.io/developing-applications/sdks/dotnet/)

8. **`ExternalServices/`**

   * **Qué:** adaptadores a APIs externas (ej: email provider, payment gateway). Implementan interfaces definidas en Application.

9. **`DependencyInjection.cs`**

   * **Qué:** extensión `IServiceCollection` para registrar `DbContext`, repositories, Dapr publisher, external adapters, e.g.:

     ```csharp
     services.AddDbContext<AppDbContext>(opts => opts.UseNpgsql(conn));
     services.AddScoped<IClienteRepository, ClienteRepository>();
     services.AddSingleton<IPubSubPublisher, DaprPubSubPublisher>();
     ```

**Interacciones:** `Infrastructure` depende de `Domain` (entities) y `Application` (interfaces), pero `Domain` no depende de `Infrastructure`. `Api` uses `DependencyInjection` to wire concrete types.

**Referencias:**

* EF Core: [https://learn.microsoft.com/ef/core/](https://learn.microsoft.com/ef/core/)
* Npgsql (Postgres EF provider): [https://www.npgsql.org/efcore/](https://www.npgsql.org/efcore/)
* Dapr .NET SDK: [https://docs.dapr.io/developing-applications/sdks/dotnet/](https://docs.dapr.io/developing-applications/sdks/dotnet/)

---

## E — `backend/src/Microservicio.CrossCutting/` — utilities comunes

**Propósito:** contener funcionalidades transversales que no pertenecen al dominio (logging, monitoring, security helpers, converters). Pueden ser referenciadas por Api, Application y Infrastructure.

### Componentes comunes

* **`Logging/SerilogConfiguration.cs`** — configurar Serilog sinks (console, file, seq).

  * **Ref:** [https://serilog.net/](https://serilog.net/)

* **`Monitoring/`** — health checks config, prometheus exporters (if used).

  * **Ref:** [https://learn.microsoft.com/aspnet/core/host-and-deploy/health-checks](https://learn.microsoft.com/aspnet/core/host-and-deploy/health-checks)

* **`Security/PermissionChecker.cs`** — helper para comprobar claims/roles.

  * **Ref:** [https://learn.microsoft.com/aspnet/core/security/authorization/introduction](https://learn.microsoft.com/aspnet/core/security/authorization/introduction)

* **`Middleware/`** — middlewares comunes (e.g., RequestTimingMiddleware) si deseas compartirlos.

**Buenas prácticas:** CrossCutting *no* debería llamar a Domain internals; su funcionalidad debe ser genérica.

---

## F — `backend/tests/` — tests projects

**Propósito:** contener proyectos de pruebas organizados por tipología.

* `UnitTests/` — pruebas rápidas en memoria o mocks. P. ej. `ClienteServiceTests.cs` que moca `IClienteRepository`.
* `IntegrationTests/` — pruebas que arrancan `AppDbContext` con Testcontainers o una instancia real de Postgres. P. ej. `ClienteApiTests` que ejecuten `WebApplicationFactory<Program>`.
* `SecurityTests/` — pruebas de tokens, claims, autorización.
* `PerformanceTests/` — benchmarks (BenchmarkDotNet) o scripts k6.

**Ejemplo Unit test (xUnit):**

```csharp
public class ClienteServiceTests
{
    [Fact]
    public async Task CreateClient_Should_CallRepository()
    {
        var repoMock = new Mock<IClienteRepository>();
        var svc = new ClienteService(repoMock.Object);
        await svc.CreateAsync(new ClienteDto("name","e@mail"));
        repoMock.Verify(r => r.AddAsync(It.IsAny<Cliente>()), Times.Once);
    }
}
```

**Referencias:**

* xUnit: [https://xunit.net/](https://xunit.net/)
* Testcontainers for .NET: [https://dotnet.testcontainers.org/](https://dotnet.testcontainers.org/)

---

## G — `frontend/` — Next.js + React + Tailwind (microfrontend)

**Propósito:** UI del microservicio, integrado con el backend mediante fetch/axios y variables de entorno. Siguiente convención: Next.js app router (`src/app/`) con TypeScript.

### Archivos y carpetas clave (extenso, con ejemplos)

```
frontend/
├─ package.json
├─ next.config.mjs
├─ tsconfig.json
├─ tailwind.config.js
├─ postcss.config.js
├─ .env.local
├─ Dockerfile
└─ src/
   ├─ app/
   │  ├─ layout.tsx
   │  └─ page.tsx
   ├─ components/
   │  └─ Header.tsx
   ├─ lib/
   │  └─ api.ts
   └─ styles/
      └─ globals.css
```

### `package.json`

* **Qué:** dependencias y scripts.
* **Ejemplo:**

  ```json
  {
    "name": "microfrontend",
    "private": true,
    "scripts": {
      "dev": "next dev -p 3000",
      "build": "next build",
      "start": "next start",
      "lint": "next lint"
    },
    "dependencies": {
      "next": "14.0.0",
      "react": "18.x",
      "react-dom": "18.x",
      "tailwindcss": "^3.4.0",
      "axios": "^1.4.0"
    }
  }
  ```

### `next.config.mjs`

* **Qué:** configuración Next.js (React strict, image domains).
* **Ejemplo mínimo:**

  ```js
  const nextConfig = { reactStrictMode: true };
  export default nextConfig;
  ```
* **Referencia:** [https://nextjs.org/docs](https://nextjs.org/docs)

### `tailwind.config.js`

* **Qué:** configuración Tailwind.
* **Ejemplo:**

  ```js
  module.exports = {
    content: ["./src/**/*.{js,ts,jsx,tsx}"],
    theme: { extend: {} },
    plugins: [],
  }
  ```
* **Referencia:** [https://tailwindcss.com/docs/installation](https://tailwindcss.com/docs/installation)

### `src/app/layout.tsx` y `page.tsx`

* **layout.tsx**: HTML shell, import global styles.
* **page.tsx**: ruta principal, p. ej. consume health endpoint.
* **Ejemplo `page.tsx`:**

  ```tsx
  import { useEffect, useState } from "react";
  import { api } from "@/lib/api";

  export default function Page() {
    const [health, setHealth] = useState<string>("loading");
    useEffect(() => { api.health().then(r=>setHealth(r.status)); }, []);
    return <div className="p-4"><h1>{health}</h1></div>;
  }
  ```

### `src/lib/api.ts`

* **Qué:** wrapper axios/fetch con `baseURL` usando `NEXT_PUBLIC_API_URL`.
* **Ejemplo:**

  ```ts
  import axios from "axios";
  export const api = axios.create({ baseURL: process.env.NEXT_PUBLIC_API_URL });
  export const health = async () => (await api.get("/api/health")).data;
  ```

### `.env.local`

* **Qué:** variables locales, p. ej.:

  ```
  NEXT_PUBLIC_API_URL=http://localhost:5000
  ```

### `Dockerfile` del frontend

* **Qué:** construir app y servir estático con `next start` o export static.
* **Ejemplo mínimo:**

  ```dockerfile
  FROM node:18-alpine AS builder
  WORKDIR /app
  COPY package*.json ./
  RUN npm install
  COPY . .
  RUN npm run build

  FROM node:18-alpine AS runner
  WORKDIR /app
  COPY --from=builder /app/.next .next
  COPY --from=builder /app/public public
  COPY --from=builder /app/package.json package.json
  RUN npm install --production
  CMD ["npm", "start"]
  ```

**Interacciones frontend ↔ backend:** Frontend consume endpoints HTTP (`/api/health`, `/api/...`). En producción, helm or ingress route maps domain to frontend and backend. Use CORS on backend.

**Referencias:**

* Next.js: [https://nextjs.org/docs](https://nextjs.org/docs)
* Tailwind CSS: [https://tailwindcss.com/](https://tailwindcss.com/)
* React: [https://react.dev/](https://react.dev/)

---

## H — `infra/` — infraestructura (platform engineering)

**Propósito:** contener todo lo necesario para desplegar y operar: Terraform (crear GKE, CloudSQL), Helm chart (templated k8s manifests), plain k8s YAML (opcional), Dapr components (pubsub, state), Dockerfiles and docker-compose for local dev.

### Estructura propuesta

```
infra/
├─ terraform/
│  ├─ main.tf
│  ├─ variables.tf
│  ├─ outputs.tf
│  └─ modules/...
├─ helm/
│  └─ chart/
│     ├─ Chart.yaml
│     ├─ values.yaml
│     └─ templates/
│        ├─ deployment.yaml
│        ├─ service.yaml
│        └─ ingress.yaml
├─ dapr/
│  └─ components/
│     ├─ pubsub.yaml
│     ├─ statestore.yaml
│     └─ secretstore.yaml
└─ docker/
   ├─ backend.Dockerfile
   ├─ frontend.Dockerfile
   └─ docker-compose.yaml
```

### `infra/terraform/*` (detallado)

* **`main.tf`**: provider(s), backends, resource blocks (GKE cluster, CloudSQL Postgres, service accounts).
* **`variables.tf`**: define variables input (project id, region, cluster name, db tier).
* **`outputs.tf`**: outputs like kubeconfig, db connection string.

**Ejemplo:** (very small)

```hcl
provider "google" { project = var.project }
resource "google_container_cluster" "gke" { name = var.cluster_name; location = var.region; initial_node_count = 1 }
```

**Referencia Terraform + GCP:**

* Terraform: [https://developer.hashicorp.com/terraform](https://developer.hashicorp.com/terraform)
* Google Cloud Provider: [https://registry.terraform.io/providers/hashicorp/google/latest/docs](https://registry.terraform.io/providers/hashicorp/google/latest/docs)

### `infra/helm/chart/*`

* **`Chart.yaml`**: chart metadata.
* **`values.yaml`**: default values for image repo, replicas, resources.
* **`templates/deployment.yaml`**: templated Deployment (image, envFrom secrets/configmaps, readiness/liveness probes).
* **Ejemplo snippet:**

  ```yaml
  apiVersion: apps/v1
  kind: Deployment
  spec:
    replicas: {{ .Values.replicaCount }}
    template:
      spec:
        containers:
          - name: backend
            image: "{{ .Values.image.repository }}:{{ .Values.image.tag }}"
            env:
              - name: ConnectionStrings__DefaultConnection
                valueFrom:
                  secretKeyRef:
                     name: db-credentials
                     key: connection
  ```

**Referencias:** [https://helm.sh/docs/](https://helm.sh/docs/)

### `infra/dapr/components/*`

* **`pubsub.yaml`** (ejemplo in-memory or Redis for dev)

  ```yaml
  apiVersion: dapr.io/v1alpha1
  kind: Component
  metadata: { name: "pubsub" }
  spec:
    type: pubsub.redis
    version: v1
    metadata:
      - name: redisHost
        value: "redis:6379"
  ```
* **`statestore.yaml`**: configure Redis/Mongo etc.
  **Referencia:** [https://docs.dapr.io/operations/components/setup-pubsub/supported-pubsub/redis/](https://docs.dapr.io/operations/components/setup-pubsub/supported-pubsub/redis/)

### `infra/docker/docker-compose.yaml` (local dev)

* Compose with `api`, `frontend`, `postgres`, optional `redis` (for dapr in-mem pubsub but Dapr can run locally separately).
* Example snippet:

  ```yaml
  services:
    postgres:
      image: postgres:16
      environment: POSTGRES_PASSWORD:postgres
      ports: - "5432:5432"
    api:
      build: ../backend/src/Microservicio.Api
      environment:
         - ConnectionStrings__DefaultConnection=Host=postgres;...
      ports: - "5000:80"
  ```

**Referencia Docker Compose:** [https://docs.docker.com/compose/](https://docs.docker.com/compose/)

---

## I — `.github/workflows/` — GitHub Actions CI/CD

**Propósito:** automatizar build/test/publish/deploy.

### Workflows recomendados

1. `backend-ci.yml` — build .NET, run unit tests, run linting, build docker image, push to registry.
2. `frontend-ci.yml` — `npm install`, `npm run build`, run lint, run tests, build docker image.
3. `deploy.yml` — on `release` or manual dispatch: run terraform plan/apply (or apply infra in separate pipeline), helm upgrade --install to cluster using GitHub OIDC.

**Ejemplo minimal backend CI:**

```yaml
name: Backend CI
on: [push]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-dotnet@v3
        with: dotnet-version: '8.0.x'
      - run: dotnet build backend/Microservicio.sln --configuration Release
      - run: dotnet test backend/tests/Microservicio.UnitTests --no-build
```

**Reference:** [https://docs.github.com/actions](https://docs.github.com/actions)

---

## J — `docs/` — documentación

**Propósito:** ADRs, arquitectura, cómo correr local, diagramas, guía de onboarding.

Ejemplos de archivos:

* `arquitectura.md` — overview C4 diagrams
* `run-local.md` — pasos para levantar docker-compose + dapr
* `README.md` — quickstart

**Buenas prácticas:** incluir `CONTRIBUTING.md` y `CODE_OF_CONDUCT.md`.

---

## K — `bmad/` — BMAD Method artifacts

**Propósito:** contener todos los artefactos del método BMAD (commands, events, ubiquitous language, canvases) **aislados** para no mezclar diseño con implementación.

Estructura sugerida:

```
bmad/
├─ 00-overview.md
├─ ubiquitous-language.md
├─ commands/
│  └─ create-order.md
├─ events/
│  └─ order-created.md
└─ scenarios/
   └─ given-when-then.md
```

**Notas:** mantener como documentación; no generar código desde aquí directamente (puedes usar plantillas para generar stubs).

**Referencia BMAD:** [https://github.com/bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD)

---

# 4) Checklist final — archivos mínimos obligatorios para ejecutar (sin lógica de negocio)

A continuación los archivos que deben existir y su propósito — el repo **compilará** y se podrá iniciar localmente (con docker-compose) si estos están presentes con contenido mínimo:

### Backend

* `backend/Microservicio.sln` — incluye proyectos.
* `backend/src/Microservicio.Api/Microservicio.Api.csproj`
* `backend/src/Microservicio.Api/Program.cs` — configura services y MapControllers.
* `backend/src/Microservicio.Api/Controllers/HealthController.cs` — endpoint health.
* `backend/src/Microservicio.Application/Microservicio.Application.csproj`
* `backend/src/Microservicio.Domain/Microservicio.Domain.csproj`
* `backend/src/Microservicio.Infrastructure/Microservicio.Infrastructure.csproj`
* `backend/src/Microservicio.Infrastructure/Persistence/EF/DbContexts/AppDbContext.cs` — minimal DbContext.
* `backend/tests/...` — projects with at least one dummy test.

### Frontend

* `frontend/package.json` with `dev`/`build`/`start` scripts.
* `frontend/next.config.mjs`, `tailwind.config.js`, `postcss.config.js`.
* `frontend/src/app/page.tsx` (Next app) or `pages/index.tsx` (pages router) that calls `api/health`.
* `.env.local` with `NEXT_PUBLIC_API_URL` for local dev.

### Infra

* `infra/docker/docker-compose.yaml` to run `postgres` and `api` and `frontend` locally.
* `infra/dapr/components/pubsub.yaml` (dev in-memory or redis).
* `infra/helm/chart/*` minimal templates.
* `infra/terraform/main.tf` minimal provider config if you intend to use terraform.

### CI

* `.github/workflows/backend-ci.yml` minimal to build and test backend.

---

# 5) Ejemplos prácticos rápidos (cómo ejecutar localmente)

1. **Levantar Postgres y API con docker-compose**

   * `cd infra/docker` y `docker compose up --build`
   * `docker logs` para verificar
   * Llamar `http://localhost:5000/api/health` -> `OK`

2. **Levantar frontend**

   * `cd frontend`
   * `npm install`
   * `npm run dev`
   * Abrir `http://localhost:3000` y debería mostrar `API OK` si `NEXT_PUBLIC_API_URL` apunta al backend.

3. **Aplicar migraciones EF Core**

   * `dotnet ef migrations add Initial -p backend/src/Microservicio.Infrastructure -s backend/src/Microservicio.Api`
   * `dotnet ef database update ...` (o usar migrator container CI/CD)

4. **Ejecutar Dapr local**

   * `dapr run --app-id api --app-port 5000 -- dotnet run --project backend/src/Microservicio.Api`
   * Dapr entregará pubsub a endpoints anotados.

**Referencias de uso:**

* Dapr run: [https://docs.dapr.io/getting-started/](https://docs.dapr.io/getting-started/)
* EF Core CLI: [https://learn.microsoft.com/ef/core/cli/dotnet](https://learn.microsoft.com/ef/core/cli/dotnet)

---

# 6) Recursos y referencias finales (útiles para cada tecnología)

* .NET 8: [https://dotnet.microsoft.com](https://dotnet.microsoft.com)
* ASP.NET Core: [https://learn.microsoft.com/aspnet/core/](https://learn.microsoft.com/aspnet/core/)
* EF Core: [https://learn.microsoft.com/ef/core/](https://learn.microsoft.com/ef/core/)
* Npgsql (Postgres provider): [https://www.npgsql.org/efcore/](https://www.npgsql.org/efcore/)
* Dapr: [https://docs.dapr.io/](https://docs.dapr.io/)
* Next.js: [https://nextjs.org/docs](https://nextjs.org/docs)
* Tailwind CSS: [https://tailwindcss.com/docs](https://tailwindcss.com/docs)
* Docker: [https://docs.docker.com/](https://docs.docker.com/)
* Docker Compose: [https://docs.docker.com/compose/](https://docs.docker.com/compose/)
* Kubernetes: [https://kubernetes.io/docs/](https://kubernetes.io/docs/)
* Helm: [https://helm.sh/docs/](https://helm.sh/docs/)
* Terraform: [https://developer.hashicorp.com/terraform](https://developer.hashicorp.com/terraform)
* GitHub Actions: [https://docs.github.com/actions](https://docs.github.com/actions)
* xUnit: [https://xunit.net/](https://xunit.net/)
* Testcontainers: [https://dotnet.testcontainers.org/](https://dotnet.testcontainers.org/)
* Serilog: [https://serilog.net/](https://serilog.net/)
* AutoMapper: [https://automapper.org/](https://automapper.org/)
* FluentValidation: [https://docs.fluentvalidation.net/](https://docs.fluentvalidation.net/)

---


