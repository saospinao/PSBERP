# General Naming Conventions (C#, PostgreSQL, TypeScript)

**Document Type:** Development Standards
**Version:** 1.5
**Date:** 2025-12-04 (Updated)
**Applicability:** All projects using C#, PostgreSQL, and TypeScript stack

---

## Purpose

This document establishes consistent naming conventions across the full technology stack (C#, PostgreSQL, TypeScript) to ensure:

1. **Code readability** - Developers can quickly understand code structure
2. **Consistency** - Same patterns throughout the codebase
3. **Interoperability** - Smooth mapping between backend, database, and frontend
4. **Maintainability** - Easy to refactor and update
5. **Team alignment** - All developers follow the same standards

---

## Overview

We adopt **language-specific conventions** with **explicit mapping** between layers:

### 1. C# Backend Conventions (PascalCase)
### 2. PostgreSQL Database Conventions (snake_case)
### 3. TypeScript Frontend Conventions (camelCase)
### 4. EF Core Mapping Strategy (Automatic snake_case conversion)

---

## 1. C# Backend Conventions

### 1.1 Acronym Capitalization Rule

**Rule:** All acronyms and initialisms must be written in full uppercase when used in PascalCase names, regardless of their length.

**Examples:**
- ✅ `ID`, `API`, `HTTP`, `XML`, `JSON`, `URL`, `HTML`, `SQL`, `ERP`, `CRM`
- ✅ `public string ID { get; set; }`
- ✅ `public string APIKey { get; set; }`
- ✅ `public class HTTPClient { }`
- ✅ `public interface IERPService { }`

**Rationale:** Maintains visual consistency, improves readability, and follows industry-standard conventions for technical identifiers.

**Incorrect Examples:**
- ❌ `Id`, `Api`, `Http` (Only first letter capitalized)
- ❌ `id`, `api`, `http` (All lowercase)
- ❌ `ApiKey`, `HttpClient` (Treated as regular words)

---

### 1.2 Namespaces

**Convention:** PascalCase with dots

```csharp
namespace MyCompany.ProjectName;
namespace Services.ProductManagement.Domain;
namespace Services.Authentication.API;
namespace Shared.Common.Utilities;
```

### 1.3 Classes, Records, Structs

**Convention:** PascalCase

```csharp
// ✅ CORRECT
public class Product { }
public record ProductResponse { }
public struct Money { }
public class APIClient { }
public class HTTPHandler { }
public class XMLParser { }

// ❌ INCORRECT
public class product { }                // lowercase
public class Product_Service { }        // Don't use underscores
public class productService { }         // camelCase
```

### 1.4 Interfaces

**Convention:** PascalCase with `I` prefix

```csharp
// ✅ CORRECT
public interface IProductService { }
public interface IDatabaseConnection { }
public interface IRepository<T> { }
public interface IAPIClient { }

// ❌ INCORRECT
public interface ProductService { }     // Missing I prefix
public interface iProductService { }    // Wrong casing
```

### 1.5 Methods

**Convention:** PascalCase with verb prefix

```csharp
// ✅ CORRECT
public async Task<Product> GetByIdAsync(Guid id) { }
public async Task<bool> ValidatePermissionAsync(string permission) { }
public void ProcessOrder() { }
public decimal CalculateTotal() { }

// ❌ INCORRECT
public async Task<Product> getById(Guid id) { }        // camelCase
public async Task<Product> Get_By_Id(Guid id) { }      // Snake_Case
```

### 1.6 Properties

**Convention:** PascalCase, NO underscores

**Primary Identifiers:**
- **Guid Primary Key:** Use `ID` property name
- **String Business Identifier:** Use `Code` property name

```csharp
// ✅ CORRECT
public class Product
{
    public Guid ID { get; set; }                    // Primary key (Guid)
    public string Code { get; set; }                // Business identifier (string)
    public string Name { get; set; }
    public decimal Price { get; set; }
    public bool IsActive { get; set; }
    public DateTime CreatedAt { get; set; }
    public Guid CreatedByUserID { get; set; }       // FK to User
    public DateTime? UpdatedAt { get; set; }
    public Guid? UpdatedByUserID { get; set; }      // FK to User (nullable)

    // Acronyms in properties (full uppercase)
    public string APIKey { get; set; }              // API (3+ letters)
    public string HTTPEndpoint { get; set; }        // HTTP
    public string XMLContent { get; set; }          // XML
    public string JSONPayload { get; set; }         // JSON
}

// ❌ INCORRECT
public Guid UUID { get; set; }              // Use ID instead
public string ID { get; set; }              // Use Code for string identifiers
public DateTime Created_At { get; set; }    // Don't use underscores
public string Api_Key { get; set; }         // Don't use underscores
public string ApiKey { get; set; }          // Keep acronyms uppercase: APIKey
```

### 1.7 Fields (Private)

**Convention:** camelCase with `_` prefix (for fields), or PascalCase (for properties)

```csharp
// ✅ CORRECT (private fields)
private readonly HttpClient _httpClient;
private readonly string _apiBaseUrl;
private string _cachedValue;

// ✅ CORRECT (auto-properties - preferred)
public string APIBaseUrl { get; set; }

// ❌ INCORRECT
private readonly HttpClient httpClient;        // Missing underscore
private readonly string APIBaseUrl;            // PascalCase for field
```

### 1.8 Local Variables and Parameters

**Convention:** camelCase

```csharp
// ✅ CORRECT - camelCase for parameters
public async Task<Product> GetProductAsync(Guid id, Guid companyId)
{
    var unitPrice = await LoadPriceAsync(id);
    var discountRate = CalculateDiscount(unitPrice);
    return new Product { Price = unitPrice - discountRate };
}

// Alternative: Using Code instead of ID
public async Task<Product> GetByCodeAsync(string code, Guid companyId)
{
    var product = await _repository.FindByCodeAsync(code, companyId);
    var discountRate = CalculateDiscount(product.Price);
    return product;
}

// ❌ INCORRECT
public async Task<Product> GetProductAsync(Guid ProductId, Guid CompanyId)  // PascalCase params
{
    var UnitPrice = ...;  // PascalCase variable
}
```

**Exception: Record Positional Parameters**

Record positional parameters use **PascalCase** because they become public properties:

```csharp
// ✅ CORRECT - Positional parameters become properties (PascalCase)
public sealed record ErrorResponse(ErrorDetail Error);
public sealed record ProductResponse(Guid ID, string Code, string Name, bool IsActive);

// ❌ INCORRECT - camelCase would create camelCase properties
public sealed record ErrorResponse(ErrorDetail error);  // Creates "error" property
```

### 1.9 Constants

**Convention:** UPPER_SNAKE_CASE

```csharp
// ✅ CORRECT
public const int MAX_RETRY_ATTEMPTS = 3;
public const int DEFAULT_TIMEOUT_SECONDS = 30;
public const string DEFAULT_CURRENCY = "USD";
public const string API_VERSION = "v1";
public const decimal TAX_RATE = 0.16m;
public static readonly TimeSpan CACHE_EXPIRATION = TimeSpan.FromMinutes(5);
public static readonly string[] ALLOWED_FILE_TYPES = { "pdf", "jpg", "png" };

// ❌ INCORRECT
public const int MaxRetryAttempts = 3;          // PascalCase
public const int max_retry_attempts = 3;        // lowercase
public const string Api_Version = "v1";         // Mixed case
```

### 1.10 Enums

**Convention:** PascalCase for enum name and values

```csharp
// ✅ CORRECT
public enum OrderStatus
{
    Pending,
    Approved,
    Rejected,
    Cancelled
}

public enum OperationType
{
    Create,
    Read,
    Update,
    Delete
}

// ❌ INCORRECT
public enum orderStatus { }                 // camelCase enum name
public enum OrderStatus { PENDING }         // UPPER_CASE value
public enum OrderStatus { pending }         // lowercase value
```

---

## 2. PostgreSQL Database Conventions

### 2.1 Tables

**Convention:** snake_case, PLURAL or SINGULAR form (configurable per project)

**EF Core Pluralization:** This standard supports both approaches:
- **Option A (Pluralization Enabled):** EF Core automatically pluralizes table names
- **Option B (Pluralization Disabled):** Manual control with singular names

**Example with Pluralization Enabled:**
```sql
-- ✅ CORRECT (Plural, snake_case)
CREATE TABLE products ( ... );              -- class: Product
CREATE TABLE customers ( ... );             -- class: Customer
CREATE TABLE order_items ( ... );           -- class: OrderItem
CREATE TABLE user_roles ( ... );            -- class: UserRole

-- ❌ INCORRECT
CREATE TABLE Products ( ... );              -- PascalCase
CREATE TABLE product ( ... );               -- Singular (if pluralization enabled)
CREATE TABLE product-items ( ... );         -- Hyphens not allowed
```

**Example with Pluralization Disabled:**
```sql
-- ✅ CORRECT (Singular, snake_case)
CREATE TABLE product ( ... );               -- class: Product
CREATE TABLE customer ( ... );              -- class: Customer
CREATE TABLE order_item ( ... );            -- class: OrderItem
CREATE TABLE user_role ( ... );             -- class: UserRole
```

**Key Identifiers:**
- **Primary Key (Guid):** Use `id` column name
- **Business Identifier (string):** Use `code` column name

```sql
-- ✅ CORRECT (with pluralization)
CREATE TABLE products (
    id UUID PRIMARY KEY DEFAULT uuidv7(),
    code VARCHAR(50) NOT NULL,
    name VARCHAR(200) NOT NULL,
    price DECIMAL(18,2) NOT NULL,
    is_active BOOLEAN DEFAULT true,
    created_at TIMESTAMP DEFAULT NOW(),
    created_by_user_id UUID REFERENCES users(id)
);

CREATE UNIQUE INDEX uk_products_code ON products(code);
```

### 2.2 Columns

**Convention:** snake_case (mapped automatically from C# PascalCase properties)

```sql
-- ✅ CORRECT (snake_case, PostgreSQL standard)
CREATE TABLE products (
    id UUID PRIMARY KEY,                        -- PK
    code VARCHAR(50),                           -- Business identifier
    name VARCHAR(200),
    price DECIMAL(18,2),
    is_active BOOLEAN,                          -- Boolean flag
    created_at TIMESTAMP,                       -- Audit field
    created_by_user_id UUID REFERENCES users(id),
    updated_at TIMESTAMP,
    updated_by_user_id UUID REFERENCES users(id)
);

-- C# class with PascalCase (maps automatically)
public class Product
{
    public Guid ID { get; set; }                // → id
    public string Code { get; set; }            // → code
    public string Name { get; set; }            // → name
    public decimal Price { get; set; }          // → price
    public bool IsActive { get; set; }          // → is_active
    public DateTime CreatedAt { get; set; }     // → created_at
    public Guid CreatedByUserID { get; set; }   // → created_by_user_id
}

-- ❌ INCORRECT
CREATE TABLE products (
    ID UUID PRIMARY KEY,                        -- PascalCase
    Price DECIMAL(18,2),                        -- PascalCase
    IsActive BOOLEAN,                           -- PascalCase
    created-at TIMESTAMP,                       -- Hyphens not allowed
    Created_At TIMESTAMP                        -- Mixed case
);
```

**Acronym Columns:**
```sql
-- C# properties with acronyms
public string APIKey { get; set; }              // → api_key
public string HTTPEndpoint { get; set; }        // → http_endpoint
public string XMLContent { get; set; }          // → xml_content
public string JSONPayload { get; set; }         // → json_payload
public int HTTPStatusCode { get; set; }         // → http_status_code

-- PostgreSQL columns (snake_case)
CREATE TABLE api_configurations (
    id UUID PRIMARY KEY,
    api_key VARCHAR(100),
    http_endpoint VARCHAR(500),
    xml_content TEXT,
    json_payload JSONB,
    http_status_code INTEGER
);
```

### 2.3 Foreign Key Columns

**Convention:** C# uses `{EntityName}ID`, database uses `{entity_name}_id` (snake_case)

**Foreign Keys:**

Use the exact entity name + ID suffix in C#. Database columns are automatically converted to snake_case.

```sql
-- ✅ CORRECT - Specific entity references (snake_case in database)
CREATE TABLE orders (
    id UUID PRIMARY KEY,
    customer_id UUID REFERENCES customers(id),      -- FK to customers table
    product_id UUID REFERENCES products(id),        -- FK to products table
    company_id UUID REFERENCES companies(id),       -- FK to companies table
    warehouse_id UUID REFERENCES warehouses(id)     -- FK to warehouses table
);

-- C# class (PascalCase properties → snake_case columns)
public class Order
{
    public Guid ID { get; set; }            // → id
    public Guid CustomerID { get; set; }    // → customer_id
    public Guid ProductID { get; set; }     // → product_id
    public Guid CompanyID { get; set; }     // → company_id
}
```

**Multiple References to Same Entity:**

When a table has multiple foreign keys to the same entity, use a context prefix to differentiate them.

**Pattern:** C# uses `{Context}{EntityName}ID`, database uses `{context}_{entity_name}_id`

```sql
-- ✅ CORRECT - Multiple FKs to same entity with context prefix
CREATE TABLE shipments (
    id UUID PRIMARY KEY,
    origin_warehouse_id UUID REFERENCES warehouses(id),      -- Origin warehouse
    destination_warehouse_id UUID REFERENCES warehouses(id), -- Destination warehouse
    shipped_at TIMESTAMP
);

CREATE TABLE transfers (
    id UUID PRIMARY KEY,
    source_account_id UUID REFERENCES accounts(id),      -- Source account
    destination_account_id UUID REFERENCES accounts(id), -- Destination account
    amount DECIMAL(18,2)
);

CREATE TABLE transactions (
    id UUID PRIMARY KEY,
    sender_user_id UUID REFERENCES users(id),    -- Sender user
    receiver_user_id UUID REFERENCES users(id),  -- Receiver user
    amount DECIMAL(18,2)
);

-- C# classes
public class Shipment
{
    public Guid ID { get; set; }
    public Guid OriginWarehouseID { get; set; }        // → origin_warehouse_id
    public Guid DestinationWarehouseID { get; set; }   // → destination_warehouse_id
}

public class Transfer
{
    public Guid ID { get; set; }
    public Guid SourceAccountID { get; set; }          // → source_account_id
    public Guid DestinationAccountID { get; set; }     // → destination_account_id
}
```

**Common Context Prefixes:**
- `Origin` / `Destination` - Origin and destination locations
- `Source` / `Destination` - Source and destination entities
- `Sender` / `Receiver` - Sender and receiver in transactions
- `Parent` / `Child` - Hierarchical relationships
- `Primary` / `Secondary` - Primary and secondary references
- `Manager` / `Subordinate` - Management relationships

**Audit Foreign Keys:**

For audit fields that reference Users, use `{Action}ByUserID` pattern in C#:

```sql
-- ✅ CORRECT - Explicit User references with action context (snake_case in database)
CREATE TABLE products (
    id UUID PRIMARY KEY,
    code VARCHAR(50),
    name VARCHAR(200),
    created_by_user_id UUID REFERENCES users(id),   -- Who created
    updated_by_user_id UUID REFERENCES users(id),   -- Who last updated
    created_at TIMESTAMP,
    updated_at TIMESTAMP
);

-- C# class
public class Product
{
    public Guid ID { get; set; }                    // → id
    public string Code { get; set; }                // → code
    public string Name { get; set; }                // → name
    public Guid CreatedByUserID { get; set; }       // → created_by_user_id
    public Guid? UpdatedByUserID { get; set; }      // → updated_by_user_id
    public DateTime CreatedAt { get; set; }         // → created_at
    public DateTime? UpdatedAt { get; set; }        // → updated_at
}
```

**Rationale:**
- C# `ProductID` is clearer than `ID` (ID of what?)
- C# `CreatedByUserID` is clearer than `CreatedBy` (created by what entity?)
- Database `product_id` follows PostgreSQL convention (snake_case)
- Self-documenting: no need to check FK constraints to understand relationships
- Consistent pattern: `{EntityName}ID` in C# → `{entity_name}_id` in database

```sql
-- ❌ INCORRECT - Generic or ambiguous names
CreatedBy UUID                      -- By what entity? Users? Systems?
product_id UUID                     -- C# side (should be ProductID in PascalCase)
Product_ID UUID                     -- Mixed case
PRODUCTID UUID                      -- All caps
ProductId UUID                      -- camelCase suffix (prefer ID)
```

### 2.4 Indexes

**Convention:** `ix_{table}_{column(s)}` or `uk_{table}_{column(s)}` (for unique) in snake_case

```sql
-- ✅ CORRECT (all snake_case)
CREATE INDEX ix_products_code ON products(code);
CREATE INDEX ix_products_name ON products(name);
CREATE INDEX ix_products_is_active ON products(is_active);
CREATE INDEX ix_orders_customer_id ON orders(customer_id);
CREATE INDEX ix_user_roles_user_id ON user_roles(user_id);

-- For multi-column indexes
CREATE INDEX ix_orders_customer_id_created_at ON orders(customer_id, created_at);

-- For unique indexes, use uk_ prefix
CREATE UNIQUE INDEX uk_products_code ON products(code);
CREATE UNIQUE INDEX uk_customers_email ON customers(email);

-- ❌ INCORRECT
CREATE INDEX ProductCodeIndex ON products(code);        -- PascalCase
CREATE INDEX idx_Products_Code ON products(code);       -- Mixed case
CREATE INDEX idx_orders_CustomerID ON orders(customer_id);  -- PascalCase column
```

### 2.5 Constraints

**Convention:** `{type}_{table}_{column(s)}` in snake_case

```sql
-- Primary Key
CONSTRAINT pk_products PRIMARY KEY (id)

-- Foreign Key
CONSTRAINT fk_orders_customers FOREIGN KEY (customer_id) REFERENCES customers(id)
CONSTRAINT fk_orders_products FOREIGN KEY (product_id) REFERENCES products(id)

-- Unique
CONSTRAINT uk_products_code UNIQUE (code)
CONSTRAINT uk_customers_email UNIQUE (email)

-- Check
CONSTRAINT chk_products_price_positive CHECK (price > 0)
CONSTRAINT chk_orders_quantity_positive CHECK (quantity > 0)
```

### 2.6 PostgreSQL Schemas

**Convention:** lowercase with underscores (snake_case)

```sql
-- ✅ CORRECT
CREATE SCHEMA authentication;
CREATE SCHEMA inventory;
CREATE SCHEMA sales;
CREATE SCHEMA accounting;
CREATE SCHEMA product_management;

-- ❌ INCORRECT
CREATE SCHEMA Authentication;           -- PascalCase
CREATE SCHEMA ProductManagement;        -- PascalCase
CREATE SCHEMA "product-management";     -- Hyphenated (prefer underscores)
```

**Schema-to-Service Mapping Example:**

| Microservice | Schema Name | Purpose |
|--------------|-------------|---------|
| AuthenticationService | `authentication` | Users, Roles, Permissions |
| InventoryService | `inventory` | Products, Warehouses, Stock |
| SalesService | `sales` | Customers, Orders, Invoices |
| AccountingService | `accounting` | Accounts, Ledgers, Transactions |

**EF Core Configuration:**

```csharp
protected override void OnModelCreating(ModelBuilder modelBuilder)
{
    // Set default schema for all entities in this context
    modelBuilder.HasDefaultSchema("inventory");

    // Configure specific entity table names
    modelBuilder.Entity<Product>(entity =>
    {
        entity.ToTable("products", "inventory");
    });

    // Apply snake_case naming to all entities
    modelBuilder.ApplySnakeCaseNaming();
}
```

### 2.7 Projection Tables (Cross-Service References)

**Convention:** C# class `{PREFIX}_{Entity}Prj`, database table `{prefix}_{origin_table_name}_prj` (snake_case)

**Purpose:** Tables that maintain eventual-consistent copies of data from other microservices for referential integrity without database-level foreign keys.

**Pattern:**
```
Prefix:       4 uppercase characters identifying the source service/module
C# Class:     {PREFIX}_{Entity}Prj (singular - class convention)
Database:     {prefix}_{origin_table_name}_prj (maintains origin table plurality)
```

**Rule:** The projection table name must maintain the same plurality (singular/plural) as the origin table it projects from.

**Prefix Examples:**
- `AUTH` - Authentication service
- `INVT` - Inventory service
- `SALE` - Sales service
- `ACCT` - Accounting service
- `PROD` - Product management service

**Examples:**

| Origin Table | Origin Schema | C# Class | Database Projection | Consumer Schema | Purpose |
|--------------|---------------|----------|---------------------|-----------------|---------|
| users | authentication | **AUTH_UserPrj** | **auth_users_prj** | accounting | Audit fields (created_by_user_id) |
| users | authentication | **AUTH_UserPrj** | **auth_users_prj** | inventory | Audit fields (created_by_user_id) |
| products | inventory | **INVT_ProductPrj** | **invt_products_prj** | sales | Product references (product_id) |
| customers | sales | **SALE_CustomerPrj** | **sale_customers_prj** | accounting | Customer references (customer_id) |
| accounts | accounting | **ACCT_AccountPrj** | **acct_accounts_prj** | sales | Account references (account_id) |

**SQL Schema Template:**

```sql
-- ✅ CORRECT: Projection table in consumer schema (snake_case with prefix, maintains origin plurality)
-- Schema: inventory (consuming users from authentication service)
-- Origin: users (plural) → Projection: auth_users_prj (plural)
CREATE TABLE auth_users_prj (
    id UUID PRIMARY KEY,
    code VARCHAR(50) NOT NULL,
    name VARCHAR(200) NOT NULL,
    is_active BOOLEAN NOT NULL,
    last_synced_at TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE INDEX ix_auth_users_prj_code ON auth_users_prj(code);
CREATE INDEX ix_auth_users_prj_is_active ON auth_users_prj(is_active);

-- Schema: sales (consuming products from inventory service)
-- Origin: products (plural) → Projection: invt_products_prj (plural)
CREATE TABLE invt_products_prj (
    id UUID PRIMARY KEY,
    code VARCHAR(50) NOT NULL,
    name VARCHAR(200) NOT NULL,
    price DECIMAL(18,2),
    is_active BOOLEAN NOT NULL,
    last_synced_at TIMESTAMP NOT NULL DEFAULT NOW()
);

-- ❌ INCORRECT: Old naming conventions
CREATE TABLE UsersPrj (...);                -- PascalCase (wrong)
CREATE TABLE user_projection (...);         -- Too verbose (wrong)
CREATE TABLE users_prj (...);               -- Missing prefix (wrong)
CREATE TABLE auth_user_prj (...);           -- Wrong plurality (origin is plural 'users')
CREATE TABLE AUTH_UsersPrj (...);           -- PascalCase in DB (wrong)
CREATE TABLE authUserPrj (...);             -- camelCase (wrong)
```

**C# Entity Example:**

```csharp
// ✅ CORRECT: C# class uses PREFIX_EntityPrj pattern
public class AUTH_UserPrj
{
    public Guid ID { get; set; }
    public string Code { get; set; } = null!;
    public string Name { get; set; } = null!;
    public bool IsActive { get; set; }
    public DateTime LastSyncedAt { get; set; }
}

public class INVT_ProductPrj
{
    public Guid ID { get; set; }
    public string Code { get; set; } = null!;
    public string Name { get; set; } = null!;
    public decimal Price { get; set; }
    public bool IsActive { get; set; }
    public DateTime LastSyncedAt { get; set; }
}

// DbContext with explicit table mapping
public DbSet<AUTH_UserPrj> AUTH_UserPrj => Set<AUTH_UserPrj>();
public DbSet<INVT_ProductPrj> INVT_ProductPrj => Set<INVT_ProductPrj>();

protected override void OnModelCreating(ModelBuilder modelBuilder)
{
    modelBuilder.Entity<AUTH_UserPrj>(entity =>
    {
        // Table name maintains origin table plurality (users → auth_users_prj)
        entity.ToTable("auth_users_prj", "inventory");
        // Column mappings applied automatically via SnakeCaseNamingConvention
    });

    modelBuilder.Entity<INVT_ProductPrj>(entity =>
    {
        // Table name maintains origin table plurality (products → invt_products_prj)
        entity.ToTable("invt_products_prj", "sales");
    });
}
```

**Synchronization:**
- Via domain events (message bus): `UserCreated`, `UserUpdated`, `ProductUpdated`
- Eventual consistency model
- No database-level FK constraints
- Application-level validation before insert

**Usage in Business Tables:**

```sql
-- Business table references projection (no FK constraint)
CREATE TABLE orders (
    id UUID PRIMARY KEY DEFAULT uuidv7(),
    customer_id UUID NOT NULL,                  -- References sale_customers_prj.id (no FK)
    created_by_user_id UUID NOT NULL,           -- References auth_users_prj.id (no FK)
    amount DECIMAL(18,2) NOT NULL,
    created_at TIMESTAMP DEFAULT NOW()
);

-- Validation in application layer before insert:
-- 1. Check sale_customers_prj
-- 2. Check auth_users_prj
-- 3. Then insert order
```

**Rationale:**
- **4-char prefix:** Identifies source service/module clearly (`AUTH`, `INVT`, `SALE`, `ACCT`)
- **`Prj` suffix in C#:** Short (3 chars), recognizable abbreviation for "Projection"
- **Brevity over verbosity:** `AUTH_UserPrj` preferred over `AuthenticationUserProjection`
- **snake_case in database:** Consistent with PostgreSQL standard
- **Maintains origin plurality:** `users` → `auth_users_prj`, `products` → `invt_products_prj` (clear relationship to origin)
- **Direct mapping:** Visual consistency between origin and projection (`users` ↔ `auth_users_prj`)
- **Self-documenting:** Clear distinction from origin table via prefix + `_prj` suffix
- **Namespace isolation:** Prefix prevents naming collisions across services
- **Query clarity:** Queries clearly show which origin table is being referenced

**Plurality Examples:**

```csharp
// With Pluralization Enabled (origin tables are plural)
Origin: users (plural) → Projection: auth_users_prj (plural)
Origin: products (plural) → Projection: invt_products_prj (plural)
Origin: categories (plural) → Projection: acct_categories_prj (plural)

// With Pluralization Disabled (origin tables are singular)
Origin: user (singular) → Projection: auth_user_prj (singular)
Origin: product (singular) → Projection: invt_product_prj (singular)
Origin: category (singular) → Projection: acct_category_prj (singular)
```

**Key Principle:** Always mirror the origin table's plurality in the projection table name for maximum clarity and consistency.

---

## 3. TypeScript Frontend Conventions

### 3.1 Interfaces and Types

**Convention:** PascalCase for interface/type names, camelCase for properties

```typescript
// ✅ CORRECT
interface Product {
  id: string;                   // UUID as string
  code: string;                 // Business identifier
  name: string;
  price: number;
  isActive: boolean;
  createdAt: string;            // ISO date string from API
  createdByUserId: string;      // FK reference
}

interface APIConfiguration {
  id: string;
  apiKey: string;               // Acronym in camelCase
  httpEndpoint: string;
  xmlContent: string;
  jsonPayload: object;
}

type ProductResponse = {
  data: Product[];
  total: number;
  page: number;
};

// ❌ INCORRECT
interface product { }                   // camelCase interface name
interface Product {
  ID: string;                           // PascalCase property (wrong for TS)
  created_at: string;                   // Snake_Case (wrong for TS)
  ApiKey: string;                       // PascalCase (wrong for TS)
}
```

### 3.2 React Components

**Convention:** PascalCase for component names and files

```typescript
// File: ProductSelector.tsx
// ✅ CORRECT
export function ProductSelector({ onSelect }: Props) {
  const [selectedProduct, setSelectedProduct] = useState<Product | null>(null);

  const handleProductChange = (product: Product) => {
    setSelectedProduct(product);
    onSelect(product.id);
  };

  return <Autocomplete ... />;
}

// ❌ INCORRECT
export function productSelector() { }      // camelCase component
export function Product_Selector() { }     // Snake_Case
```

### 3.3 Functions and Variables

**Convention:** camelCase

```typescript
// ✅ CORRECT
const getProductByCode = async (code: string): Promise<Product> => {
  const response = await apiClient.get(`/api/products/by-code/${code}`);
  return response.data;
};

function validatePrice(price: number): boolean {
  return price > 0;
}

const currentUser = await getCurrentUser();
const orderTotal = calculateTotal(items);

// ❌ INCORRECT
const GetProductByCode = async () => { };       // PascalCase function
const get_product_by_code = async () => { };    // Snake_Case
const CurrentUser = await getCurrentUser();     // PascalCase variable
```

### 3.4 Constants

**Convention:** UPPER_SNAKE_CASE (same as C#)

```typescript
// ✅ CORRECT
const MAX_RETRY_ATTEMPTS = 3;
const DEFAULT_TIMEOUT_SECONDS = 30;
const DEFAULT_CURRENCY = 'USD';
const API_VERSION = 'v1';
const TAX_RATE = 0.16;
const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL;
const CACHE_EXPIRATION_MS = 300000;
const ALLOWED_FILE_TYPES = ['pdf', 'jpg', 'png'];

// ❌ INCORRECT
const maxRetryAttempts = 3;                 // camelCase (not clear it's constant)
const MaxRetryAttempts = 3;                 // PascalCase
const max_retry_attempts = 3;               // lowercase
const Api_Version = 'v1';                   // Mixed case
```

### 3.5 Enums

**Convention:** PascalCase for enum name and keys (same as C#)

**Note:** Enum values (the assigned values) are not part of this standard - they can be determined by project requirements.

```typescript
// ✅ CORRECT - Enum names and keys in PascalCase
enum OrderStatus {
  Pending = 'PENDING',      // Key: PascalCase ✅, Value: project choice
  Approved = 'APPROVED',
  Rejected = 'REJECTED',
  Cancelled = 'CANCELLED'
}

enum PaymentMethod {
  CreditCard = 'credit_card',
  DebitCard = 'debit_card',
  BankTransfer = 'bank_transfer'
}

enum UserRole {
  Admin = 1,
  Manager = 2,
  User = 3
}

// ❌ INCORRECT
enum orderStatus { }                        // camelCase enum name
enum OrderStatus {
  PENDING = 'PENDING',                      // UPPER_CASE key (wrong)
  APPROVED = 'APPROVED'
}
enum OrderStatus { pending, approved }      // lowercase keys (wrong)
```

### 3.6 File Names

**Convention:**
- Components: PascalCase (`.tsx`)
- Utilities: camelCase or kebab-case (`.ts`)
- Types: camelCase or kebab-case (`.ts`)

```
✅ CORRECT
components/
  ProductSelector.tsx
  OrderForm.tsx
  CustomerList.tsx

utils/
  apiClient.ts
  formatCurrency.ts
  validation.ts

types/
  product.ts
  order.ts
  api-responses.ts

❌ INCORRECT
components/
  productSelector.tsx          // camelCase component file
  product_selector.tsx         // Snake_Case
```

---

## 4. EF Core Mapping Strategy

### 4.1 Strategy: Automatic snake_case Conversion

**Decision:** C# classes use idiomatic PascalCase, PostgreSQL uses idiomatic snake_case. EF Core automatically converts between them via `SnakeCaseNamingConvention`.

**Benefits:**
- ✅ Idiomatic C# code (PascalCase properties)
- ✅ PostgreSQL standard naming (snake_case columns)
- ✅ Zero manual `[Column]` or `[Table]` attributes needed
- ✅ Handles acronyms correctly (APIKey → api_key, HTTPClient → http_client)
- ✅ Single source of truth (C# classes define structure)

**Implementation:**

```csharp
// File: Shared/EntityFramework/SnakeCaseNamingConvention.cs
public static class SnakeCaseNamingConvention
{
    public static string ToSnakeCase(string input)
    {
        if (string.IsNullOrEmpty(input)) return input;

        // Handle acronyms and PascalCase correctly:
        // ID → id, APIKey → api_key, CreatedAt → created_at, HTTPClient → http_client
        var snakeCase = Regex.Replace(input, "([a-z0-9])([A-Z])", "$1_$2");
        snakeCase = Regex.Replace(snakeCase, "([A-Z]+)([A-Z][a-z])", "$1_$2");
        return snakeCase.ToLowerInvariant();
    }

    public static void ApplySnakeCaseNaming(this ModelBuilder modelBuilder)
    {
        foreach (var entity in modelBuilder.Model.GetEntityTypes())
        {
            // Convert table names: Product → product (or products if pluralization enabled)
            entity.SetTableName(ToSnakeCase(entity.GetTableName()));

            // Convert column names: CreatedAt → created_at
            foreach (var property in entity.GetProperties())
            {
                property.SetColumnName(ToSnakeCase(property.Name));
            }

            // Convert indexes: ix_Product_Code → ix_product_code
            foreach (var index in entity.GetIndexes())
            {
                var prefix = index.IsUnique ? "uk_" : "ix_";
                var tableName = ToSnakeCase(entity.GetTableName());
                var columnNames = string.Join("_", index.Properties.Select(p => ToSnakeCase(p.Name)));
                index.SetDatabaseName($"{prefix}{tableName}_{columnNames}");
            }

            // Convert FK constraints: fk_Order_Customer → fk_order_customer
            foreach (var foreignKey in entity.GetForeignKeys())
            {
                var dependentTable = ToSnakeCase(foreignKey.DeclaringEntityType.GetTableName());
                var principalTable = ToSnakeCase(foreignKey.PrincipalEntityType.GetTableName());
                foreignKey.SetConstraintName($"fk_{dependentTable}_{principalTable}");
            }
        }
    }
}
```

**Example Mapping:**

```csharp
// C# Entity (idiomatic PascalCase)
public class Product
{
    public Guid ID { get; set; }                // → id
    public string Code { get; set; }            // → code
    public string Name { get; set; }            // → name
    public decimal Price { get; set; }          // → price
    public bool IsActive { get; set; }          // → is_active
    public DateTime CreatedAt { get; set; }     // → created_at
    public Guid CreatedByUserID { get; set; }   // → created_by_user_id
    public string APIKey { get; set; }          // → api_key
    public string HTTPEndpoint { get; set; }    // → http_endpoint
}

// PostgreSQL Table (PostgreSQL standard snake_case) - GENERATED AUTOMATICALLY
CREATE TABLE products (  -- or 'product' if pluralization disabled
  id UUID PRIMARY KEY DEFAULT uuidv7(),
  code VARCHAR(50) NOT NULL,
  name VARCHAR(200) NOT NULL,
  price DECIMAL(18,2) NOT NULL,
  is_active BOOLEAN NOT NULL,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  created_by_user_id UUID NOT NULL REFERENCES users(id),
  api_key VARCHAR(100),
  http_endpoint VARCHAR(500)
);

CREATE UNIQUE INDEX uk_products_code ON products(code);
CREATE INDEX ix_products_is_active ON products(is_active);
```

### 4.2 DbContext Configuration

**CRITICAL:** Apply snake_case naming **AFTER** all entity configurations:

```csharp
// Example DbContext
public class ApplicationDbContext : DbContext
{
    protected override void OnModelCreating(ModelBuilder modelBuilder)
    {
        // Set schema
        modelBuilder.HasDefaultSchema("inventory");

        // Configure entities (explicit table naming)
        modelBuilder.Entity<Product>(entity =>
        {
            // Explicit snake_case table name
            // Use "products" if pluralization enabled, "product" if disabled
            entity.ToTable("products", "inventory");

            entity.HasKey(e => e.ID);

            entity.Property(e => e.Code).IsRequired().HasMaxLength(50);
            entity.HasIndex(e => e.Code).IsUnique();

            entity.Property(e => e.Price).HasPrecision(18, 2);
        });

        // CRITICAL: Apply snake_case naming LAST
        modelBuilder.ApplySnakeCaseNaming();
    }
}
```

**Why apply last?** The convention needs to process all configured entities, indexes, and constraints.

### 4.3 When to Use [Column] or [Table] Attributes

**Short answer: RARELY**

The `SnakeCaseNamingConvention` handles all mapping automatically. Manual attributes are:
- ❌ Usually not needed
- ❌ Can create inconsistency
- ❌ Bypass the convention
- ❌ Increase maintenance burden

```csharp
// ❌ INCORRECT - Don't use manual attributes (convention handles this)
public class Product
{
    [Column("price")]  // WRONG - convention handles this
    public decimal Price { get; set; }

    [Table("products")]  // WRONG - use ToTable() in OnModelCreating instead
}

// ✅ CORRECT - Let convention handle everything
public class Product
{
    public decimal Price { get; set; }  // → price automatically
}
```

**Exception:** If you legitimately need a database column name that doesn't follow snake_case (e.g., legacy integration), document it clearly and use `[Column]` with a comment explaining why.

---

## 5. API Endpoint Conventions

### 5.1 URL Paths

**Convention:** kebab-case, lowercase

```
✅ CORRECT
GET  /api/v1/products
GET  /api/v1/products/{id}
GET  /api/v1/products/by-code/{code}
POST /api/v1/products
PUT  /api/v1/products/{id}
DELETE /api/v1/products/{id}
GET  /api/v1/orders/customer/{customerId}

❌ INCORRECT
GET  /api/v1/Products                   // PascalCase
GET  /api/v1/products_list              // Snake_Case
GET  /api/v1/ProductsList               // No separators
GET  /api/v1/products/byCode/{code}     // camelCase in path
```

### 5.2 Query Parameters

**Convention:** camelCase

```
✅ CORRECT
GET /api/v1/products?companyId=xxx&includeInactive=true
GET /api/v1/orders?customerId=xxx&startDate=2024-01-01&endDate=2024-12-31

❌ INCORRECT
GET /api/v1/products?CompanyId=xxx          // PascalCase
GET /api/v1/products?company_id=xxx         // Snake_Case
GET /api/v1/products?Company-Id=xxx         // kebab-case
```

### 5.3 JSON Response Keys

**Convention:** camelCase (standard for JSON)

```json
// ✅ CORRECT
{
  "id": "a7b3c4d5-e6f7-8a9b-0c1d-2e3f4a5b6c7d",
  "code": "PROD-001",
  "name": "Premium Widget",
  "price": 99.99,
  "isActive": true,
  "createdAt": "2025-01-15T10:30:00Z",
  "createdByUserId": "b8c4d5e6-f7a8-9b0c-1d2e-3f4a5b6c7d8e"
}

// ❌ INCORRECT
{
  "ID": "...",                    // PascalCase (C# convention, wrong for JSON)
  "Code": "PROD-001",             // PascalCase
  "price": 99.99,                 // ✅ OK
  "is_active": true,              // Snake_Case (Python convention, wrong for JSON)
  "created_at": "2025-01-15..."   // Snake_Case
}
```

### 5.4 C# → JSON Serialization

**Configuration:** Use `System.Text.Json` with camelCase naming policy

```csharp
// Program.cs or Startup.cs
builder.Services.ConfigureHttpJsonOptions(options =>
{
    options.SerializerOptions.PropertyNamingPolicy = JsonNamingPolicy.CamelCase;
    options.SerializerOptions.DictionaryKeyPolicy = JsonNamingPolicy.CamelCase;
});

// Result: Price → price, IsActive → isActive in JSON automatically
```

---

## 6. Special Cases and Guidelines

### 6.1 Acronyms in Property Names

**Convention:** Full acronyms in uppercase (3+ letters) when using PascalCase

```csharp
// ✅ CORRECT
public string APIKey { get; set; }              // API (3 letters, all caps)
public string HTTPClient { get; set; }          // HTTP (4 letters, all caps)
public string XMLDocument { get; set; }         // XML (3 letters, all caps)
public string JSONPayload { get; set; }         // JSON (4 letters, all caps)
public string URLPath { get; set; }             // URL (3 letters, all caps)
public string HTMLContent { get; set; }         // HTML (4 letters, all caps)
public int HTTPStatusCode { get; set; }         // HTTP (all caps)

// Special cases (2 letters)
public string ID { get; set; }                  // 2 letters: all caps
public Guid ID { get; set; }                    // Primary key: all caps

// ❌ INCORRECT
public string ApiKey { get; set; }              // Should be APIKey
public string HttpClient { get; set; }          // Should be HTTPClient
public string XmlDocument { get; set; }         // Should be XMLDocument
```

**Database Mapping:**
```csharp
// C# → PostgreSQL
APIKey          → api_key
HTTPClient      → http_client
XMLDocument     → xml_document
JSONPayload     → json_payload
HTTPStatusCode  → http_status_code
```

### 6.2 Boolean Properties

**Convention:** Use `Is`, `Has`, `Can` prefix

```csharp
// ✅ CORRECT
public bool IsActive { get; set; }
public bool IsDeleted { get; set; }
public bool HasPermission { get; set; }
public bool CanModify { get; set; }
public bool IsEnabled { get; set; }

// ❌ INCORRECT
public bool Active { get; set; }                // Missing Is prefix
public bool Deleted { get; set; }               // Missing Is prefix
public bool Permission { get; set; }            // Missing Has prefix
```

### 6.3 Collection Properties

**Convention:** Plural noun

```csharp
// ✅ CORRECT
public List<Product> Products { get; set; }
public ICollection<Order> Orders { get; set; }
public string[] AllowedOperations { get; set; }
public HashSet<string> Tags { get; set; }

// ❌ INCORRECT
public List<Product> ProductList { get; set; }  // Don't add "List" suffix
public List<Product> Product { get; set; }      // Should be plural
```

### 6.4 Async Method Naming

**Convention:** Add `Async` suffix to async methods

```csharp
// ✅ CORRECT
public async Task<Product> GetProductAsync(Guid id) { }
public async Task<bool> SaveChangesAsync() { }
public async Task DeleteAsync(Guid id) { }

// ❌ INCORRECT
public async Task<Product> GetProduct(Guid id) { }     // Missing Async suffix
public async Task<Product> GetProductAsynchronous(Guid id) { }  // Too verbose
```

### 6.5 DateTime Properties

**Convention:** Use descriptive suffixes (`At`, `On`, `Date`)

```csharp
// ✅ CORRECT
public DateTime CreatedAt { get; set; }         // Timestamp
public DateTime UpdatedAt { get; set; }         // Timestamp
public DateTime DeletedAt { get; set; }         // Timestamp (soft delete)
public DateTime PublishedAt { get; set; }       // Timestamp
public DateOnly BirthDate { get; set; }         // Date only
public DateOnly DueDate { get; set; }           // Date only

// ❌ INCORRECT
public DateTime Created { get; set; }           // Missing At suffix
public DateTime Update { get; set; }            // Missing At suffix, wrong tense
public DateTime Creation { get; set; }          // Use CreatedAt instead
```

---

## 7. Summary Table

| Layer | Elements | Convention | C# Example | PostgreSQL Example | TypeScript Example |
|-------|----------|------------|------------|--------------------|--------------------|
| **C#** | Classes, Interfaces | PascalCase | `Product`, `IProductService`, `APIClient` | - | - |
| **C#** | Methods | PascalCase (verb) | `GetByIdAsync`, `ValidateOrder` | - | - |
| **C#** | Properties | PascalCase | `CreatedAt`, `ProductID`, `APIKey` | → `created_at`, `product_id`, `api_key` | - |
| **C#** | Primary Key (Guid) | `ID` | `public Guid ID` | → `id` | - |
| **C#** | Business ID (string) | `Code` | `public string Code` | → `code` | - |
| **C#** | Foreign Keys | `{Entity}ID` | `CustomerID`, `ProductID` | → `customer_id`, `product_id` | - |
| **C#** | Audit Fields | `{Action}ByUserID` | `CreatedByUserID` | → `created_by_user_id` | - |
| **C#** | Parameters, variables | camelCase | `productId`, `unitPrice` | - | - |
| **C#** | Private fields | `_camelCase` | `_httpClient`, `_apiUrl` | - | - |
| **C#** | Constants | UPPER_SNAKE_CASE | `MAX_RETRY_ATTEMPTS` | - | - |
| **PostgreSQL** | Schemas | snake_case | - | `authentication`, `inventory` | - |
| **PostgreSQL** | Tables | snake_case (plural/singular) | `Product` | → `products` or `product` | - |
| **PostgreSQL** | Columns | snake_case | `IsActive`, `APIKey` | → `is_active`, `api_key` | - |
| **PostgreSQL** | Foreign Keys | `{entity}_id` | `ProductID` | → `product_id` | - |
| **PostgreSQL** | Indexes (unique) | `uk_{table}_{column}` | - | `uk_products_code` | - |
| **PostgreSQL** | Indexes (non-unique) | `ix_{table}_{column}` | - | `ix_products_is_active` | - |
| **PostgreSQL** | Primary Keys | `pk_{table}` | - | `pk_products` | - |
| **PostgreSQL** | FK Constraints | `fk_{dep}_{prin}` | - | `fk_orders_customers` | - |
| **PostgreSQL** | Projections | `{prefix}_{origin_table}_prj` | `AUTH_UserPrj` | → `auth_users_prj` (plural from origin) | - |
| **TypeScript** | Interfaces, Types | PascalCase | - | - | `Product`, `APIConfig` |
| **TypeScript** | Properties | camelCase | - | - | `isActive`, `apiKey` |
| **TypeScript** | Functions, variables | camelCase | - | - | `getProduct`, `currentUser` |
| **TypeScript** | Components | PascalCase | - | - | `ProductSelector` |
| **TypeScript** | Constants | UPPER_SNAKE_CASE | - | - | `MAX_RETRY_ATTEMPTS` |
| **TypeScript** | Enums | PascalCase (name & keys) | - | - | `OrderStatus { Pending, Approved }` |
| **API** | Endpoints | kebab-case | - | - | `/api/v1/products` |
| **API** | Query params | camelCase | - | - | `?customerId=xxx` |
| **JSON** | Keys | camelCase | - | - | `"isActive": true` |

**Key Insight:** Each layer uses its idiomatic convention. C# uses PascalCase/camelCase, PostgreSQL uses snake_case, TypeScript/JSON uses camelCase. EF Core `SnakeCaseNamingConvention` bridges them automatically.

---

## 8. Implementation Checklist

### For New Projects

**Step 1: Create SnakeCaseNamingConvention**
```csharp
// File: Shared/EntityFramework/SnakeCaseNamingConvention.cs
// Implement ToSnakeCase() with proper acronym handling
// Provide ApplySnakeCaseNaming() extension method for ModelBuilder
```

**Step 2: Configure DbContext**
```csharp
protected override void OnModelCreating(ModelBuilder modelBuilder)
{
    modelBuilder.HasDefaultSchema("your_schema");

    // Configure entities with explicit snake_case table names
    modelBuilder.Entity<Product>(entity =>
    {
        entity.ToTable("products", "your_schema");  // or "product" if pluralization disabled
        entity.Property(e => e.Code).IsRequired();
    });

    // CRITICAL: Apply snake_case naming LAST
    modelBuilder.ApplySnakeCaseNaming();
}
```

**Step 3: Configure JSON Serialization**
```csharp
// Program.cs
builder.Services.ConfigureHttpJsonOptions(options =>
{
    options.SerializerOptions.PropertyNamingPolicy = JsonNamingPolicy.CamelCase;
});
```

**Step 4: Generate Migrations**
```bash
# Generate migration
dotnet ef migrations add InitialCreate --project YourProject

# Verify migration uses snake_case
# Check: tables are lowercase with underscores
# Check: columns are lowercase with underscores

# Apply to database
dotnet ef database update --project YourProject
```

**Step 5: Configure Linters**
- C#: EditorConfig + StyleCop
- TypeScript: ESLint with naming conventions
- SQL: pg_format or SQLFluff

### For Existing Projects

**Migration Strategy:**
1. Assess current naming patterns
2. Create snake_case conversion strategy
3. Generate new migrations with updated naming
4. Test thoroughly before deployment
5. Update all queries and raw SQL to use snake_case
6. Update documentation

---

## 9. Tooling and Enforcement

### 9.1 C# - EditorConfig

```ini
# .editorconfig
[*.cs]
# Naming rules
dotnet_naming_rule.interfaces_should_be_pascal_case_prefixed_with_i.severity = warning
dotnet_naming_rule.interfaces_should_be_pascal_case_prefixed_with_i.symbols = interface
dotnet_naming_rule.interfaces_should_be_pascal_case_prefixed_with_i.style = pascal_case_prefixed_with_i

dotnet_naming_rule.constants_should_be_upper_snake_case.severity = warning
dotnet_naming_rule.constants_should_be_upper_snake_case.symbols = constant
dotnet_naming_rule.constants_should_be_upper_snake_case.style = upper_snake_case

# Styles
dotnet_naming_style.upper_snake_case.capitalization = all_upper
dotnet_naming_style.upper_snake_case.word_separator = _

dotnet_naming_style.pascal_case_prefixed_with_i.required_prefix = I
dotnet_naming_style.pascal_case_prefixed_with_i.capitalization = pascal_case
```

### 9.2 TypeScript - ESLint

```json
// .eslintrc.json
{
  "rules": {
    "@typescript-eslint/naming-convention": [
      "error",
      {
        "selector": "interface",
        "format": ["PascalCase"]
      },
      {
        "selector": "variable",
        "format": ["camelCase", "UPPER_CASE"]
      },
      {
        "selector": "function",
        "format": ["camelCase"]
      },
      {
        "selector": "typeLike",
        "format": ["PascalCase"]
      }
    ]
  }
}
```

### 9.3 SQL - pg_format

```bash
# Format SQL files with snake_case
pg_format --function-case 2 --keyword-case 2 --spaces 2 migration.sql
```

---

## 10. Consequences

### Positive

✅ **Consistency**: Single, clear convention for each language
✅ **No mapping overhead**: Automatic conversion between C# and PostgreSQL
✅ **Readability**: Each language uses its idiomatic conventions
✅ **Maintainability**: Easy to know which convention to use
✅ **Team efficiency**: No debates about naming during code review
✅ **Tooling friendly**: Standard conventions work with linters, formatters
✅ **Scalability**: Clear patterns for microservices and cross-service projections

### Considerations

⚠️ **Learning curve**: Team must learn conventions initially
⚠️ **Migration effort**: Existing projects need careful migration planning
⚠️ **Convention consistency**: Must apply `ApplySnakeCaseNaming()` in all DbContexts

### Mitigations

- Use linters and automated tooling
- Include naming convention checks in code review
- Provide templates for new entities/components
- Keep this document visible and updated
- Run automated tests to verify naming consistency

---

## 11. References

- [C# Naming Guidelines (Microsoft)](https://learn.microsoft.com/en-us/dotnet/csharp/fundamentals/coding-style/identifier-names)
- [PostgreSQL Naming Conventions](https://www.postgresql.org/docs/current/sql-syntax-lexical.html#SQL-SYNTAX-IDENTIFIERS)
- [TypeScript Style Guide (Google)](https://google.github.io/styleguide/tsguide.html)
- [REST API Naming Conventions](https://restfulapi.net/resource-naming/)
- [JSON Naming Convention](https://google.github.io/styleguide/jsoncstyleguide.xml)

---

## Document History

- **2025-12-04 (Version 1.5):** Added acronym capitalization rule
  - **CLARITY FIX:** Added new Section 1.1 "Acronym Capitalization Rule"
  - Establishes that all acronyms must be written in full uppercase (ID, API, HTTP, XML, JSON, etc.)
  - Applies to all PascalCase identifiers: properties, classes, methods, interfaces
  - Renumbered all subsections in Section 1 (1.1 Namespaces → 1.2, etc.)
  - Examples: APIKey, HTTPClient, XMLParser, ERPService (not ApiKey, HttpClient, etc.)
  - Rationale: Visual consistency, improved readability, industry-standard convention

- **2025-12-04 (Version 1.4):** Enhanced foreign key naming conventions
  - **CLARITY & COMPLETENESS FIX:** Improved Section 2.3 foreign key naming
  - Renamed "Business Entity Foreign Keys" → "Foreign Keys" (clearer terminology)
  - Renamed "Audit Field Foreign Keys" → "Audit Foreign Keys" (simplified)
  - Added new subsection: "Multiple References to Same Entity"
  - New pattern: `{Context}{EntityName}ID` in C# → `{context}_{entity_name}_id` in DB
  - Added comprehensive examples: Shipments, Transfers, Transactions
  - Documented common context prefixes: Origin/Destination, Source/Destination, Sender/Receiver, etc.
  - Rationale: Handles multiple FKs to same entity with clear, self-documenting naming

- **2025-12-04 (Version 1.3):** Corrected parameter naming in examples
  - **CLARITY FIX:** Updated Section 1.7 examples to use consistent parameter naming
  - Changed `GetProductAsync(Guid productId, string companyCode)` to use proper ID conventions
  - Added alternative example: `GetByCodeAsync(string code, Guid companyId)`
  - Clarified that parameters use `id` (not `productId`) and `code` (not `productCode`) when unambiguous
  - When multiple entities involved, use `{entity}Id` pattern (e.g., `companyId`, `productId`)
  - Rationale: Consistency with property names (`ID`, `Code`) and clarity in parameters

- **2025-12-04 (Version 1.2):** Standardized TypeScript enum naming
  - **CONSISTENCY FIX:** TypeScript enums now use PascalCase for names and keys (matching C#)
  - Added new Section 3.5 for TypeScript Enums with clear examples
  - Enum values are explicitly not part of the standard (project choice)
  - Renumbered Section 3.5 (File Names) to 3.6
  - Updated Summary Table (Section 7) to include TypeScript enum convention
  - Rationale: Maintains consistency between C# and TypeScript enum naming

- **2025-12-04 (Version 1.1):** Corrected projection table plurality rule
  - **CRITICAL FIX:** Projection tables now maintain origin table plurality
  - Changed pattern from `{prefix}_{entity}_prj` to `{prefix}_{origin_table_name}_prj`
  - Example: `users` → `auth_users_prj` (not `auth_user_prj`)
  - Updated Section 2.7 with clear plurality examples (plural and singular)
  - Added "Key Principle" to emphasize mirroring origin table plurality
  - Updated all SQL examples and C# DbContext configurations
  - Updated Summary Table (Section 7) to reflect correct convention
  - Rationale: Maintains clear relationship to origin table, improves query clarity

- **2025-12-04 (Version 1.0):** Initial general standards document created
  - Based on project-specific ADR 004
  - Generalized for any C#/PostgreSQL/TypeScript project
  - Changed `UUID` to `ID` for Guid identifiers
  - Changed string `ID` to `Code` for business identifiers
  - Updated acronym handling to keep full uppercase (APIKey, HTTPClient, etc.)
  - Added 4-character prefix requirement for projection tables
  - Standardized constants to UPPER_SNAKE_CASE in both C# and TypeScript
  - Made EF Core pluralization configurable (project-specific choice)
  - Included comprehensive examples across all three languages

---

**End of Document**
