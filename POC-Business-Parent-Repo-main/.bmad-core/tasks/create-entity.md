# Create Domain Entity

## Purpose
Create a domain entity with value objects, aggregates, and business rules following DDD principles.

## Task Configuration
```yaml
elicit: true
interactive: true
required_params:
  - entity_name
  - service_name
  - properties
optional_params:
  - value_objects
  - business_rules
  - domain_events
```

## Task Execution

### Step 1: Elicit Entity Requirements
Ask user for:

**Entity Name**: What is the entity name? (use PascalCase)
**Service Name**: Which bounded context does this entity belong to?
**Properties**: What are the entity properties? (name, type, validation rules)
**Value Objects**: Any complex properties that should be value objects? (optional)
**Business Rules**: What business rules should this entity enforce? (optional)
**Domain Events**: What events should this entity publish? (optional)

### Step 2: Generate Entity Structure
Create the following files:

```
src/modules/{service-name}/domain/
├── entities/
│   └── {entity}.entity.ts
├── value-objects/
│   ├── {entity}-id.value-object.ts
│   └── {property}.value-object.ts
├── aggregates/
│   └── {entity}.aggregate.ts
└── events/
    └── {entity}-{action}.event.ts
```

### Step 3: Create Domain Entity
Generate entity with:
- Unique identifier (UUID or custom ID)
- Properties with proper typing
- Business rule validation methods
- Factory methods for creation
- Domain event publishing
- Immutability patterns

Example structure:
```typescript
export class {Entity}Entity extends AggregateRoot {{
  private constructor(
    public readonly id: {Entity}Id,
    private _property: PropertyValueObject,
    // ... other properties
  ) {{
    super();
  }}

  static create(props: Create{Entity}Props): {Entity}Entity {{
    // Validation logic
    // Business rule enforcement
    const entity = new {Entity}Entity(/* ... */);
    entity.addDomainEvent(new {Entity}CreatedEvent(entity.id));
    return entity;
  }}

  // Business methods
  public updateProperty(newValue: PropertyValueObject): void {{
    // Business rule validation
    this._property = newValue;
    this.addDomainEvent(new {Entity}UpdatedEvent(this.id));
  }}

  // Getters
  get property(): PropertyValueObject {{
    return this._property;
  }}
}}
```

### Step 4: Generate Value Objects
For each value object:
- Immutable classes with validation
- Equality based on value, not reference
- Factory methods with validation
- Type safety and domain expressiveness

### Step 5: Create Aggregate Root
If entity is an aggregate root:
- Extend AggregateRoot base class
- Manage domain events
- Enforce consistency boundaries
- Handle child entity relationships

### Step 6: Generate Domain Events
For each domain event:
- Event class with entity data
- Event handler interfaces
- Integration with application layer
- Serialization for external systems

### Step 7: Generate Entity Framework Configuration
Create EF Core entity configuration with:
- Entity table definition
- Proper field types and constraints
- Relationships with other entities
- Indexes for performance
- Migrations for schema changes

### Step 8: Generate Tests
Create comprehensive tests:
- Entity business rule tests
- Value object validation tests
- Aggregate consistency tests
- Domain event publishing tests
- Factory method tests

## Completion Criteria
- Entity follows DDD patterns
- Business rules properly enforced
- Value objects provide type safety
- Domain events properly implemented
- Entity Framework Core configuration created
- Comprehensive test coverage