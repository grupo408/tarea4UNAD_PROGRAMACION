```python
from datetime import datetime


class Logger:
    """
    Clase encargada de registrar eventos del sistema.
    """

    ARCHIVO_LOG = "logs.txt"

    @staticmethod
    def log(tipo, mensaje):
        """
        Registra mensajes en el archivo de logs.
        """

        fecha_hora = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )

        registro = (
            f"[{fecha_hora}] "
            f"{tipo.upper()} -> "
            f"{mensaje}\n"
        )

        try:
            with open(
                Logger.ARCHIVO_LOG,
                "a",
                encoding="utf-8"
            ) as archivo:

                archivo.write(registro)

        except Exception as error:
            print(
                f"Error al escribir en el log: {error}"
            )

    @staticmethod
    def info(mensaje):
        """
        Registra mensajes informativos.
        """

        Logger.log("INFO", mensaje)

    @staticmethod
    def warning(mensaje):
        """
        Registra advertencias del sistema.
        """

        Logger.log("WARNING", mensaje)

    @staticmethod
    def error(mensaje):
        """
        Registra errores del sistema.
        """

        Logger.log("ERROR", mensaje)

    @staticmethod
    def separador():
        """
        Agrega una línea separadora en el log.
        """

        with open(
            Logger.ARCHIVO_LOG,
            "a",
            encoding="utf-8"
        ) as archivo:

            archivo.write(
                "-" * 50 + "\n"
            )
```
