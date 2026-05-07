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
from logger import registrar_error


# =========================
# CLASE: ReservaSala
# =========================
class ReservaSala(Servicio):

    def __init__(self, codigo, nombre, precio, disponible=True):
        super().__init__(codigo, nombre, precio, disponible)

    def calcular_costo(self, horas, tarifa=50):
        try:
            if not self.disponible:
                registrar_error("ReservaSala: servicio no disponible")
                raise ErrorValidacion("Servicio no disponible")

            if horas <= 0:
                registrar_error("ReservaSala: horas inválidas")
                raise ErrorValidacion("Horas inválidas para reserva de sala")

            return horas * tarifa

        except Exception as e:
            registrar_error(f"Error en ReservaSala.calcular_costo: {e}")
            raise

    def descripcion(self):
        return f"Servicio: {self.nombre} - Reserva de sala por horas"


# =========================
# CLASE: AlquilerEquipo
# =========================
class AlquilerEquipo(Servicio):

    def __init__(self, codigo, nombre, precio, disponible=True):
        super().__init__(codigo, nombre, precio, disponible)

    def calcular_costo(self, dias, tarifa=30):
        try:
            if not self.disponible:
                registrar_error("AlquilerEquipo: servicio no disponible")
                raise ErrorValidacion("Servicio no disponible")

            if dias <= 0:
                registrar_error("AlquilerEquipo: días inválidos")
                raise ErrorValidacion("Días inválidos para alquiler de equipo")

            return dias * tarifa

        except Exception as e:
            registrar_error(f"Error en AlquilerEquipo.calcular_costo: {e}")
            raise

    def descripcion(self):
        return f"Servicio: {self.nombre} - Alquiler de equipos"


# =========================
# CLASE: AsesoriaEspecializada
# =========================
class AsesoriaEspecializada(Servicio):

    def __init__(self, codigo, nombre, precio, disponible=True):
        super().__init__(codigo, nombre, precio, disponible)

    def calcular_costo(self, horas, tarifa=100, descuento=0.1):
        try:
            if not self.disponible:
                registrar_error("Asesoria: servicio no disponible")
                raise ErrorValidacion("Servicio no disponible")

            if horas <= 0:
                registrar_error("Asesoria: horas inválidas")
                raise ErrorValidacion("Horas inválidas en asesoría")

            if not (0 <= descuento <= 1):
                registrar_error("Asesoria: descuento inválido")
                raise ErrorValidacion("Descuento inválido")

            total = horas * tarifa
            return total - (total * descuento)

        except Exception as e:
            registrar_error(f"Error en AsesoriaEspecializada.calcular_costo: {e}")
            raise

    def descripcion(self):
        return f"Servicio: {self.nombre} - Asesoría especializada"
        total = horas * tarifa
        return total - (total * descuento)

    def descripcion(self):
        return f"Servicio: {self.nombre} - Asesoría especializada"
