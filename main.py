from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Models
class Empresa(BaseModel):
    idEmpresa: int
    nombre: str
    nit: str
    telefono: str
    direccion: str
    correo: str

class Proyecto(BaseModel):
    idProyecto: int
    titulo: str
    empresaFK: int

class Ticket(BaseModel):
    idTicket: int
    desc: str
    comentarios: List[str]
    estado: str
    proyectoFK: int

class Usuario(BaseModel):
    idUser: int
    nombre: str
    correo: str
    contrasena: str
    ticketFK: int
    empresaFK: int

# In-memory data storage
empresas = []
proyectos = []
tickets = []
usuarios = []

# Routes
@app.post("/empresa/", response_model=Empresa)
def create_empresa(empresa: Empresa):
    empresas.append(empresa)
    return empresa

@app.post("/proyecto/", response_model=Proyecto)
def create_proyecto(proyecto: Proyecto):
    proyectos.append(proyecto)
    return proyecto

@app.post("/ticket/", response_model=Ticket)
def create_ticket(ticket: Ticket):
    tickets.append(ticket)
    return ticket

@app.post("/usuario/", response_model=Usuario)
def create_usuario(usuario: Usuario):
    usuarios.append(usuario)
    return usuario

@app.get("/empresa/", response_model=List[Empresa])
def get_empresas():
    return empresas

@app.get("/proyecto/", response_model=List[Proyecto])
def get_proyectos():
    return proyectos

@app.get("/ticket/", response_model=List[Ticket])
def get_tickets():
    return tickets

@app.get("/usuario/", response_model=List[Usuario])
def get_usuarios():
    return usuarios

@app.get("/empresa/{empresa_id}", response_model=Empresa)
def get_empresa(empresa_id: int):
    for empresa in empresas:
        if empresa.idEmpresa == empresa_id:
            return empresa
    raise HTTPException(status_code=404, detail="Empresa not found")

@app.get("/proyecto/{proyecto_id}", response_model=Proyecto)
def get_proyecto(proyecto_id: int):
    for proyecto in proyectos:
        if proyecto.idProyecto == proyecto_id:
            return proyecto
    raise HTTPException(status_code=404, detail="Proyecto not found")

@app.get("/ticket/{ticket_id}", response_model=Ticket)
def get_ticket(ticket_id: int):
    for ticket in tickets:
        if ticket.idTicket == ticket_id:
            return ticket
    raise HTTPException(status_code=404, detail="Ticket not found")

@app.get("/usuario/{usuario_id}", response_model=Usuario)
def get_usuario(usuario_id: int):
    for usuario in usuarios:
        if usuario.idUser == usuario_id:
            return usuario
    raise HTTPException(status_code=404, detail="Usuario not found")
