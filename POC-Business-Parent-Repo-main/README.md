# Ejemplo de Arquitectura (Clean Architecture + Microservicios)

Repositorio de demostración alineado con `.bmad-core/data/architecture-patterns.md`. Incluye dos microservicios mínimos en .NET 10 con Minimal API, cada uno como repositorio Git independiente conectado aquí como submódulo.

## Qué hay en este repo
- `apps/sales-service`: microservicio Sales (Clean Architecture: Domain, Application, Infrastructure, API).
- `apps/inventory-service`: microservicio Inventory (estructura idéntica).
- Documentación de referencia: `.bmad-core/data/architecture-patterns.md`.

## Uso rápido
```bash
# inicializar submódulos (si clonas el repo)
git submodule update --init --recursive

# levantar Sales
dotnet run --project apps/sales-service/Sales.API/Sales.API.csproj
# -> GET http://localhost:5183/?name=Ana

# levantar Inventory
dotnet run --project apps/inventory-service/Inventory.API/Inventory.API.csproj
# -> GET http://localhost:5076/?location=central
```

## Estructura de cada microservicio
- Domain: entidades de negocio.
- Application: contratos y casos de uso (`GreetingService`, `InventoryStatusService`).
- Infrastructure: implementaciones concretas de los contratos.
- API: Minimal API que expone los casos de uso.