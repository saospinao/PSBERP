# Manejo de sesesion en Next.Js

## Resumen Ejecutivo: Modelo de Sesiones para el ERP

El modelo de sesiones implementado utilizará una combinación de **Tokens Web JSON (JWT)**, **Tokens de Refresco (Refresh Tokens)** y un **Almacenamiento Centralizado (Redis)** para garantizar la seguridad, el estado persistente y la capacidad de revocación instantánea.

### Componentes Clave de la Arquitectura

| Componente | Uso Principal | Ubicación y Seguridad | Vida Útil (Ej.) |
| :--- | :--- | :--- | :--- |
| **Access Token (JWT)** | Autorización rápida en cada solicitud (microservicios). | Enviado en el **cuerpo de la respuesta** (Header `Authorization`). | **5 - 15 minutos** (Corta). |
| **Refresh Token** | Obtener nuevos Access Tokens sin forzar el re-login. | Almacenado en una **Cookie HttpOnly** (Protección contra XSS). | **7 - 30 días** (Larga). |
| **Session Store (Redis)** | Almacenar Refresh Tokens válidos para **revocación instantánea** y estado centralizado. | Backend. | Hasta la expiración o revocación. |
| **Modelo de Autorización** | **RBAC (Role-Based Access Control)**. Los permisos viajan dentro del JWT para validación rápida. | Backend (Generación), JWT (Payload), Backend (Validación final). | N/A |

### Flujo de Autenticación y Sesiones

El proceso se divide en cuatro pasos cruciales:

#### 1. Login y Generación
* El servidor genera un **JWT de Acceso** y un **Refresh Token**.
* El JWT se envía en la respuesta para uso inmediato del frontend.
* El Refresh Token se coloca en una **Cookie HttpOnly y Secure**.
* El Refresh Token se registra en **Redis** junto con el `userId`, IP y `userAgent` para control de seguridad y revocación.

#### 2. Validación (Middleware)
* En Next.js (`/middleware.ts`), se valida el **JWT de Acceso** en cada ruta protegida.
* Si el JWT es válido, se permite el acceso. 

#### 3. Refresco (Mantenimiento de Sesión)
* Si el JWT expira, el frontend llama al endpoint `/api/auth/refresh`.
* El backend extrae el **Refresh Token** de la cookie HttpOnly, lo valida contra Redis y, si es correcto, emite un **nuevo JWT de Acceso** al cliente.

#### 4. Logout y Revocación
* Al hacer logout, el backend **elimina el Refresh Token de Redis** y borra la cookie HttpOnly. Esto garantiza el cierre de sesión inmediato.


### Seguridad y Auditoría

La arquitectura está diseñada con los siguientes mecanismos de seguridad y control:

#### 1. Gestión de Permisos (RBAC)
* El ERP define un **árbol de permisos** (Ej: `inventario.productos.ver`).
* Los roles (`admin`, `inventarios`) se asignan a los permisos.
* Los permisos se incrustan en el **JWT** para una verificación de acceso eficiente en los *Route Handlers* del backend.

#### 2. Revocación Instantánea
* La clave para el control de sesiones es **Redis**. Si un usuario es bloqueado o se detecta actividad sospechosa, el administrador puede **invalidar (eliminar)** el Refresh Token de Redis, denegando el acceso inmediatamente.

#### 3. **Auditoría** (Obligatorio para ERP)
* Se implementará una tabla (`audit_logs`) para registrar **todas las acciones sensibles** (inicios de sesión, intentos fallidos, crear/modificar/eliminar registros, cambios de roles/permisos).

#### 4. **Hardening Adicional**
* Se aplicarán medidas como **Cookies SameSite=Strict**, **Rate Limiting** para el login, **HSTS** y la verificación opcional de **IP/UserAgent** al refrescar el token.


### 🌐 Sincronización de Estado en Frontend (Next.js/React)

Para manejar el estado del usuario (roles, permisos, nombre) en el cliente:

* Se usará **React Query** para cargar el estado del usuario de forma asincrónica desde el endpoint `/api/auth/me`.
* Se usará **Zustand** o **Context** para mantener el estado global básico del usuario.
* El **Middleware de Next.js** garantiza que el usuario esté autenticado *antes* de cargar cualquier página privada.

