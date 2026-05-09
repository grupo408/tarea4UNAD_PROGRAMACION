from datetime import datetime
from errores import ReservaError, DuracionInvalidaError, DatoInvalidoError
from logger import logger

class Reserva:
    _contador = 1
    def __init__(self, cliente, servicio, duracion):
        if not duracion or duracion <= 0:
            raise DuracionInvalidaError("La duración debe ser mayor a cero.")
        self.__id = Reserva._contador
        Reserva._contador += 1
        self.__fecha = datetime.now()
        self.__cliente = cliente
        self.__servicio = servicio
        self.__duracion = duracion
        self.__estado = "Pendiente" 
        

    def confirmar(self):
        try:
            if self.__estado != "Pendiente":
                raise ReservaError("La reserva ya ha sido confirmada o cancelada.")
        except ReservaError as e:
            logger.error(f"Error al confirmar reserva: {e}")
            raise
        else:
            self.__estado = "Confirmada"
            logger.info(f"Reserva confirmada para cliente {self.__cliente.nombre} con servicio {self.__servicio.nombre}.")

    def cancelar(self):
        try:
            if self.__estado == "Cancelada":
                raise ReservaError("La reserva ya fue cancelada.")
            if self.__estado == "Pendiente":
                raise ReservaError("La reserva no ha sido confirmada, no se puede cancelar.")
            self.__estado = "Cancelada"
            logger.info(f"Reserva cancelada para cliente {self.__cliente.nombre} con servicio {self.__servicio.nombre}.")
        except ReservaError as e:   
            logger.error(f"Error al cancelar reserva: {e}")
            raise
        finally:
            logger.info(f"Reserva cancelada para cliente {self.__cliente.nombre} con servicio {self.__servicio.nombre}.")

    def procesar(self):
        try:
            if not self.__cliente.validar():
                raise DatoInvalidoError("Datos del cliente no válidos.")
            if not self.__servicio:
                raise DatoInvalidoError("Servicio no válido.")
            self.confirmar()
        except (DatoInvalidoError, ReservaError) as e:
            logger.error(f"Error al procesar reserva: {e}")
            raise ReservaError("No se pudo procesar la reserva") from e
        finally:
            logger.info(f"Intento de procesamiento registrado [{self.__id}]")
    
    def describir(self):
        return f"Reserva #{self.__id} para cliente {self.__cliente.nombre} con servicio {self.__servicio.nombre} por {self.__duracion} horas. Estado: {self.__estado}"
    def validar(self):
        return all([self.__cliente, self.__servicio, self.__duracion])