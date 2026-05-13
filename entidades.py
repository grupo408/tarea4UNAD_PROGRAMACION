from errores import DatoInvalidoError
from abc import ABC, abstractmethod


# =========================
# CLASE BASE GENERAL
# =========================

class EntidadGeneral(ABC):

    def __init__(self, id=None):
        self.id = id

class Cliente(EntidadGeneral):

    _contador = 1

    def __init__(self, nombre, documento, email, telefono):

        super().__init__()

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
    def id(self):
        return self.__id

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
            raise DatoInvalidoError(
                "El documento no puede estar vacío."
            )

        if not valor.strip().isdigit():
            raise DatoInvalidoError(
                "El documento debe contener solo números."
            )

        self.__documento = valor.strip()

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, valor):

        if not valor or not valor.strip():
            raise DatoInvalidoError(
                "El email no puede estar vacío."
            )

        if "@" not in valor or "." not in valor:
            raise DatoInvalidoError(
                "El email no tiene un formato válido."
            )

        self.__email = valor.strip()

    @property
    def telefono(self):
        return self.__telefono

    @telefono.setter
    def telefono(self, valor):

        if not valor or not valor.strip():
            raise DatoInvalidoError(
                "El teléfono no puede estar vacío."
            )

        if not valor.strip().isdigit():
            raise DatoInvalidoError(
                "El teléfono debe contener solo números."
            )

        if len(valor.strip()) < 7:
            raise DatoInvalidoError(
                "El teléfono es inválido."
            )

        self.__telefono = valor.strip()

    def describir(self):

        return (
            f"Cliente [{self.id}] | "
            f"Nombre: {self.nombre} | "
            f"Documento: {self.documento} | "
            f"Email: {self.email} | "
            f"Teléfono: {self.telefono}"
        )

    def validar(self):

        return all([
            self.__nombre,
            self.__documento,
            self.__email,
            self.__telefono
        ])

    def __str__(self):

        return (
            f"{self.nombre} "
            f"({self.documento})"
        )


# =========================
# SERVICIO BASE
# =========================

class Servicio(EntidadGeneral, ABC):

    def __init__(
        self,
        id=None,
        nombre=None,
        precio_hora=0.0
    ):

        super().__init__(id)

        if not nombre or not nombre.strip():
            raise DatoInvalidoError(
                "El nombre del servicio no puede estar vacío."
            )

        if precio_hora <= 0:
            raise DatoInvalidoError(
                "El precio por hora debe ser mayor que cero."
            )

        self.nombre = nombre.strip()
        self.precio_hora = precio_hora

    def __str__(self):

        return (
            f"{self.nombre} "
            f"- ${self.precio_hora:.2f}/hora"
        )

    @abstractmethod
    def describir(self):
        pass

    def validar_parametros(
        self,
        duracion_horas=None,
        impuestos=None,
        descuento=None
    ):

        if (
            duracion_horas is not None and
            duracion_horas <= 0
        ):
            raise DatoInvalidoError(
                "La duración debe ser mayor que cero."
            )

        if (
            impuestos is not None and
            impuestos < 0
        ):
            raise DatoInvalidoError(
                "Los impuestos no pueden ser negativos."
            )

        if (
            descuento is not None and
            descuento < 0
        ):
            raise DatoInvalidoError(
                "El descuento no puede ser negativo."
            )

    def aplicar_impuestos_y_descuento(
        self,
        costo,
        impuestos,
        descuento
    ):

        return costo * (1 + impuestos) - descuento

    def calcular_costo(
        self,
        duracion_horas,
        impuestos=0.0,
        descuento=0.0
    ):

        self.validar_parametros(
            duracion_horas,
            impuestos,
            descuento
        )

        costo = duracion_horas * self.precio_hora

        return self.aplicar_impuestos_y_descuento(
            costo,
            impuestos,
            descuento
        )


# =========================
# RESERVA DE SALAS
# =========================

class ServicioReservaSalas(Servicio):

    def __init__(
        self,
        id=None,
        nombre="Reserva de Sala",
        sala_numero=None,
        precio_hora=0.0
    ):

        super().__init__(
            id,
            nombre,
            precio_hora
        )

        if sala_numero is None:
            raise DatoInvalidoError(
                "Debe indicar el número de sala."
            )

        self.sala_numero = sala_numero

    def describir(self):

        return (
            f"Reserva Sala #{self.sala_numero} "
            f"- ${self.precio_hora:.2f}/hora"
        )


# =========================
# ALQUILER EQUIPOS
# =========================

class ServicioAlquilerEquipos(Servicio):

    def __init__(
        self,
        id=None,
        nombre="Alquiler de Equipos",
        equipo_tipo=None,
        precio_hora=0.0
    ):

        super().__init__(
            id,
            nombre,
            precio_hora
        )

        if not equipo_tipo:
            raise DatoInvalidoError(
                "Debe indicar el tipo de equipo."
            )

        self.equipo_tipo = equipo_tipo

    def describir(self):

        return (
            f"Alquiler Equipo: {self.equipo_tipo} "
            f"- ${self.precio_hora:.2f}/hora"
        )


# =========================
# ASESORÍAS
# =========================

class ServicioAsesoriasEspecializadas(Servicio):

    def __init__(
        self,
        id=None,
        nombre="Asesoría Especializada",
        especialidad=None,
        precio_hora=0.0
    ):

        super().__init__(
            id,
            nombre,
            precio_hora
        )

        if not especialidad:
            raise DatoInvalidoError(
                "Debe indicar la especialidad."
            )

        self.especialidad = especialidad

    def describir(self):

        return (
            f"Asesoría en {self.especialidad} "
            f"- ${self.precio_hora:.2f}/hora"
        )
