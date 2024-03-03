# Importación de clases necesarias para definir el middleware y las respuestas JSON en FastAPI.
from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import FastAPI, Request, Response
from fastapi.responses import JSONResponse

# Definición de la clase ErrorHandler que actúa como middleware de manejo de errores.
class ErrorHandler(BaseHTTPMiddleware):
    
    # Constructor de la clase que recibe una instancia de la aplicación FastAPI.
    def __init__(self, app: FastAPI):
        super().__init__(app)
    
    # Método de despacho que intercepta las solicitudes HTTP entrantes.
    async def fispatch(self, request: Request, call_next) -> Response | JSONResponse:
        try:
            # Se llama a la siguiente función de middleware para procesar la solicitud.
            return await call_next(request)
        except Exception as e:
            # Si se produce una excepción durante el procesamiento de la solicitud, se captura aquí.
            # Se crea una respuesta JSON con un código de estado HTTP 500 (error interno del servidor)
            # y un cuerpo JSON que contiene el mensaje de error obtenido al convertir la excepción a cadena.
            return JSONResponse(
                status_code=500,
                content={"error": str(e)}
            )