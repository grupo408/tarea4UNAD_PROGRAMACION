from abc import ABC, abstractmethod 
from datetime import datetime #Devuelve la fecha y hora actual del sistema

#EXCEPCIONES

class SistemaError(Exception): #Error general del sistema
    pass

class ClienteError(SistemaError): #Error en datos del cliente
    pass

class ServicioError(SistemaError): #Error en datos del servicio
    pass

class ReservaError(SistemaError): #Error en datos de la reserva
    pass

# LOGGER
class Logger:
    @staticmethod
    def log(mensaje):
        with open("logs.txt", "a") as f:
            f.write(f"{datetime.now()} - {mensaje}\n")


#Clase Abstracta
class Entidades_generales(ABC):
    pass

class Cliente(Entidades_generales):
    def __init__(self, nombre, documento, email):
        self.nombre = nombre
        self.documento = documento
        self.email = email

