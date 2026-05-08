
# ejemplo de importación de modulos personalizados
from logger import Logger
from entidades import Cliente
from sistema import Sistema

sistema = Sistema()

sistema.agregar_cliente(Cliente("Juan Pérez", "12345678", "juan@gmail.com"))

