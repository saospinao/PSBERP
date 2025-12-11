# Siesa Business ERP Product Requirements Document (PRD)

## Goals and Background Context

### Goals

*   To launch an MVP within 3 months that validates the core purchase and sales workflow.
*   To create a foundational platform for future module integration, starting with Sales and Purchasing.
*   To achieve successful adoption by at least one pilot customer who can run their core sales and purchasing cycle on the platform.

### Background Context

Based on our Project Brief, Siesa Business ERP aims to solve the problem of operational inefficiency caused by fragmented systems in Small to Medium-Sized Enterprises (SMEs). The current market relies on a patchwork of tools, leading to data silos, manual errors, and a lack of real-time visibility.

This PRD focuses specifically on an aggressive 3-month MVP designed to deliver the most critical value first. The scope is tightly focused on two core workflows: sales order management and purchase order management. By delivering this "tracer bullet" functionality, we aim to validate the core architecture and value proposition with a pilot customer before expanding to other modules like finance, inventory, and HR.

### Change Log

| Date       | Version | Description     | Author |
| :--------- | :------ | :-------------- | :----- |
| 2025-12-11 | 1.0     | Initial draft   | John   |

## Requirements

*A notable outcome of our Agile Team review is the consensus that detailed Acceptance Criteria will be defined for each functional requirement during the story-writing phase to ensure testability.*

### Functional
*   **FR1: User Management:** Users must be able to log in and log out. The system must support at least two roles: `Sales Agent` and `Purchasing Agent`, with permissions strictly limited to their respective modules.
*   **FR2: Customer Management (Minimal):** A `Sales Agent` must be able to create, view, and select a customer when creating a sales order.
*   **FR3: Supplier Management (Minimal):** A `Purchasing Agent` must be able to create, view, and select a supplier when creating a purchase order.
*   **FR4: Product Management (Minimal):** A user must be able to create and view basic products/services with a name and a standard price. This catalog will be used in both sales and purchase orders.
*   **FR5: Sales Order Creation:** A `Sales Agent` must be able to create a new sales order, associate it with a customer, and add line items by selecting from the product catalog.
*   **FR6: Purchase Order Creation:** A `Purchasing Agent` must be able to create a new purchase order, associate it with a supplier, and add line items by selecting from the product catalog.
*   **FR7: Order Management:** Users must be able to view a list of all sales and purchase orders. Each order must have a status (`Open`, `Completed`, `Cancelled`). Users must be able to change the status of an order.

### Non Functional
*   **NFR1: Usability:** A new user's ability to create a sales or purchase order will be validated via a timed, script-based usability test. The task must be completed in under 5 minutes.
*   **NFR2: Performance:** Core pages (like order lists or creation forms) must load in under 3 seconds with up to 1,000 records in the database and 10 concurrent users.
*   **NFR3: Security:** All user data must be encrypted in transit and at rest. Role-based access control must be strictly enforced at the API level.
*   **NFR4: Scalability:** The architecture must use a modular monolith pattern, with clear separation of concerns between the Sales and Purchasing modules at the code level, to facilitate future extraction into microservices if needed.

## User Interface Design Goals

### Overall UX Vision
The user experience will be clean, efficient, and data-driven. The primary goal is to enable users (Sales and Purchasing agents) to complete their core tasks—creating and managing orders—with minimal friction and cognitive load. The interface should feel professional, responsive, and reliable.

### Key Interaction Paradigms
The UI will be built on standard, well-understood web conventions:
*   **Data Entry:** Standard forms with clear labels, input validation, and dropdowns/searchable selects for entities like customers, suppliers, and products.
*   **Data Display:** Sortable and filterable tables for lists of orders, customers, etc.
*   **Actions:** Key actions will be represented by clearly labeled buttons. Critical actions (e.g., 'Cancel Order') will use confirmation modals to prevent errors.

### Core Screens and Views
Based on our functional requirements, the following conceptual screens are necessary for the MVP:
*   Login Screen
*   Main Dashboard (displaying KPIs for Sales and Purchasing)
*   Sales Order List
*   Sales Order Create/View/Edit Page
*   Purchase Order List
*   Purchase Order Create/View/Edit Page
*   Customer List & Management Page
*   Supplier List & Management Page
*   Product List & Management Page

### Accessibility: WCAG AA
The application should adhere to the Web Content Accessibility Guidelines (WCAG) 2.1 Level AA as a standard to ensure it is usable by people with a wide range of disabilities.

### Branding
The UI must incorporate the existing "Siesa" corporate branding. This includes using the official logos (e.g., `Siesa_Logosimbolo_Azul.svg`), color palette, and any specified typography.

### Target Device and Platforms: Web Responsive
The application will be a responsive web app, designed with a "desktop-first" approach but ensuring full functionality on tablet devices. Mobile phone access will be for viewing data, with complex data entry tasks optimized for larger screens.

