from typing import Optional
from pydantic import BaseModel, Field

# Definición de una clase llamada Game que hereda de BaseModel (de Pydantic)
class Game(BaseModel):
    # Atributo id que puede ser un entero opcional (puede ser None)
    id: Optional[int] = None

    # Atributo nombre, una cadena de texto con valores predeterminados y restricciones
    nombre: str = Field(default="Mi Juego", min_length=5, max_length=30)

    # Atributo categoria, una cadena de texto con valores predeterminados y restricciones
    categoria: str = Field(default="Comedia", min_length=3, max_length=15)

    # Atributo calificacion, un número de punto flotante con valores predeterminados y restricciones
    calificacion: float = Field(default=10, ge=0, le=10)

    # Configuración adicional para la documentación de la clase
    class Config:
        # Configuración del modelo que afecta a la generación de esquemas JSON
        model_config = {
            "json_schema_extra": {
                # Ejemplos adicionales para la documentación del esquema JSON
                "examples": [
                    {
                        "id": 1,
                        "nombre": "Mi Pelicula",
                        "categoria": "Descripcion de la pelicula",
                        "calificacion": 10,
                    }
                ]
            }
        }