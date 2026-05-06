class SistemaError(Exception): #Error general del sistema
    pass

class ClienteError(SistemaError): #Error en datos del cliente
    pass

class ServicioError(SistemaError): #Error en datos del servicio
    pass

class ReservaError(SistemaError): #Error en datos de la reserva
    pass