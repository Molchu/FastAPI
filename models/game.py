from config.database import Base
from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, ForeignKey

class Game(Base):
    __tablename__ = "games"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    categoria =  Column(String, nullable=False)
    calificacion = Column(String, nullable=False)