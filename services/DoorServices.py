from providers.NodosProvider import NodosProvider
from providers.Registros_PuertaProvider import Registros_PuertaProvider
from datetime import datetime
import pytz


class DoorServices:
    def __init__(self):
        self.nodosProvider = NodosProvider()
        self.registros_puertaProvider = Registros_PuertaProvider()

    def register_door_action(self, nodo_id, apertura):
        # Obtener la fecha y hora actual en UTC
        fecha_utc = datetime.now(pytz.utc)

        # Definir la zona horaria de Colombia
        zona_horaria_colombia = pytz.timezone('America/Bogota')

        # Convertir la fecha y hora a la zona horaria de Colombia
        fecha_colombia = fecha_utc.astimezone(zona_horaria_colombia)

        # formato de fecha
        fecha_colombia = fecha_colombia.strftime("%Y-%m-%d %H:%M:%S")
        print(fecha_colombia)
        self.registros_puertaProvider.registrar_registro_puerta(nodo_id, fecha_colombia, apertura)
        return {"message": "Door action registered"}

    def get_sonar_time(self, nodo_id):
        nodo = self.nodosProvider.get_nodo_by_id(nodo_id)
        return nodo.tiempo_sonar

    # Funcion de sonar para actualizar la ultima lectura de cada nodo
    def sonar(self, nodo_id):
        fecha = datetime.now()
        # convertir de utc a zona horaria de colombia
        fecha = fecha.astimezone()
        # formato de fecha
        fecha = fecha.strftime("%Y-%m-%d %H:%M:%S")
        self.nodosProvider.update_last_signal(nodo_id, fecha)
        return {"message": "Last signal updated"}
