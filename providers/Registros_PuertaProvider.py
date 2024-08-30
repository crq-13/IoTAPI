from config.Db_config import Session
from models.Registro_Puerta import Registro_Puerta


class Registros_PuertaProvider:
    def __init__(self):
        self.session = Session()

    """"
    Esta funcion se encarga de registrar una accion de puerta en la base de datos.
    
    Proceso:
    1. Crea un nuevo registro de puerta.
    2. Agrega el registro a la base de datos.
    3. Hace commit de la transaccion.
    
    Parametros:
    nodo_id (int): El id del nodo que realizo la accion.
    fecha (str): La fecha en la que se realizo la accion.
    valor (str): El valor de la accion.
    
    Excepciones:
    Si ocurre un error durante la creacion o la insercion del registro, se hace
    rollback de la transaccion y se lanza la excepcion para que pueda ser manejada
    en un nivel superior.
    """
    def registrar_registro_puerta(self, nodo_id, fecha, valor):
        try:
            # Crear un nuevo registro de puerta
            registro_puerta = Registro_Puerta(nodo_id=nodo_id, fecha=fecha, valor=valor)
            # Agregar el registro a la base de datos
            self.session.add(registro_puerta)
            # Hacer commit de la transaccion
            self.session.commit()
        except Exception as e:
            # Si ocurre un error, hacer rollback de la transaccion
            self.session.rollback()
            # Lanzar la excepcion para que pueda ser manejada en un nivel superior
            raise e
        finally:
            # Cerrar la sesion
            self.session.close()
