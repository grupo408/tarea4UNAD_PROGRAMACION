from errores import DatoInvalidoError
from abc import ABC, abstractmethod

class EntidadGeneral(ABC):
    def __init__(self, id=None):
        self.id = id

    @abstractmethod
    def describir(self):
        pass
    
    @abstractmethod
    def validar(self):
        pass

class Cliente(EntidadGeneral):
    _contador = 1
    def __init__(self, nombre, documento, email, telefono):
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
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, valor):
        if not valor or not valor.strip():
            raise DatoInvalidoError("El nombre no puede estar vacío.")
        if not all(c.isalpha() or c.isspace() for c in valor.strip()):
            raise DatoInvalidoError("El nombre solo puede contener letras.")
        self.__nombre = valor 
    
    @property
    def documento(self):
        return self.__documento
    
    @documento.setter
    def documento(self, valor):
        if not valor or not valor.strip():
            raise DatoInvalidoError("El documento no puede estar vacío.")  
        if not valor.strip().isdigit():
            raise DatoInvalidoError("El documento debe contener solo dígitos.")
        self.__documento = valor
        
    @property
    def email(self):
        return self.__email    

    @email.setter
    def email(self, valor):
        if not valor or not valor.strip():
            raise DatoInvalidoError("El email no puede estar vacío.")
        if "@" not in valor or "." not in valor:
            raise DatoInvalidoError("El email no tiene un formato válido.")  
        self.__email = valor

    @property
    def telefono(self):
        return self.__telefono    

    @telefono.setter
    def telefono(self, valor):
        if not valor or not valor.strip():
            raise DatoInvalidoError("El teléfono no puede estar vacío.")
        if not valor.strip().isdigit():
            raise DatoInvalidoError("El teléfono debe contener solo numeros.")
        self.__telefono = valor
    
    def describir(self):
        return f"Cliente: [{self.__id}]:{self.nombre}, Documento: {self.documento}, Email: {self.email}, Teléfono: {self.telefono}"

    def validar(self):
        return all([self.__nombre,
                    self.__documento,
                    self.__email,
                    self.__telefono])

# Servicios
class Servicio(EntidadGeneral, ABC):
    def __init__(self, id=None, nombre=None):
        super().__init__(id)
        if not nombre:
            raise DatoInvalidoError("El nombre del servicio no puede estar vacío.")
        self.nombre = nombre

    def __str__(self):
        return f"Servicio({self.nombre})"

    @abstractmethod
    def describir(self):
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

    def describir(self):
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

    def describir(self):
        return f"Alquiler de equipo {self.equipo_tipo}: precio {self.precio_hora:.2f} por hora"

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

    def describir(self):
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
