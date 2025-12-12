Este documento describe un conjunto integral de convenciones de nomenclatura para un entorno tecnológico full-stack que utiliza C#, PostgreSQL y TypeScript. El principio fundamental es utilizar el estilo de nomenclatura idiomático de cada lenguaje y automatizar el mapeo entre ellos.

A continuación se presenta un resumen de las convenciones clave para cada capa:

*   **C# (Backend):**
    *   **PascalCase** se utiliza para namespaces, clases, records, interfaces (con un prefijo `I`), métodos y propiedades.
    *   Los **acrónimos** (como `ID`, `API`, `HTTP`) se mantienen en mayúsculas dentro de los nombres en PascalCase (por ejemplo, `APIKey`, `HTTPClient`).
    *   **camelCase** se utiliza para variables locales y parámetros.
    *   Los campos privados llevan un prefijo de guion bajo (`_camelCase`).
    *   Las constantes están en `UPPER_SNAKE_CASE`.

*   **PostgreSQL (Base de datos):**
    *   **snake_case** se utiliza para todo: esquemas, tablas y columnas.
    *   Los nombres de las tablas pueden ser plurales o singulares, pero esto debe ser coherente dentro de un proyecto.
    *   Las claves primarias se nombran `id`, y los identificadores de negocio (cadenas de texto) se nombran `code`.
    *   Las columnas de clave foránea siguen el patrón `{entity_name}_id`.
    *   Los índices y las restricciones tienen sus propios prefijos estandarizados en `snake_case` (`ix_`, `uk_`, `fk_`, etc.).

*   **TypeScript (Frontend):**
    *   **PascalCase** se utiliza para interfaces, nombres de tipos y componentes de React.
    *   **camelCase** se utiliza para propiedades, funciones y variables.
    *   Las constantes siguen la convención `UPPER_SNAKE_CASE`, de forma similar a C#.

*   **API y JSON:**
    *   Las URL de los endpoints de la API están en **kebab-case** (por ejemplo, `/api/v1/user-profiles`).
    *   Los parámetros de consulta y las claves de los objetos JSON están en **camelCase**.

*   **Mapeo con EF Core:**
    *   Se utiliza un ayudante `SnakeCaseNamingConvention` personalizado en Entity Framework Core para traducir automáticamente las propiedades en `PascalCase` de C# a columnas en `snake_case` de PostgreSQL. Esto elimina la necesidad de atributos de mapeo manual.

*   **Datos entre servicios (Tablas de proyección):**
    *   Para microservicios, cuando un servicio necesita una copia de datos de otro, se utilizan tablas especiales de "proyección". Estas tablas se nombran con un prefijo de 4 letras que indica el servicio de origen y un sufijo `_prj` (por ejemplo, `auth_users_prj` para datos de usuario del servicio de autenticación).

El documento también proporciona una lista de verificación de implementación, configuraciones de herramientas (para `EditorConfig` y `ESLint`) y un historial detallado de cambios.