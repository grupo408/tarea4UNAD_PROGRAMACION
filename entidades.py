from errores import DatoInvalidoError
from abc import ABC 
from logger import logger

class EntidadGeneral(ABC):
    def __init__(self, id):
        self.id = id

class Cliente(EntidadGeneral):
    _contador = 1
    def __init__(self, nombre, documento, email, telefono):
        self.__id = Cliente._contador
        Cliente._contador += 1
        self.__nombre = None
        self.__documento = None
        self.__email = None
        self.__telefono = None
        
        self.nombre = nombre
        self.documento = documento
        self.email = email
        self.telefono = telefono
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, valor):
        if not valor or not valor.strip():
            raise DatoInvalidoError("El nombre no puede estar vacío.")  
        self.__nombre = valor 
    
    @property
    def documento(self):
        return self.__documento
    
    @documento.setter
    def documento(self, valor):
        if not valor or not valor.strip():
            raise DatoInvalidoError("El documento no puede estar vacío.")  
        if not valor.strip().isdigit():
            raise DatoInvalidoError("El documento debe contener solo dígitos.")
        self.__documento = valor
        
    @property
    def email(self):
        return self.__email    

    @email.setter
    def email(self, valor):
        if not valor or not valor.strip():
            raise DatoInvalidoError("El email no puede estar vacío.")
        if "@" not in valor or "." not in valor:
            raise DatoInvalidoError("El email no tiene un formato válido.")  
        self.__email = valor

    @property
    def telefono(self):
        return self.__telefono    

    @telefono.setter
    def telefono(self, valor):
        if not valor or not valor.strip():
            raise DatoInvalidoError("El teléfono no puede estar vacío.")
        if not valor.strip().isdigit():
            raise DatoInvalidoError("El teléfono debe contener solo numeros.")
        self.__telefono = valor
    
    def describir(self):
        return f"Cliente: [{self.__id}]:{self.nombre}, Documento: {self.documento}, Email: {self.email}, Teléfono: {self.telefono}"

    def validar(self):
        return all([self.__nombre,
                    self.__documento,
                    self.__email,
                    self.__telefono])

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


