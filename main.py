from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from config.database import engine, Base
from middlewares.error_handler import ErrorHandler 
from routers.game import game_router 
from routers.auth import auth_router 

# Creación de una instancia de FastAPI
app = FastAPI()
app.title = "GameStore"  # Título de la app
app.version = "1.0.0"  # Versión de la app

# Adición de un middleware personalizado para manejar errores
app.add_middleware(ErrorHandler)

# Inclusión de los enrutadores específicos para juegos y autenticación
app.include_router(game_router)
app.include_router(auth_router)

# Creación de las tablas en la base de datos según las definiciones de clases de modelo (si no existen)
Base.metadata.create_all(bind=engine)

# Definición de una ruta para la raíz de la aplicación
@app.get("/", tags=['home'])  # Decorador para manejar solicitudes GET en la ruta "/"
def message():
    return HTMLResponse(content="<h1> Mostrador de Videojuegos </h1>")  # Respuesta HTML simple para la ruta raíz
