from fastapi import FastAPI, Header, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from services.DoorServices import DoorServices
from typing import Annotated

app = FastAPI()

# Configure cors
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

door_service = DoorServices()

@app.get("/")
async def root():
    return {"message": "Hello World"}


# Ruta para recibir el valor de apertura como query parameter y el nodo_id en los headers
@app.get("/registro_puerta/")
async def open_door(nodo_id: str = None, valor: str = None):
    if valor is None:
        raise HTTPException(status_code=400, detail="No se recibió el valor de apertura")
    elif nodo_id is None:
        raise HTTPException(status_code=400, detail="No se recibió el nodo_id")
    else:
        message = door_service.register_door_action(nodo_id, valor)
    return message

# Ruta para consultar el tiempo del sonar de un nodo
@app.get("/tiempo_sonar/")
async def get_sonar_time(nodo_id: str = None):
    if nodo_id is None:
        raise HTTPException(status_code=400, detail="No se recibió el nodo_id")
    else:
        sonar_time = door_service.get_sonar_time(nodo_id)
    return sonar_time

# Ruta para actualizar la ultima lectura de un nodo
@app.get("/sonar/")
async def sonar(nodo_id: str = None):
    if nodo_id is None:
        raise HTTPException(status_code=400, detail="No se recibió el nodo_id")
    else:
        message = door_service.sonar(nodo_id)
    return message


