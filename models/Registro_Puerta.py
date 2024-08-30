from config.Db_config import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class Registro_Puerta(Base):
    __tablename__ = 'registro_puertas'
    registro_puerta_id = Column(Integer, primary_key=True)
    nodo_id = Column(Integer, ForeignKey('nodos.nodo_id'))
    fecha = Column(String, nullable=False)
    valor = Column(String, nullable=False)