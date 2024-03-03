from fastapi import APIRouter
from utils.jwt_manager import create_token 
from fastapi.responses import JSONResponse
from schemas.user import User

# Se crea un nuevo enrutador de API utilizando APIRouter(), que permitirá definir los endpoints para la autenticación
auth_router = APIRouter()

# Se define una ruta POST /login en el enrutador de autenticación.
# Esta ruta está decorada con @auth_router.post, lo que indica que responde a solicitudes POST en la ruta /login.
# También se especifica que este endpoint pertenece al tag 'auth' y tiene un modelo de respuesta de tipo dict, con un código de estado de respuesta 200.
@auth_router.post("/login", tags=['auth'], response_model=dict, status_code=200)
def login(user: User) -> dict:
    # Se verifica si el correo electrónico y la contraseña proporcionados en el objeto user coinciden con las credenciales de administrador.
    if user.email == 'admin@gmail.com' and user.password == "admin":
        # Si las credenciales son válidas, se genera un token JWT utilizando la función create_token y se devuelve como parte de una respuesta JSON con un código de estado 200.
        token = create_token(data=user.model_dump())  # Se genera el token JWT utilizando la función create_token y los datos del usuario.
        return JSONResponse(content={"token": token}, status_code=200)  # Se devuelve el token JWT en una respuesta JSON con un código de estado 200.
    else:
        # Si las credenciales no son válidas, se devuelve un mensaje de error en una respuesta JSON con un código de estado 401.
        return JSONResponse(content={"message": "Invalid credentials"}, status_code=401)  # Se devuelve un mensaje de error en una respuesta JSON con un código de estado 401.
