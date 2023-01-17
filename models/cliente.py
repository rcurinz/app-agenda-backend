from . import db
from .bases import Model, BaseConstant

class Cliente(Model):
    __tablename__ = 'cliente'
    # COLUMNS