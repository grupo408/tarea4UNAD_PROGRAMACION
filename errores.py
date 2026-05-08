class SistemaError(Exception): #Error general del sistema
    pass

class DatoInvalidoError(SistemaError): #Error en datos ingresados
    pass
class ClienteNoEncontradoError(SistemaError): #Error cuando no se encuentra un cliente
    pass
class ServicioError(SistemaError): #Error en datos del servicio
    pass
class ServicioNoEncontradoError(SistemaError): #Error cuando no se encuentra un servicio
    pass
class ServicioNoDisponibleError(SistemaError): #Error cuando el servicio no esta disponible
    pass
class ReservaError(SistemaError): #Error en datos de la reserva
    pass
class DuracionInvalidaError(SistemaError): #Error en duración de la reserva
    pass
class CapacidadInvalidaError(SistemaError): #Error en capacidad de la reserva
    pass
