from abc import ABC 

class Entidades_generales(ABC):
    pass

class Cliente(Entidades_generales):
    def __init__(self, nombre, documento, email):
        self.nombre = nombre
        self.documento = documento
        self.email = email
