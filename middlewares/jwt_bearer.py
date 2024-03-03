from fastapi.security import HTTPBearer
from utils.jwt_manager import validate_token
from fastapi import Request, HTTPException

# Definición de una clase llamada JWTBearer que hereda de HTTPBearer
class JWTBearer(HTTPBearer):
    # Implementación de la función __call__ para realizar la validación del token en cada solicitud
    async def __call__(self, request: Request):
        # Llamada a la implementación __call__ de la clase base HTTPBearer para obtener la información de autenticación
        auth = await super().__call__(request)
        
        # Validación del token utilizando la función validate_token del módulo utils.jwt_manager
        data = validate_token(auth.credentials)

        # Verificación adicional: si el email en los datos decodificados no es 'admin@gmail.com', se lanza una excepción HTTP 401
        if data['email'] != 'admin@gmail.com':
            raise HTTPException(status_code=401, detail="Invalid user")
