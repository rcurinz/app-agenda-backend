def prueba():
    return {"test ":"prueba"}

def getServicios():
    servicios = []
    servicios.append({"id":1,'name': 'Programacion'})
    servicios.append({"id": 2, 'name': 'Ingles'})
    servicios.append({"id": 3, 'name': 'Servicio Tecnico Computacional'})
    servicios.append({"id": 4, 'name': 'Calculo'})
    return {"servicios":servicios}


def getEspecialidades(servicio):
    especialidades = []
    if servicio == "Programacion":
        especialidades.append({"id": 1, 'name': 'Python'})
        especialidades.append({"id": 2, 'name': 'Java'})
        especialidades.append({"id": 3, 'name': 'C++'})
        especialidades.append({"id": 4, 'name': 'C#'})
        especialidades.append({"id": 5, 'name': 'PHP'})
        especialidades.append({"id": 6, 'name': 'Ruby'})
        especialidades.append({"id": 7, 'name': 'Javascript'})
        especialidades.append({"id": 8, 'name': 'NodeJS'})
        especialidades.append({"id": 9, 'name': 'AngularJS'})
        especialidades.append({"id": 10, 'name': 'ReactJS'})
        especialidades.append({"id": 11, 'name': 'VueJS'})
        especialidades.append({"id": 12, 'name': 'Swift'})
        especialidades.append({"id": 13, 'name': 'Kotlin'})
        especialidades.append({"id": 14, 'name': 'Cobol'})
        especialidades.append({"id": 15, 'name': 'Pascal'})
        especialidades.append({"id": 16, 'name': 'Fortran'})
        especialidades.append({"id": 17, 'name': 'Perl'})
        especialidades.append({"id": 18, 'name': 'Go'})
        especialidades.append({"id": 19, 'name': 'Rust'})
        especialidades.append({"id": 20, 'name': 'Scala'})
        especialidades.append({"id": 21, 'name': 'Clojure'})
        especialidades.append({"id": 22, 'name': 'Haskell'})
        especialidades.append({"id": 23, 'name': 'Erlang'})
        especialidades.append({"id": 24, 'name': 'Prolog'})
        especialidades.append({"id": 25, 'name': 'Lisp'})
        especialidades.append({"id": 26, 'name': 'Dart'})
        especialidades.append({"id": 27, 'name': 'Objective-C'})
        especialidades.append({"id": 28, 'name': 'R'})
        especialidades.append({"id": 29, 'name': 'Matlab'})
        especialidades.append({"id": 30, 'name': 'Visual Basic'})
        especialidades.append({"id": 31, 'name': 'Delphi'})
        especialidades.append({"id": 32, 'name': 'Assembly'})
    if servicio == "Ingles":
        especialidades.append({"id": 1, 'name': 'Ingles Basico'})
        especialidades.append({"id": 2, 'name': 'Ingles Intermedio'})
        especialidades.append({"id": 3, 'name': 'Ingles Avanzado'})
    if servicio == "Servicio Tecnico Computacional":
        especialidades.append({"id": 1, 'name': 'Instalacion de Software'})
        especialidades.append({"id": 2, 'name': 'Instalacion de Hardware'})
        especialidades.append({"id": 3, 'name': 'Mantenimiento de Computadores'})
        especialidades.append({"id": 4, 'name': 'Mantenimiento de Impresoras'})
        especialidades.append({"id": 5, 'name': 'Mantenimiento de Redes'})
        especialidades.append({"id": 6, 'name': 'Mantenimiento de Servidores'})
        especialidades.append({"id": 7, 'name': 'Mantenimiento de Telefonos'})
        especialidades.append({"id": 8, 'name': 'Mantenimiento de Tablets'})
        especialidades.append({"id": 9, 'name': 'Mantenimiento de Celulares'})
        especialidades.append({"id": 10, 'name': 'Mantenimiento de Videojuegos'})
        especialidades.append({"id": 11, 'name': 'Mantenimiento de Computadores Portatiles'})
        especialidades.append({"id": 12, 'name': 'Mantenimiento de Computadores de Escritorio'})
        especialidades.append({"id": 13, 'name': 'Mantenimiento de Computadores de Juegos'})
    if servicio == "Calculo":
        especialidades.append({"id": 1, 'name': 'Calculo Basico'})
        especialidades.append({"id": 2, 'name': 'Calculo Intermedio'})
        especialidades.append({"id": 3, 'name': 'Calculo Avanzado'})

    return {"especialidades":especialidades}