## Technical Assumptions

### Repository Structure: Monorepo
We will use a monorepo, managed with a tool like **Nx or Turborepo**, to house the code for all microservices. This will centralize build processes and dependency management.

### Service Architecture
The MVP will be built using a **Microservices architecture**. The Sales and Purchasing modules will be developed as independent services from the start. This approach increases upfront complexity and infrastructure overhead but provides maximum long-term scalability and team autonomy. Communication between services will be handled via well-defined REST APIs for synchronous queries and a **Pub/Sub** mechanism for asynchronous events.

### Testing Requirements
The project will require a combination of **Unit and Integration tests**. Additionally, at least one automated **End-to-End (E2E) "happy path" test** will be created for the complete sales order flow and the complete purchase order flow.

### Additional Technical Assumptions and Requests
*   **Backend Language & Framework:** The backend services will be developed using **C# with .NET 8 LTS**.
*   **UI Library:** The frontend will be built using **Shadcn UI**.
*   **Database:** The preferred database technology is a relational DB, such as **PostgreSQL**.
*   **Cloud Deployment:** The application will be deployed on **Google Cloud Platform (GCP)**, likely using GKE (Google Kubernetes Engine) to manage the services.
*   **CI/CD:** A CI/CD pipeline will be set up to automate the building, testing, and deployment of each microservice independently.

#### Data Strategy
*   **Database Per Service:** Each microservice is the single source of truth for its domain and must own its own private database. There will be no shared databases between services.
*   **Data Consistency:** Eventual consistency is acceptable between services. Asynchronous events via Pub/Sub will be the primary method for propagating state changes.

#### Operational Strategy
*   **Health Checks:** Every microservice must expose a `/health` endpoint that the GKE ingress can use to determine application health.
*   **Alerting:** Basic alerting will be configured in GCP Monitoring to notify the team of high API error rates (e.g., >5% server-side errors over a 5-minute window).

## Epic List

Here is the proposed high-level list of epics to deliver the MVP:

*   **Epic 1: Foundation & Core Services**
    *   **Goal:** Establish the complete project infrastructure on GCP/GKE, including CI/CD pipelines for microservices, and build the foundational User, Authentication, and Product services.
    *   **Success Metrics:** All CI/CD pipelines are operational. A new "hello-world" service can be deployed to the development environment automatically in under 15 minutes. All foundational service APIs are deployed and return successful health checks.

*   **Epic 2: End-to-End Purchasing Workflow**
    *   **Goal:** Develop the Purchasing microservice, enabling users to create and manage suppliers and process purchase orders.
    *   **Success Metrics:** The "happy path" E2E test for creating a supplier and then a purchase order passes successfully. A user can perform these actions via the UI without error. API endpoints achieve >95% unit test coverage.

*   **Epic 3: End-to-End Sales Workflow**
    *   **Goal:** Develop the Sales microservice, enabling users to create and manage customers and process sales orders.
    *   **Success Metrics:** The "happy path" E2E test for creating a customer and then a sales order passes successfully. A user can perform these actions via the UI without error. API endpoints achieve >95% unit test coverage.

## Epic 1 Foundation & Core Services

The primary goal of this epic is to construct the entire technical backbone of the application, acknowledging the significant upfront complexity of a microservices architecture. This involves setting up the cloud infrastructure, source control, observability, and automated deployment pipelines. We will then build the cross-cutting services (Authentication, User, and Product) that all other business modules will depend on. By the end of this epic, we will have a fully operational, deployable platform ready for business-specific features to be built upon it, but with no end-user business functionality yet available.

### Story 1.1 Monorepo & Foundational CI/CD
As a Developer, I want a properly configured monorepo with a working CI/CD pipeline, so that I can efficiently organize, build, and deploy a "hello world" service.

#### Acceptance Criteria
1.  A new monorepo is initialized using Nx.
2.  A shared library for common DTOs/types is created within the monorepo.
3.  A "hello-world" .NET 8 service skeleton is created and successfully built by a new CI/CD pipeline.
4.  The pipeline automatically deploys the service to a **Development** environment on GCP.
5.  A **Staging** environment is also provisioned in GCP, and the pipeline can deploy to it manually.

### Story 1.2 Core Infrastructure & API Gateway
As a DevOps Engineer, I want the core GKE infrastructure and an API Gateway, so that services can be exposed securely and consistently to the outside world.

#### Acceptance Criteria
1.  A GKE cluster is provisioned and configured in the GCP project.
2.  An API Gateway is deployed and configured to route traffic to deployed services.
3.  A decision on the service-to-service communication pattern (e.g., REST, gRPC) is documented.
4.  The "hello-world" service is accessible only through the API Gateway's public URL.

