from errores import DatoInvalidoError
from abc import ABC 

class EntidadGeneral(ABC):
    def __init__(self, id):
        self.id = id

class Cliente(EntidadGeneral):
    def __init__(self, nombre, documento, email):
        if not nombre:
            raise DatoInvalidoError("El nombre del cliente no puede estar vacío.")
        self.nombre = nombre
        self.documento = documento
        self.email = email



# Servicios
class Servicio(EntidadGeneral):
    pass


class ServicioA(Servicio):
    pass

class ServicioB(Servicio):
    pass

class ServicioC(Servicio):
    pass



# Reservas

class Reserva:
    def __init__(self, cliente, servicio, duracion, estado):
        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = estado

    def confirmar(self):
        self.estado = "Confirmada"


