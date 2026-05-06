from datetime import datetime #Devuelve la fecha y hora actual del sistema

class Logger:
    @staticmethod
    def log(mensaje):
        with open("logs.txt", "a") as f:
            f.write(f"{datetime.now()} - {mensaje}\n")