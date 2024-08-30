from config.Db_config import Session
from models.Nodo import Nodo


class NodosProvider:
    def get_nodos(self):
        """"
        Esta función se encarga de obtener los nodos de la base de datos.

        Proceso:
        1. Crea una nueva sesión de base de datos.
        2. Consulta los nodos.
        3. Cierra la sesión.

        Devuelve:
        nodos (list): Una lista de nodos.

        Excepciones:
        Si ocurre un error durante la consulta o la conversión de los datos, se hace rollback
        de la transacción y se lanza la excepción para que pueda ser manejada en un nivel superior.
        """
        try:
            # Crear una nueva sesión
            db = Session()
            # Consultar los nodos
            nodos = db.query(Nodo).all()
        except Exception as e:
            # Si ocurre un error, hacer rollback de la transacción
            db.rollback()
            # Lanzar la excepción
            raise e
        finally:
            # Cerrar la sesión
            db.close()
        return nodos

    def get_nodo_by_id(self, nodo_id):
        """"
        Esta función se encarga de obtener un nodo por su id.

        Proceso:
        1. Crea una nueva sesión de base de datos.
        2. Consulta el nodo por su id.
        3. Cierra la sesión.

        Parámetros:
        nodo_id (int): El id del nodo a consultar.

        Devuelve:
        nodo (Nodo): El nodo consultado.

        Excepciones:
        Si ocurre un error durante la consulta o la conversión de los datos, se hace rollback
        de la transacción y se lanza la excepción
        """
        try:
            # Crear una nueva sesión
            db = Session()
            # Consultar el nodo por su id
            nodo = db.query(Nodo).filter(Nodo.nodo_id == nodo_id).first()
        except Exception as e:
            # Si ocurre un error, hacer rollback de la transacción
            db.rollback()
            # Lanzar la excepción
            raise e
        finally:
            # Cerrar la sesión
            db.close()
        return nodo

    """
    Esta función se encarga de actualizar la última señal de un nodo en la base de datos.
    
    Proceso:
    1. Crea una nueva sesión de base de datos.
    2. Consulta el nodo por su id.
    3. Actualiza la última señal del nodo.
    4. Hace commit de la transacción.
    5. Cierra la sesión.
    
    Parámetros:
    nodo_id (int): El id del nodo a actualizar.
    fecha (str): La fecha de la última señal.
    
    Excepciones:
    Si ocurre un error durante la actualización o la conversión de los datos, se hace rollback
    """
    def update_last_signal(self, nodo_id, fecha):
        try:
            # Crear una nueva sesión
            db = Session()
            # Consultar el nodo por su id
            nodo = db.query(Nodo).filter(Nodo.nodo_id == nodo_id).first()
            # Actualizar la última señal del nodo
            nodo.ultima_señal = fecha
            #   Hacer commit de la transacción
            db.commit()
        except Exception as e:
            # Si ocurre un error, hacer rollback de la transacción
            db.rollback()
            # Lanzar la excepción
            raise e
        finally:
            # Cerrar la sesión
            db.close()

