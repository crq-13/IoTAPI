from config.Db_config import Base
from sqlalchemy import Column, Integer, String, DateTime


class Nodo(Base):
    __tablename__ = 'nodos'
    nodo_id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    activo = Column(Integer, nullable=False)
    tiempo_sonar = Column(Integer, nullable=True)
    ultima_señal = Column(DateTime, nullable=True)
