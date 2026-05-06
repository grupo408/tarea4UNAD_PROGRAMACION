
# ejemplo de importación de modulos personalizados
from logger import Logger
from entidades import Cliente

cliente_prueba = Cliente("Juan Perez", "123456789", "juan@perez.com")

Logger.log("Iniciando el programa...")