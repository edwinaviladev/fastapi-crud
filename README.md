# TaskApp API

API REST para gestión de tareas con autenticación JWT y caché Redis.

## Stack Tecnológico

- **FastAPI** - Framework web
- **SQLite** - Base de datos
- **Redis** - Caché
- **JWT** - Autenticación

## Instalación

```bash
# Crear entorno virtual
python -m venv .venv
source .venv/Scripts/activate  # Windows: .venv\Scripts\activate

# Instalar dependencias
pip install fastapi uvicorn sqlmodel python-jose[cryptography] pwdlib[argon2] python-multipart redis fastapi-cache python-dotenv

# Iniciar Redis
docker-compose -f compose.yml up -d

# Ejecutar
uvicorn app.main:app --reload
```

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
