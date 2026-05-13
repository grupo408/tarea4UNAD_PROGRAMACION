# =========================
# EXCEPCIONES DEL SISTEMA
# =========================

class SistemaError(Exception):
    """
    Excepción base para todos los errores del sistema.
    """

    def __init__(self, mensaje="Error general del sistema"):
        super().__init__(mensaje)


# =========================
# ERRORES DE DATOS
# =========================

class DatoInvalidoError(SistemaError):
    """
    Error cuando los datos ingresados son inválidos.
    """

    def __init__(self, mensaje="Dato inválido"):
        super().__init__(mensaje)


# =========================
# ERRORES DE CLIENTES
# =========================

class ClienteNoEncontradoError(SistemaError):
    """
    Error cuando no se encuentra un cliente.
    """

    def __init__(self, mensaje="Cliente no encontrado"):
        super().__init__(mensaje)


# =========================
# ERRORES DE SERVICIOS
# =========================

class ServicioError(SistemaError):
    """
    Error relacionado con servicios.
    """

    def __init__(self, mensaje="Error en el servicio"):
        super().__init__(mensaje)


class ServicioNoEncontradoError(SistemaError):
    """
    Error cuando no se encuentra un servicio.
    """

    def __init__(self, mensaje="Servicio no encontrado"):
        super().__init__(mensaje)


class ServicioNoDisponibleError(SistemaError):
    """
    Error cuando el servicio no está disponible.
    """

    def __init__(self, mensaje="Servicio no disponible"):
        super().__init__(mensaje)


# =========================
# ERRORES DE RESERVAS
# =========================

class ReservaError(SistemaError):
    """
    Error relacionado con reservas.
    """

    def __init__(self, mensaje="Error en la reserva"):
        super().__init__(mensaje)


class DuracionInvalidaError(SistemaError):
    """
    Error cuando la duración es inválida.
    """

    def __init__(self, mensaje="Duración inválida"):
        super().__init__(mensaje)


class CapacidadInvalidaError(SistemaError):
    """
    Error cuando la capacidad es inválida.
    """

    def __init__(self, mensaje="Capacidad inválida"):
        super().__init__(mensaje)
