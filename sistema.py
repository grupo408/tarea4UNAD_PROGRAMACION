from errores import (
    ClienteNoEncontradoError,
    ServicioNoEncontradoError,
    ReservaError,
    DatoInvalidoError
)

from logger import Logger


class Sistema:

    def __init__(self):

        self.clientes = []
        self.servicios = []
        self.reservas = []

        Logger.info(
            "Sistema inicializado correctamente."
        )

    # =========================
    # CLIENTES
    # =========================

    def agregar_cliente(self, cliente):

        if not cliente:
            raise DatoInvalidoError(
                "El cliente no es válido."
            )

        self.clientes.append(cliente)

        Logger.info(
            f"Cliente agregado: "
            f"{cliente.nombre}"
        )

    def buscar_cliente_por_documento(
        self,
        documento
    ):

        for cliente in self.clientes:

            if cliente.documento == documento:
                return cliente

        Logger.error(
            f"Cliente no encontrado: {documento}"
        )

        raise ClienteNoEncontradoError(
            "No existe un cliente con ese documento."
        )

    def eliminar_cliente(
        self,
        documento
    ):

        cliente = self.buscar_cliente_por_documento(
            documento
        )

        self.clientes.remove(cliente)

        Logger.info(
            f"Cliente eliminado: "
            f"{cliente.nombre}"
        )

    # =========================
    # SERVICIOS
    # =========================

    def agregar_servicio(self, servicio):

        if not servicio:
            raise DatoInvalidoError(
                "El servicio no es válido."
            )

        self.servicios.append(servicio)

        Logger.info(
            f"Servicio agregado: "
            f"{servicio.nombre}"
        )

    def buscar_servicio_por_nombre(
        self,
        nombre
    ):

        for servicio in self.servicios:

            if servicio.nombre.lower() == nombre.lower():
                return servicio

        Logger.error(
            f"Servicio no encontrado: {nombre}"
        )

        raise ServicioNoEncontradoError(
            "No existe un servicio con ese nombre."
        )

    def eliminar_servicio(
        self,
        nombre
    ):

        servicio = self.buscar_servicio_por_nombre(
            nombre
        )

        self.servicios.remove(servicio)

        Logger.info(
            f"Servicio eliminado: "
            f"{servicio.nombre}"
        )

    # =========================
    # RESERVAS
    # =========================

    def realizar_reserva(self, reserva):

        if not reserva:
            raise ReservaError(
                "La reserva no es válida."
            )

        self.reservas.append(reserva)

        Logger.info(
            f"Reserva registrada: "
            f"{reserva.describir()}"
        )

    def listar_clientes(self):

        return [
            cliente.describir()
            for cliente in self.clientes
        ]

    def listar_servicios(self):

        return [
            servicio.describir()
            for servicio in self.servicios
        ]

    def listar_reservas(self):

        return [
            reserva.describir()
            for reserva in self.reservas
        ]

    # =========================
    # ESTADÍSTICAS
    # =========================

    def total_clientes(self):

        return len(self.clientes)

    def total_servicios(self):

        return len(self.servicios)

    def total_reservas(self):

        return len(self.reservas)

    # =========================
    # REPRESENTACIÓN
    # =========================

    def __str__(self):

        return (
            f"Sistema -> "
            f"Clientes: {len(self.clientes)} | "
            f"Servicios: {len(self.servicios)} | "
            f"Reservas: {len(self.reservas)}"
        )
