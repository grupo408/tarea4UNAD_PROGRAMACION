class Sistema:
    def __init__(self):
        self.clientes = []
        self.servicios = []
        self.reservas = []

    def agregar_cliente(self, cliente):
        self.clientes.append(cliente)

    def agregar_servicio(self, servicio):
        self.servicios.append(servicio)

    def realizar_reserva(self, reserva):
        self.reservas.append(reserva)
