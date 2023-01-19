from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

#Models
from .profesional import Profesional
from .cliente import Cliente
from .agenda_cliente import AgendaCliente
from .agenda_del_profesional import AgendaDelProfesional
from .bases import Model, BaseConstant
from .especialidades import Especialidades
from .servicios import Servicios
