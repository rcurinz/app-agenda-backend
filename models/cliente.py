from . import db
from .bases import Model, BaseConstant

class Cliente(Model):
    __tablename__ = 'Cliente'
    # COLUMNS
    id_cliente = db.Column(db.Integer, primary_key=True, autoincrement=True)
    rut = db.Column(db.String(12), nullable=False, unique=True)
    nombre = db.Column(db.String(100), nullable=False)
    apellido_materno = db.Column(db.String(100), nullable=True)
    apellido_paterno = db.Column(db.String(100), nullable=False)
    codigo_telefono = db.Column(db.String(3), nullable=False, default='+56')
    telefono = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(100), nullable=False)
    direccion = db.Column(db.String(100), nullable=False)