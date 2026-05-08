class SistemaError(Exception): #Error general del sistema
    pass

class DatoInvalidoError(SistemaError): #Error en datos ingresados
    pass