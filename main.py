from fastapi import FastAPI, Header, HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Configure cors
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get("/")
async def root():
    return {"message": "Hello World"}

# Ruta para recibir el valor de apertura como query parameter y el nodo_id en los headers
@app.get("/open")
async def open_door(nodo_id: str = Header(None), apertura: str = None):
    if apertura is None:
        raise HTTPException(status_code=400, detail="No se recibió el valor de apertura")
    if nodo_id is None:
        raise HTTPException(status_code=400, detail="No se recibió el nodo_id")

    return {"nodo_id": nodo_id, "apertura": apertura}

