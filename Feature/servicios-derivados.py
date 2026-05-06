# =========================
# SERVICIOS DERIVADOS (DIEGO)
# servicios-derivados.py
# Implementación de servicios derivados usando herencia, polimorfismo y validación de datos.
# Autor: Diego Claro Silva
# Rama: Feature/servicios-derivados 
# =========================

# IMPORTACIONES NECESARIAS
from servicio_base import Servicio
from excepciones import ErrorValidacion


# =========================
# CLASE: ReservaSala
# =========================
class ReservaSala(Servicio):

    def __init__(self, codigo, nombre, precio, disponible=True):
        super().__init__(codigo, nombre, precio, disponible)

    def calcular_costo(self, horas, tarifa=50):
        if not self.disponible:
            raise ErrorValidacion("Servicio no disponible")

        if horas <= 0:
            raise ErrorValidacion("Horas inválidas para reserva de sala")

        return horas * tarifa

    def descripcion(self):
        return f"Servicio: {self.nombre} - Reserva de sala por horas"


# =========================
# CLASE: AlquilerEquipo
# =========================
class AlquilerEquipo(Servicio):

    def __init__(self, codigo, nombre, precio, disponible=True):
        super().__init__(codigo, nombre, precio, disponible)

    def calcular_costo(self, dias, tarifa=30):
        if not self.disponible:
            raise ErrorValidacion("Servicio no disponible")

        if dias <= 0:
            raise ErrorValidacion("Días inválidos para alquiler de equipo")

        return dias * tarifa

    def descripcion(self):
        return f"Servicio: {self.nombre} - Alquiler de equipos"


# =========================
# CLASE: AsesoriaEspecializada
# =========================
class AsesoriaEspecializada(Servicio):

    def __init__(self, codigo, nombre, precio, disponible=True):
        super().__init__(codigo, nombre, precio, disponible)

    def calcular_costo(self, horas, tarifa=100, descuento=0.1):
        if not self.disponible:
            raise ErrorValidacion("Servicio no disponible")

        if horas <= 0:
            raise ErrorValidacion("Horas inválidas en asesoría")

        if not (0 <= descuento <= 1):
            raise ErrorValidacion("Descuento inválido")

        total = horas * tarifa
        return total - (total * descuento)

    def descripcion(self):
        return f"Servicio: {self.nombre} - Asesoría especializada"
