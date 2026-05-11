"""
logger.py
Módulo de registro de eventos y errores para Software FJ
Autor: Angel Erick Bermudez
Rama: Feature/logger
"""

# Importamos datetime para obtener la fecha y hora actual

import os # Importamos os para construir la ruta del archivo de forma segura
from datetime import datetime


RUTA_LOG = os.path.join(os.path.dirname(__file__), "software_fj_logs.txt") # Ruta completa del archivo de log


# Función interna 
def _escribir(nivel: str, mensaje: str):

    # Obtenemos la fecha y hora actual con formato legible
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Formamos la línea completa que se va a guardar
    linea = f"[{timestamp}] [{nivel}] {mensaje}\n"

    print(linea, end="")

    # Guardamos en el archivo usando try/except para que si
    # falla la escritura, el sistema NO se detenga
    try:
        with open(RUTA_LOG, "a", encoding="utf-8") as archivo:
            archivo.write(linea)
    except OSError as e:
        print(f"[ADVERTENCIA] No se pudo escribir en el log: {e}")


# Funciones públicas 
def registrar_evento(mensaje: str):

    # Validamos que el mensaje no esté vacío antes de registrar
    if not mensaje or not isinstance(mensaje, str):
        registrar_error("Se intentó registrar un evento con mensaje inválido")
        return

    # Llamamos a la función interna con el nivel EVENTO
    _escribir("EVENTO", mensaje)


def registrar_error(mensaje: str):

    # Validamos que el mensaje no esté vacío
    if not mensaje or not isinstance(mensaje, str):
        # Si el mensaje es inválido usamos un texto por defecto
        mensaje = "Error sin descripción"

    # Llamamos a la función interna con el nivel ERROR
    _escribir("ERROR", mensaje)


def separador(titulo: str = ""):

    if titulo:
        linea = f"\n{'=' * 50}\n  {titulo}\n{'=' * 50}"
    else:
        linea = "=" * 50

    _escribir("------", linea)


# Bloque de prueba
# Este bloque solo se ejecuta cuando corres logger.py directamente
# NO se ejecuta cuando otros módulos hacen "import logger"
if __name__ == "__main__":
    print("Probando el módulo logger...\n")

    separador("INICIO DE PRUEBAS")
    registrar_evento("Sistema iniciado correctamente")
    registrar_evento("Cliente C001 registrado exitosamente")
    registrar_error("El servicio S003 no está disponible")
    registrar_error("Intento de reserva con duración inválida: -2 horas")
    registrar_evento("Reserva R001 confirmada — costo: $95.200")
    separador("FIN DE PRUEBAS")

    print("\nRevisa el archivo 'software_fj_logs.txt' para ver el resultado.")