from models import *


def prueba():
    return {"test ":"prueba"}

def getServicios():
    q = Servicios.query.all()
    servicios = []
    for servicio in q:
        servicios.append({"id": servicio.id_servicio, 'name': servicio.nombre, 'descripcion': servicio.descripcion, 'duracion': servicio.duracion, 'precio': servicio.precio, 'imagen': servicio.imagen})

    return {"servicios":servicios}


def getEspecialidades(servicio):
    q = Especialidades.query.filter_by(id_servicio=servicio).all()
    print(q)
    especialidades = []
    for especialidad in q:
        especialidades.append({"id": especialidad.id_especialidad, 'name': especialidad.nombre})
    return {"especialidades":especialidades}