### Story 1.3 Observability Foundation
As a QA Analyst, I want centralized logging and distributed tracing, so that I can effectively debug and monitor requests that span multiple services.

#### Acceptance Criteria
1.  A centralized logging solution (e.g., Google Cloud Logging) is configured.
2.  All services are configured to send structured logs to this solution.
3.  A distributed tracing solution (e.g., OpenTelemetry) is integrated into the service skeletons.
4.  A single request to the API Gateway that calls another service produces a single, correlated trace.

### Story 1.4 Authentication & User Services
As a User, I want to be able to register, log in, and have my permissions recognized, so that I can access the application securely.

#### Acceptance Criteria
1.  An Authentication service provides secure endpoints for registration and login, issuing a JWT.
2.  A User service provides endpoints to manage user data and roles (`Sales Agent`, `Purchasing Agent`).
3.  The frontend token handling strategy (e.g., secure HttpOnly cookie) is implemented.
4.  Integration tests for these services use mocks to run independently.
5.  User passwords are not stored in plaintext; they must be securely hashed and salted.

### Story 1.5 Develop Product Service
As an Admin, I want to manage a catalog of products, so that they can be used in sales and purchase orders.

#### Acceptance Criteria
1.  The service provides paginated CRUD API endpoints for managing Products.
2.  All endpoints are protected and require a valid JWT.
3.  The service has its own dedicated database.
4.  The service is fully observable (logging and tracing) as per the foundation set in Story 1.3.

## Epic 2 End-to-End Purchasing Workflow

The goal of this epic is to deliver the first complete piece of business value to the end-user. Building upon the foundational services from Epic 1, we will develop the Purchasing microservice and the corresponding frontend components. By the end of this epic, a user with the 'Purchasing Agent' role will be able to log in, manage suppliers, and create and manage purchase orders from start to finish.

### Story 2.1 Develop Purchasing Service Skeleton & CI/CD
As a Developer, I want a new 'Purchasing' service skeleton with an automated CI/CD pipeline, so that I can begin developing business features.

#### Acceptance Criteria
1.  A new .NET 8 service project named 'Purchasing.API' is created in the monorepo.
2.  The service is configured for observability (logging/tracing).
3.  A new CI/CD pipeline is created that automatically builds, tests, and deploys the Purchasing service to the dev environment.
4.  The new service is registered with the API Gateway and is accessible.

### Story 2.2 Implement Supplier Management
As a Purchasing Agent, I want to create and manage suppliers, so that I can easily select them when creating purchase orders.

#### Acceptance Criteria
1.  The Purchasing service provides CRUD API endpoints for managing Suppliers.
2.  A 'Supplier' consists of at least a name and contact information.
3.  All endpoints are protected and require a JWT with the 'Purchasing Agent' role.

### Story 2.3 Implement Purchase Order Creation
As a Purchasing Agent, I want to create a new purchase order, so that I can procure products from a supplier.

#### Acceptance Criteria
1.  The Purchasing service provides an endpoint to create a new Purchase Order.
2.  The endpoint accepts a supplier ID and a list of line items (product ID and quantity).
3.  The service communicates asynchronously (via Pub/Sub) with the Product service to retrieve product details.
4.  The Purchase Order saves an immutable 'snapshot' of the product's price and description at the time of creation.

### Story 2.4 Implement Purchase Order Management
As a Purchasing Agent, I want to view and manage the status of my purchase orders, so that I can track the procurement process.

#### Acceptance Criteria
1.  The Purchasing service provides a paginated list of all purchase orders.
2.  The listing endpoint supports filtering by 'status' (`Open`, `Completed`, `Cancelled`). (A `//TODO:` comment will be left for future filtering options like by date or supplier).
3.  The service provides an endpoint to update the status of a purchase order.

### Story 2.5 Build UI for Supplier Management
As a Purchasing Agent, I want a user interface for managing suppliers, so that I can handle supplier data visually.

#### Acceptance Criteria
1.  A "Suppliers" page is created in the frontend application.
2.  The page displays a list of all suppliers.
3.  The page includes forms to create a new supplier and edit an existing one.
4.  Only users with the 'Purchasing Agent' role can access this page.

### Story 2.6 Build UI for Purchase Order Workflow
As a Purchasing Agent, I want a user interface for managing purchase orders, so that I can handle the procurement process visually.

#### Acceptance Criteria
1.  A "Purchase Orders" page is created to list and filter orders by status.
2.  The UI allows a user to view the details of a single purchase order.
3.  The UI provides a mechanism (e.g., a button) to change the status of an order.
4.  A form is created to allow a user to create a new purchase order, including a searchable selector for products.

## Epic 3 End-to-End Sales Workflow

The goal of this epic is to deliver the second major piece of business value. It mirrors the purchasing workflow but is focused on the sales cycle. By the end of this epic, a user with the 'Sales Agent' role will be able to log in, manage customers, and create and manage sales orders, completing the core functionality of the MVP.

