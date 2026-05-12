```python id="wvk1sp"
from datetime import datetime

from errores import (
    ReservaError,
    DuracionInvalidaError,
    DatoInvalidoError
)

from logger import Logger


class Reserva:

    _contador = 1

    def __init__(
        self,
        cliente,
        servicio,
        duracion
    ):

        if duracion <= 0:
            raise DuracionInvalidaError(
                "La duración debe ser mayor a cero."
            )

        if not cliente:
            raise DatoInvalidoError(
                "Debe indicar un cliente válido."
            )

        if not servicio:
            raise DatoInvalidoError(
                "Debe indicar un servicio válido."
            )

        self.__id = Reserva._contador
        Reserva._contador += 1

        self.__fecha = datetime.now()
        self.__cliente = cliente
        self.__servicio = servicio
        self.__duracion = duracion
        self.__estado = "Pendiente"

        Logger.info(
            f"Reserva creada [{self.__id}]"
        )

    @property
    def id(self):
        return self.__id

    @property
    def fecha(self):
        return self.__fecha

    @property
    def cliente(self):
        return self.__cliente

    @property
    def servicio(self):
        return self.__servicio

    @property
    def duracion(self):
        return self.__duracion

    @property
    def estado(self):
        return self.__estado

    def confirmar(self):

        if self.__estado != "Pendiente":

            Logger.error(
                f"No se pudo confirmar "
                f"la reserva [{self.__id}]"
            )

            raise ReservaError(
                "La reserva ya fue procesada."
            )

        self.__estado = "Confirmada"

        Logger.info(
            f"Reserva confirmada "
            f"[{self.__id}] "
            f"Cliente: {self.__cliente.nombre}"
        )

    def cancelar(self):

        if self.__estado == "Cancelada":

            Logger.error(
                f"La reserva [{self.__id}] "
                f"ya estaba cancelada."
            )

            raise ReservaError(
                "La reserva ya fue cancelada."
            )

        if self.__estado == "Pendiente":

            Logger.error(
                f"No se puede cancelar "
                f"la reserva [{self.__id}] "
                f"porque aún está pendiente."
            )

            raise ReservaError(
                "La reserva debe confirmarse "
                "antes de cancelarse."
            )

        self.__estado = "Cancelada"

        Logger.info(
            f"Reserva cancelada "
            f"[{self.__id}]"
        )

    def procesar(self):

        try:

            if not self.__cliente.validar():

                raise DatoInvalidoError(
                    "Datos del cliente inválidos."
                )

            if not self.__servicio:

                raise DatoInvalidoError(
                    "Servicio inválido."
                )

            self.confirmar()

            Logger.info(
                f"Reserva procesada "
                f"correctamente [{self.__id}]"
            )

        except (
            DatoInvalidoError,
            ReservaError
        ) as error:

            Logger.error(
                f"Error al procesar "
                f"reserva [{self.__id}]: {error}"
            )

            raise ReservaError(
                "No se pudo procesar la reserva."
            ) from error

    def calcular_total(
        self,
        impuestos=0.0,
        descuento=0.0
    ):

        return self.__servicio.calcular_costo(
            self.__duracion,
            impuestos,
            descuento
        )

    def describir(self):

        return (
            f"Reserva #{self.__id} | "
            f"Cliente: {self.__cliente.nombre} | "
            f"Servicio: {self.__servicio.nombre} | "
            f"Duración: {self.__duracion} horas | "
            f"Estado: {self.__estado}"
        )

    def validar(self):

        return all([
            self.__cliente,
            self.__servicio,
            self.__duracion > 0
        ])

    def __str__(self):

        return (
            f"Reserva({self.__id}) - "
            f"{self.__cliente.nombre}"
        )
```
