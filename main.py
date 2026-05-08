
# ejemplo de importación de modulos personalizados
from logger import Logger
from sistema import Sistema
import entidades

sistema = Sistema()

# Agregar servicios
sistema.agregar_servicio(entidades.ServicioReservaSalas(sala_numero=101, precio_hora=50.0))
sistema.agregar_servicio(entidades.ServicioAlquilerEquipos(equipo_tipo="Proyector", precio_hora=20.0))
sistema.agregar_servicio(entidades.ServicioAsesoriasEspecializadas(especialidad="Matemáticas", precio_hora=100.0))

sistema.agregar_cliente(entidades.Cliente("Juan Pérez", "12345678", "juan@gmail.com"))

