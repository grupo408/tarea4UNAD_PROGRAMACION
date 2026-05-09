from datetime import datetime #Devuelve la fecha y hora actual del sistema

class Logger:
    @staticmethod
    def log(mensaje):
        with open("logs.txt", "a") as f:
            f.write(f"{datetime.now()} - {mensaje}\n")

    @staticmethod
    def info(mensaje):
        Logger.log(f"INFO: {mensaje}")

    @staticmethod
    def error(mensaje):
        Logger.log(f"ERROR: {mensaje}")