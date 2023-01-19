from . import db
from .bases import Model, BaseConstant

class Especialidades(Model):
    __tablename__ = 'Especialidades'
    # COLUMNS
    id_especialidad = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_servicio = db.Column(db.Integer, nullable=False)
    nombre = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.String(100), nullable=True)
    id_profesional = db.Column(db.Integer, nullable=True)