# TaskApp API

API REST para gestión de tareas con autenticación JWT y caché Redis.

## Stack Tecnológico

- **FastAPI** - Framework web
- **SQLite** - Base de datos
- **Redis** - Caché
- **JWT** - Autenticación

## Endpoints

### Autenticación
| Método | Endpoint | Descripción |
|--------|----------|-------------|
| POST | `/auth/token` | Obtener token JWT |

### Usuarios
| Método | Endpoint | Descripción |
|--------|----------|-------------|
| POST | `/users/` | Crear usuario |
| GET | `/users/me` | Usuario actual |

### Tareas
| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/tasks/` | Listar tareas |
| GET | `/tasks/{id}` | Ver tarea |
| POST | `/tasks/` | Crear tarea |
| PUT | `/tasks/{id}` | Actualizar tarea |
| DELETE | `/tasks/{id}` | Eliminar tarea |

## Documentación

Swagger: http://localhost:8000/docs
