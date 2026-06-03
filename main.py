from fastapi import FastAPI
from sqlmodel import Session

from mascota_model import *
from crud_mascota import *
from database import engine

app = FastAPI()


@app.post("/mascotas")
def create_endpoint(mascota: MascotaBase):

    with Session(engine) as session:
        return create_mascota(session, mascota)
    



@app.get("/mascotas/{id}")
def get_one_endpoint(id: int):

    with Session(engine) as session:
        return get_one_mascota(session, id)

    """
        mascota = get_one_mascota(session, id)
        return get_or_404(mascota)
    """

@app.put("/mascotas/{id}")
def update_endpoint(id: int, mascota: MascotaUpdate):

    with Session(engine) as session:
        return update_mascota(session, id, mascota)

    """
        updated = update_mascota(session, id, mascota)
        return get_or_404(updated)
    """

@app.delete("/mascotas/{id}")
def delete_endpoint(id: int):

    with Session(engine) as session:
        return delete_mascota(session, id)
    
"""
        deleted = delete_mascota(session, id)
        return get_or_404(deleted)


"""
    
"""
startup
from fastapi import FastAPI
from sqlmodel import SQLModel

from database import engine

app = FastAPI()


@app.on_event("startup")
def startup():
    SQLModel.metadata.create_all(engine)

uvicorn main:app --host 0.0.0.0 --port 8000

"""