from fastapi import FastAPI, HTTPException, Depends
from app.models import ServicioFunerario
from app.auth import get_current_user

app = FastAPI(title="API Funeraria")


servicios = []

@app.post("/funeraria/", response_model=ServicioFunerario)
def crear_servicio(servicio: ServicioFunerario, user: dict = Depends(get_current_user)):
    if user["role"] != "admin":
        raise HTTPException(status_code=403, detail="No autorizado")
    servicios.append(servicio)
    return servicio

@app.get("/funeraria/")
def listar_servicios():
    return servicios

@app.get("/funeraria/{servicio_id}")
def obtener_servicio(servicio_id: int):
    for s in servicios:
        if s.id == servicio_id:
            return s
    raise HTTPException(status_code=404, detail="Servicio no encontrado")
