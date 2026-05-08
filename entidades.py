from errores import DatoInvalidoError
 revert-10-Clase-cliente
from abc import ABC 
=======
servicios
from abc import ABC, abstractmethod
from logger import logger
main
> main

class EntidadGeneral(ABC):
    def __init__(self, id=None):
        self.id = id

class Cliente(EntidadGeneral):
    def __init__(self, nombre, documento, email):
        if not nombre:
            raise DatoInvalidoError("El nombre del cliente no puede estar vacío.")
        self.nombre = nombre
        self.documento = documento
        self.email = email



# Servicios
servicios
class Servicio(EntidadGeneral, ABC):
    def __init__(self, id=None, nombre=None):
        super().__init__(id)
        if not nombre:
            raise DatoInvalidoError("El nombre del servicio no puede estar vacío.")
        self.nombre = nombre
class Servicio(EntidadGeneral):
    pass
class ServicioA(Servicio):
    pass

class ServicioB(Servicio):
    pass

class ServicioC(Servicio):
    pass

main

    def __str__(self):
        return f"Servicio({self.nombre})"

    @abstractmethod
    def descripcion(self):
        raise NotImplementedError("Los servicios deben implementar una descripción.")

    @abstractmethod
    def calcular_costo(self, duracion_horas, impuestos=0.0, descuento=0.0):
        raise NotImplementedError("Los servicios deben implementar el cálculo de costo.")

    @abstractmethod
    def validar_parametros(self, duracion_horas=None, impuestos=None, descuento=None):
        raise NotImplementedError("Los servicios deben validar sus parámetros.")

    def aplicar_impuestos_y_descuento(self, costo, impuestos, descuento):
        if impuestos < 0:
            raise DatoInvalidoError("Los impuestos no pueden ser negativos.")
        if descuento < 0:
            raise DatoInvalidoError("El descuento no puede ser negativo.")
        return costo * (1 + impuestos) - descuento


class ServicioReservaSalas(Servicio):
    def __init__(self, id=None, nombre="Reserva de Sala", sala_numero=None, precio_hora=0.0):
        super().__init__(id, nombre)
        self.sala_numero = sala_numero
        self.precio_hora = precio_hora
        self.validar_parametros()

    def descripcion(self):
        return (
            f"Reserva de sala {self.sala_numero}: precio {self.precio_hora:.2f} por hora"
        )

    def validar_parametros(self, duracion_horas=None, impuestos=None, descuento=None):
        if self.precio_hora <= 0:
            raise DatoInvalidoError("El precio por hora debe ser mayor que cero.")
        if duracion_horas is not None and duracion_horas <= 0:
            raise DatoInvalidoError("La duración en horas debe ser mayor que cero.")
        if impuestos is not None and impuestos < 0:
            raise DatoInvalidoError("Los impuestos no pueden ser negativos.")
        if descuento is not None and descuento < 0:
            raise DatoInvalidoError("El descuento no puede ser negativo.")

    def calcular_costo(self, duracion_horas, impuestos=0.0, descuento=0.0):
        self.validar_parametros(duracion_horas=duracion_horas, impuestos=impuestos, descuento=descuento)
        costo = duracion_horas * self.precio_hora
        costo_final = self.aplicar_impuestos_y_descuento(costo, impuestos, descuento)
        return costo_final


class ServicioAlquilerEquipos(Servicio):
    def __init__(self, id=None, nombre="Alquiler de Equipos", equipo_tipo=None, precio_hora=0.0):
        super().__init__(id, nombre)
        self.equipo_tipo = equipo_tipo
        self.precio_hora = precio_hora
        self.validar_parametros()

    def descripcion(self):
        return f"Alquiler de equipo {self.equipo_tipo}: precio {self.precio_por_dia:.2f} por día"

    def validar_parametros(self, duracion_horas=None, impuestos=None, descuento=None):
        if self.precio_hora <= 0:
            raise DatoInvalidoError("El precio por hora debe ser mayor que cero.")
        if duracion_horas is not None and duracion_horas <= 0:
            raise DatoInvalidoError("La duración en horas debe ser mayor que cero.")
        if impuestos is not None and impuestos < 0:
            raise DatoInvalidoError("Los impuestos no pueden ser negativos.")
        if descuento is not None and descuento < 0:
            raise DatoInvalidoError("El descuento no puede ser negativo.")

    def calcular_costo(self, duracion_horas, impuestos=0.0, descuento=0.0):
        self.validar_parametros(duracion_horas=duracion_horas, impuestos=impuestos, descuento=descuento)
        costo = duracion_horas * self.precio_hora
        costo_final = self.aplicar_impuestos_y_descuento(costo, impuestos, descuento)
        return costo_final


class ServicioAsesoriasEspecializadas(Servicio):
    def __init__(self, id=None, nombre="Asesoría Especializada", especialidad=None, precio_hora=0.0):
        super().__init__(id, nombre)
        self.especialidad = especialidad
        self.precio_hora = precio_hora
        self.validar_parametros()

    def descripcion(self):
        return f"Asesoría especializada en {self.especialidad}: precio {self.precio_hora:.2f} por hora"
    
    def validar_parametros(self, duracion_horas=None, impuestos=None, descuento=None):
        if self.precio_hora <= 0:
            raise DatoInvalidoError("El precio por hora debe ser mayor que cero.")
        if duracion_horas is not None and duracion_horas <= 0:
            raise DatoInvalidoError("La duración en horas debe ser mayor que cero.")
        if impuestos is not None and impuestos < 0:
            raise DatoInvalidoError("Los impuestos no pueden ser negativos.")
        if descuento is not None and descuento < 0:
            raise DatoInvalidoError("El descuento no puede ser negativo.")
        
    def calcular_costo(self, duracion_horas, impuestos=0.0, descuento=0.0):
        self.validar_parametros(duracion_horas=duracion_horas, impuestos=impuestos, descuento=descuento)
        costo = duracion_horas * self.precio_hora
        costo_final = self.aplicar_impuestos_y_descuento(costo, impuestos, descuento)
        return costo_final

# Reservas

class Reserva:
    def __init__(self, cliente, servicio, duracion, estado):
        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = estado

    def confirmar(self):
        self.estado = "Confirmada"


