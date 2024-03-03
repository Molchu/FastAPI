from fastapi import APIRouter, Path, Query, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from typing import List
from models.game import Game as GameModel
from config.database import Session
from middlewares.jwt_bearer import JWTBearer
from services.game import GameService
from schemas.game import Game

# Se crea un nuevo enrutador de API utilizando APIRouter(), que permitirá definir los endpoints relacionados con los juegos.
game_router = APIRouter()

# Se define un endpoint GET /games para obtener todos los juegos.
@game_router.get("/games", tags=['games'], response_model=List[Game], status_code=200)
def get_games() -> List[Game]:
    # Se llama al método get_games() del servicio GameService para obtener todos los juegos.
    result = GameService(Session()).get_games()
    # Se retorna una respuesta JSON con los juegos obtenidos.
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

# Se define un endpoint GET /games/{id} para obtener un juego por su ID.
@game_router.get("/games/{id}", tags=['games'], response_model=Game, status_code=200)
def get_game(id: int = Path(..., title="The ID of the game to get")) -> Game:
    # Se llama al método get_game(id) del servicio GameService para obtener el juego con el ID especificado.
    result = GameService(Session()).get_game(id)
    # Si no se encuentra el juego, se retorna un mensaje de error.
    if not result:
        return JSONResponse(status_code=404, content={"message": "Game not found"})
    # Se retorna una respuesta JSON con el juego obtenido.
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

# Se define un endpoint GET /games/ para obtener juegos por categoría.
@game_router.get("/games/", tags=['games'], response_model=List[Game])
def get_games_by_category(category: str = Query(..., min_length=3, max_length=15, title="Categoria del juego")) -> List[Game]:
    # Se llama al método get_games_by_category(category) del servicio GameService para obtener juegos por categoría.
    result = GameService(Session()).get_games_by_category(category)
    # Si no se encuentran juegos, se retorna un mensaje de error.
    if not result:
        return JSONResponse(status_code=404, content={"message": "Juegos no encontrados"})
    # Se retorna una respuesta JSON con los juegos obtenidos.
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

# Se define un endpoint POST /games para crear un nuevo juego.
@game_router.post("/games", tags=['games'], response_model=dict, status_code=201)
def create_game(game: Game) -> dict:
    # Se llama al método create_game(game) del servicio GameService para crear un nuevo juego.
    GameService(Session()).create_game(game)
    # Se retorna un mensaje de éxito.
    return JSONResponse(content={"message": "Juego creado satisfactoriamente"}, status_code=201)

# Se define un endpoint PUT /games/{id} para actualizar un juego existente por su ID.
@game_router.put("/games/{id}", tags=['games'], response_model=dict, status_code=200)
def update_game(id: int, game: Game) -> dict:
    # Si no se encuentra el juego, se retorna un mensaje de error.
    if not GameService(Session()).get_game(id):
        return JSONResponse(content={"message": "Juego no encontrado"}, status_code=404)
    # Se llama al método update_game(id, game) del servicio GameService para actualizar el juego.
    GameService(Session()).update_game(id, game)
    # Se retorna un mensaje de éxito.
    return JSONResponse(content={"message": "Juego actualizado satisfactoriamnte"}, status_code=200)

# Se define un endpoint DELETE /games/{id} para eliminar un juego por su ID.
@game_router.delete("/games/{id}", tags=['games'], response_model=dict)
def delete_game(id: int) -> dict:
    # Si no se encuentra el juego, se retorna un mensaje de error.
    if not GameService(Session()).get_game(id):
        return JSONResponse(content={"message": "Game not found"}, status_code=404)
    # Se llama al método delete_game(id) del servicio GameService para eliminar el juego.
    GameService(Session()).delete_game(id)
    # Se retorna un mensaje de éxito.
    return JSONResponse(content={"message": "Game deleted successfully"})