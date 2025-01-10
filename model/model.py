from pydantic import BaseModel
from typing import List

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
    
class Comentario(BaseModel):
    idComent: int
    comentario: str
    
class ComentarioRequest(BaseModel):
    comentario: str
    
class EstadoRequest(BaseModel):
    estado: str
    
class DescripcionRequest(BaseModel):
    desc: str

class Ticket(BaseModel):
    idTicket: int
    desc: str
    comentarios: List[Comentario]
    estado: str
    proyectoFK: int
    usuarioFK: int

class Usuario(BaseModel):
    idUser: int
    nombre: str
    correo: str
    contrasena: str
