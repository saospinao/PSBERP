# Backend Development Checklist

## Architecture & Structure
- [ ] Hexagonal architecture layers properly separated (domain, application, infrastructure)
- [ ] Domain layer contains only business entities and rules
- [ ] Application layer manages use cases and orchestration
- [ ] Infrastructure layer handles external concerns (database, HTTP, messaging)
- [ ] Primary and secondary ports clearly defined
- [ ] Dependencies point inward toward domain core
- [ ] No circular dependencies between layers

## Domain-Driven Design
- [ ] Bounded contexts properly identified and separated
- [ ] Domain entities follow DDD patterns
- [ ] Value objects used for type safety and validation
- [ ] Aggregates maintain consistency boundaries
- [ ] Domain events properly implemented
- [ ] Domain services handle complex business logic
- [ ] Ubiquitous language used throughout codebase

## .NET & C#
- [ ] .NET 10 with C# latest version
- [ ] Nullable reference types enabled
- [ ] Dependency injection properly configured
- [ ] All classes and methods have proper type definitions
- [ ] No usage of `any` type
- [ ] Decorators used appropriately (@Injectable, @Controller, etc.)
- [ ] Module organization follows domain boundaries
- [ ] Guards and interceptors properly implemented

## Database & Entity Framework Core
- [ ] EF Core DbContext properly configured
- [ ] Entity configurations use Fluent API
- [ ] No raw SQL queries - all operations through EF Core
- [ ] Migrations properly versioned
- [ ] Database migrations created and tested
- [ ] Proper indexing for performance
- [ ] Foreign key relationships properly defined
- [ ] Connection pooling configured
- [ ] Transaction handling for complex operations

## Use Cases & Business Logic
- [ ] Use cases follow single responsibility principle
- [ ] Input validation using class-validator
- [ ] Business rules enforced in domain layer
- [ ] Error handling comprehensive and consistent
- [ ] Command/Query separation implemented
- [ ] Use cases are testable with mocked dependencies

## Repository Pattern
- [ ] Repository interfaces defined in application layer
- [ ] Repository implementations in infrastructure layer
- [ ] Repository methods return domain entities
- [ ] Proper abstraction of data access concerns
- [ ] Repository tests with test database
- [ ] EF Core entity configurations map to domain entities
- [ ] AutoMapper profiles for DTO transformations

## API Design
- [ ] REST endpoints follow RESTful conventions
- [ ] Request/response DTOs properly defined
- [ ] Swagger/OpenAPI documentation complete
- [ ] Proper HTTP status codes returned
- [ ] Input validation on all endpoints
- [ ] Error responses properly formatted

## Testing
- [ ] Unit tests for all domain entities
- [ ] Use case tests with mocked dependencies
- [ ] Integration tests for repositories
- [ ] E2E tests for critical workflows
- [ ] Test coverage meets minimum threshold (80%)
- [ ] Tests follow AAA pattern (Arrange, Act, Assert)

## Security
- [ ] Authentication implemented (JWT/OAuth)
- [ ] Authorization guards protect endpoints
- [ ] Input validation prevents injection attacks
- [ ] Sensitive data properly encrypted
- [ ] Environment variables for secrets
- [ ] CORS properly configured
- [ ] Rate limiting implemented

## Performance
- [ ] Database queries optimized
- [ ] Proper indexing strategy
- [ ] Caching implemented where appropriate
- [ ] Pagination for large datasets
- [ ] Connection pooling configured
- [ ] Memory usage optimized

## Monitoring & Logging
- [ ] Structured logging with Winston
- [ ] Health check endpoints implemented
- [ ] Error tracking and alerting
- [ ] Performance monitoring
- [ ] Audit logging for sensitive operations
- [ ] Log rotation configured

## MonoRepo & Shared Libraries
- [ ] Nx workspace properly configured
- [ ] Shared libraries properly structured
- [ ] Dependencies between apps and libs correct
- [ ] Build system optimized
- [ ] Shared code doesn't violate domain boundaries
- [ ] Library versioning strategy defined

## Microservices (if applicable)
- [ ] Service boundaries align with business domains
- [ ] Inter-service communication via events/messages
- [ ] Each service has independent database
- [ ] Service discovery and configuration
- [ ] Circuit breaker pattern for resilience
- [ ] Distributed tracing implemented

## Development Workflow
- [ ] Git hooks for pre-commit validation
- [ ] Code formatting with Prettier
- [ ] Linting rules enforced
- [ ] TypeScript compilation successful
- [ ] All tests passing
- [ ] No security vulnerabilities
- [ ] Documentation up to date

## Environment Configuration
- [ ] Environment-specific configurations
- [ ] Secrets management properly implemented
- [ ] Database connection strings secure
- [ ] Feature flags for conditional logic
- [ ] Configuration validation on startup
- [ ] Docker configuration if applicable

## Error Handling
- [ ] Custom exception classes for domain errors
- [ ] Global exception filter implemented
- [ ] Proper error logging without sensitive data
- [ ] User-friendly error messages
- [ ] Error response consistency
- [ ] Graceful degradation for external service failures

## Event Handling
- [ ] Domain events properly published
- [ ] Event handlers are idempotent
- [ ] Event sourcing if applicable
- [ ] Message queue integration
- [ ] Dead letter queue handling
- [ ] Event schema versioning