#Ésta parte me salta error al importar la libreria jwt
from jwt import encode, decode

def create_token(data: dict, secret: str = "1234567890") -> str:
    """
    En ésta función se crea un token JWT, 

    Parametros:
    - data: Un diccionario que contiene la información que se quiere incluir en el token.
    - secret: Clave secreta utilizada para firmar el token (por defecto es "1234567890").

    Retornos:
    - Un token JWT como una cadena de caracteres.
    """
    token = encode(payload=data, key=secret, algorithm="HS256")
    return token

def validate_token(token: str):
    """
    Función para validar un token JWT.

    Parametros:
    - token: Token JWT que se desea validar.

    Returns:
    - Los datos decodificados del token si la validación es exitosa, de lo contrario, lanzará una excepción.
    """
    data = decode(token, "1234567890", algorithms=["HS256"])
    return data