from . import db
from .bases import Model, BaseConstant

class Servicios(Model):
    __tablename__ = 'Servicios'
    # COLUMNS
    id_servicio = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(100), nullable=True)
    descripcion = db.Column(db.String(100), nullable=True)
    duracion = db.Column(db.Integer, nullable=True)
    precio = db.Column(db.Integer, nullable=True)
    id_profesional = db.Column(db.Integer, nullable=True)