### Story 3.1 Develop Sales Service Skeleton & CI/CD
As a Developer, I want a new 'Sales' service skeleton with an automated CI/CD pipeline, so that I can begin developing business features for the sales module.

#### Acceptance Criteria
1.  A new .NET 8 service project named 'Sales.API' is created in the monorepo.
2.  The service is configured for observability (logging/tracing).
3.  A new CI/CD pipeline is created that automatically builds, tests, and deploys the Sales service.
4.  The new service is registered with the API Gateway and is accessible.

### Story 3.2 Implement Customer Management
As a Sales Agent, I want to create and manage customers, so that I can easily select them when creating sales orders.

#### Acceptance Criteria
1.  The Sales service provides CRUD API endpoints for managing Customers.
2.  A 'Customer' consists of at least a name and contact information.
3.  All endpoints are protected and require a JWT with the 'Sales Agent' role.

### Story 3.3 Implement Sales Order Creation
As a Sales Agent, I want to create a new sales order, so that I can sell products to a customer.

#### Acceptance Criteria
1.  The Sales service provides an endpoint to create a new Sales Order.
2.  The endpoint accepts a customer ID and a list of line items (product ID and quantity).
3.  The service communicates asynchronously (via Pub/Sub) with the Product service to retrieve product details.
4.  The Sales Order saves an immutable 'snapshot' of the product's price and description.

### Story 3.4 Implement Sales Order Management
As a Sales Agent, I want to view and manage the status of my sales orders, so that I can track the sales process.

#### Acceptance Criteria
1.  The Sales service provides a paginated list of all sales orders.
2.  The listing endpoint supports filtering by 'status' (`Open`, `Completed`, `Cancelled`).
3.  The service provides an endpoint to update the status of a sales order.

### Story 3.5 Build UI for Customer Management
As a Sales Agent, I want a user interface for managing customers, so that I can handle customer data visually.

#### Acceptance Criteria
1.  A "Customers" page is created in the frontend application.
2.  The page displays a list of all customers.
3.  The page includes forms to create a new customer and edit an existing one.
4.  Only users with the 'Sales Agent' role can access this page.

### Story 3.6 Build UI for Sales Order Workflow
As a Sales Agent, I want a user interface for managing sales orders, so that I can handle the sales process visually.

#### Acceptance Criteria
1.  A "Sales Orders" page is created to list and filter orders by status.
2.  The UI allows a user to view the details of a single sales order.
3.  The UI provides a mechanism to change the status of an order.
4.  A form is created to allow a user to create a new sales order, including a searchable selector for products.

## Checklist Results Report

### **Executive Summary**

*   **Overall PRD Completeness:** 90%
*   **MVP Scope Appropriateness:** Just Right (Aggressive but well-defined)
*   **Readiness for Architecture Phase:** Ready
*   **Most Critical Gaps or Concerns:** While the document is strong, it lacks explicit sections for Data and Operational requirements. These are currently implied within stories but should be stated clearly for the architect.

### **Category Analysis Table**

| Category | Status | Critical Issues |
| :--- | :--- | :--- |
| 1. Problem Definition & Context | PASS | None. |
| 2. MVP Scope Definition | PASS | None. |
| 3. User Experience Requirements | PASS | None. |
| 4. Functional Requirements | PASS | None. |
| 5. Non-Functional Requirements | PASS | While solid, could be more detailed in future iterations. |
| 6. Epic & Story Structure | PASS | None. |
| 7. Technical Guidance | PASS | None. |
| 8. Cross-Functional Requirements | PARTIAL | Data and Operational requirements are not explicitly documented as separate sections. |
| 9. Clarity & Communication | PASS | None. |

### **Top Issues by Priority**

*   **MEDIUM:** **Data Requirements:** We should add a small section to formalize our data strategy (e.g., "Each service owns its data," "No shared databases," etc.).
*   **MEDIUM:** **Operational Requirements:** We should explicitly state monitoring and alerting needs (e.g., "Each service must expose a health check endpoint," "Alerts should be configured for high error rates").

### **MVP Scope Assessment**
The scope is tightly defined and aligned with the 3-month goal. The breakdown into three epics (Foundation, Purchasing, Sales) is logical. The risk remains high due to the timeline and complexity of the microservices architecture, but the plan is clear.

### **Recommendations**
1.  **Action:** Before handing off to the architect, create two small subsections under "Additional Technical Assumptions": one for "Data Strategy" and one for "Operational Strategy" to address the medium-priority issues.
2.  **Next Step:** Proceed with the "Next Steps" section of the PRD to generate the handoff prompts.

### **Final Decision**
**READY FOR ARCHITECT**: The PRD and epics are comprehensive and ready for the architectural design phase, pending the minor additions recommended above.
