from fastapi import FastAPI, APIRouter, HTTPException
from typing import List
from pymongo import MongoClient
from model.model import Empresa, Proyecto, Ticket, Usuario, ComentarioRequest, EstadoRequest, DescripcionRequest

router = APIRouter()
app = FastAPI()

# MongoDB connection
client = MongoClient("mongodb://localhost:27017")
db = client["fusepong"]

## GET Routes
@router.get("/corporations", response_model=List[Empresa])
def get_empresas():
    return list(db.corporations.find({}, {"_id": 0}))

@router.get("/proyects", response_model=List[Proyecto])
def get_proyectos():
    return list(db.proyects.find({}, {"_id": 0}))

@router.get("/tickets", response_model=List[Ticket])
def get_tickets():
    return list(db.tickets.find({}, {"_id": 0}))

@router.get("/users", response_model=List[Usuario])
def get_usuarios():
    return list(db.users.find({}, {"_id": 0}))

## POST
@router.post("/createCorporations", response_model=Empresa)
def create_empresa(empresa: Empresa):
    db.corporations.insert_one(empresa.dict())
    return empresa

@router.post("/createProyects", response_model=Proyecto)
def create_proyecto(proyecto: Proyecto):
    db.proyects.insert_one(proyecto.dict())
    return proyecto

@router.post("/createTickets", response_model=Ticket)
def create_ticket(ticket: Ticket):
    db.tickets.insert_one(ticket.dict())
    return ticket

@router.post("/createUsers", response_model=Usuario)
def create_usuario(usuario: Usuario):
    db.users.insert_one(usuario.dict())
    return usuario

@router.post("/ticketsComents/{id_ticket}/comentarios", response_model=Ticket)
def add_comentario(id_ticket: int, comentario_data: ComentarioRequest):
    ticket = db.tickets.find_one({"idTicket": id_ticket})
    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket no encontrado")
    nuevo_comentario = {
        "idComent": len(ticket['comentarios']) + 1,  
        "comentario": comentario_data.comentario
    }
    db.tickets.update_one({"idTicket": id_ticket}, {"$push": {"comentarios": nuevo_comentario}})
    return db.tickets.find_one({"idTicket": id_ticket}, {"_id": 0})

## PUT
@router.put("/ticketsState/{id_ticket}", response_model=Ticket)
def update_ticket_estado(id_ticket: int, estado_request: EstadoRequest):
    ticket = db.tickets.find_one({"idTicket": id_ticket})
    if ticket is None:
        raise HTTPException(status_code=404, detail="Ticket no encontrado")
    estado = estado_request.estado
    db.tickets.update_one(
        {"idTicket": id_ticket},
        {"$set": {"estado": estado}}
    )
    updated_ticket = db.tickets.find_one({"idTicket": id_ticket}, {"_id": 0})
    return updated_ticket

@router.put("/ticketsDesc/{id_ticket}", response_model=Ticket)
def update_ticket_desc(id_ticket: int, descripcion_request: DescripcionRequest):
    ticket = db.tickets.find_one({"idTicket": id_ticket})
    if ticket is None:
        raise HTTPException(status_code=404, detail="Ticket no encontrado")
    desc = descripcion_request.desc
    db.tickets.update_one(
        {"idTicket": id_ticket},
        {"$set": {"desc": desc}}
    )
    updated_ticket = db.tickets.find_one({"idTicket": id_ticket}, {"_id": 0})
    return updated_ticket