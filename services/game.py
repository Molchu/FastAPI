from models.game import Game as GameModel
from schemas.game import Game

# Definición de una clase llamada GameService
class GameService():
    # Constructor de la clase que recibe una instancia de la base de datos (db) como parámetro
    def __init__(self, db) -> None:
        self.db = db

    # Método para obtener todos los juegos desde la base de datos
    def get_games(self):
        result = self.db.query(GameModel).all()
        return result

    # Método para obtener un juego por su ID desde la base de datos
    def get_game(self, id: int):
        result = self.db.query(GameModel).filter(GameModel.id == id).first()
        return result

    # Método para obtener todos los juegos de una categoría específica desde la base de datos
    def get_games_by_category(self, category):
        result = self.db.query(GameModel).filter(GameModel.category == category).all()
        return result

    # Método para crear un nuevo juego en la base de datos
    def create_game(self, game: Game):
        # Se crea una nueva instancia de la clase GameModel usando los datos del objeto game
        new_game = GameModel(**game.model_dump())
        # Se agrega el nuevo juego a la sesión de la base de datos
        self.db.add(new_game)
        # Se confirman los cambios en la base de datos
        self.db.commit()

    # Método para actualizar un juego existente en la base de datos
    def update_game(self, id: int, data: Game):
        # Se obtiene el juego existente por su ID
        game = self.get_game(id)
        # Se actualizan los atributos del juego con los datos proporcionados
        game.nombre = data.nombre
        game.categoria = data.categoria
        game.calificacion = data.calificacion
        # Se confirman los cambios en la base de datos
        self.db.commit()

    # Método para eliminar un juego de la base de datos por su ID
    def delete_game(self, id: int):
        # Se obtiene el juego por su ID
        game = self.get_game(id)
        # Se elimina el juego de la sesión de la base de datos
        self.db.delete(game)
        # Se confirman los cambios en la base de datos
        self.db.commit()