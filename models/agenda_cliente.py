from . import db
from .bases import Model, BaseConstant

class AgendaCliente(Model):
    __tablename__ = 'AgendaCliente'
    # COLUMNS
    id_agenda = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_cliente = db.Column(db.Integer, nullable=False)
    fecha = db.Column(db.Date, nullable=False)
    hora_inicio = db.Column(db.Time, nullable=False)
    hora_termino = db.Column(db.Time, nullable=False)
    ocupado = db.Column(db.Boolean, nullable=False, default=False)