from fastapi import FastAPI, HTTPException
from typing import List
from pymongo import MongoClient
from model.model import Empresa, Proyecto, Ticket, Usuario, Comentario

app = FastAPI()

# MongoDB connection
client = MongoClient("mongodb://localhost:27017")
db = client["fusepong"]

# Routes
## GET
@app.get("/corporations/", response_model=List[Empresa])
def get_empresas():
    return list(db.corporations.find({}, {"_id": 0}))

@app.get("/proyects/", response_model=List[Proyecto])
def get_proyectos():
    return list(db.proyects.find({}, {"_id": 0}))

@app.get("/tickets/", response_model=List[Ticket])
def get_tickets():
    return list(db.tickets.find({}, {"_id": 0}))

@app.get("/users/", response_model=List[Usuario])
def get_usuarios():
    return list(db.users.find({}, {"_id": 0}))

## POST
@app.post("/createCorporations/", response_model=Empresa)
def create_empresa(empresa: Empresa):
    db.corporations.insert_one(empresa.dict())
    return empresa

@app.post("/createProyects/", response_model=Proyecto)
def create_proyecto(proyecto: Proyecto):
    db.proyects.insert_one(proyecto.dict())
    return proyecto

@app.post("/createTickets/", response_model=Ticket)
def create_ticket(ticket: Ticket):
    db.tickets.insert_one(ticket.dict())
    return ticket

@app.post("/createUsers/", response_model=Usuario)
def create_usuario(usuario: Usuario):
    db.users.insert_one(usuario.dict())
    return usuario

@app.post("/ticketsComents/{id_ticket}/comentarios", response_model=Ticket)
def add_comentario(id_ticket: int, comentario: str):
    ticket = db.tickets.find_one({"idTicket": id_ticket})
    
    if ticket is None:
        raise HTTPException(status_code=404, detail="Ticket no encontrado")
    
    id_coment = len(ticket['comentarios']) + 1  
    nuevo_comentario = {"idComent": id_coment, "comentario": comentario}
    
    db.tickets.update_one(
        {"idTicket": id_ticket},
        {"$push": {"comentarios": nuevo_comentario}}
    )
    
    updated_ticket = db.tickets.find_one({"idTicket": id_ticket}, {"_id": 0})
    return updated_ticket

## PUT
@app.put("/ticketsState/{id_ticket}", response_model=Ticket)
def update_ticket_estado(id_ticket: int, estado: str):
    ticket = db.tickets.find_one({"idTicket": id_ticket})
    
    if ticket is None:
        raise HTTPException(status_code=404, detail="Ticket no encontrado")
    
    db.tickets.update_one(
        {"idTicket": id_ticket},
        {"$set": {"estado": estado}}
    )
    
    updated_ticket = db.tickets.find_one({"idTicket": id_ticket}, {"_id": 0})
    return updated_ticket

@app.put("/ticketsDesc/{id_ticket}", response_model=Ticket)
def update_ticket_desc(id_ticket: int, desc: str):
    ticket = db.tickets.find_one({"idTicket": id_ticket})
    
    if ticket is None:
        raise HTTPException(status_code=404, detail="Ticket no encontrado")
    
    db.tickets.update_one(
        {"idTicket": id_ticket},
        {"$set": {"desc": desc}}
    )
    
    updated_ticket = db.tickets.find_one({"idTicket": id_ticket}, {"_id": 0})
    return updated_ticket
