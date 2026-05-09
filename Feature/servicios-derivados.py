# =========================
# SERVICIOS DERIVADOS (DIEGO)
# servicios-derivados.py
# Implementación de servicios derivados usando herencia, polimorfismo y validación de datos.
# Autor: Diego Claro Silva
# Rama: Feature/servicios-derivados 
# =========================

# =========================
# IMPORTACIONES
# =========================
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
        """
        Calcula el costo de la reserva de sala
        según la cantidad de horas.
        """
        try:

            # Validar disponibilidad
            if not self.disponible:
                registrar_error(
                    "ReservaSala: servicio no disponible"
                )
                raise ErrorValidacion(
                    "Servicio no disponible"
                )

            # Validar horas
            if horas <= 0:
                registrar_error(
                    "ReservaSala: horas inválidas"
                )
                raise ErrorValidacion(
                    "Horas inválidas para reserva de sala"
                )

            # Calcular costo
            costo_total = horas * tarifa
            return costo_total

        except Exception as e:
            registrar_error(
                f"Error en ReservaSala.calcular_costo: {e}"
            )
            raise

    def descripcion(self):
        """
        Devuelve la descripción del servicio.
        """
        return (
            f"Servicio: {self.nombre} - "
            f"Reserva de sala por horas"
        )


# =========================
# CLASE: AlquilerEquipo
# =========================
class AlquilerEquipo(Servicio):

    def __init__(self, codigo, nombre, precio, disponible=True):
        super().__init__(codigo, nombre, precio, disponible)

    def calcular_costo(self, dias, tarifa=30):
        """
        Calcula el costo del alquiler
        según la cantidad de días.
        """
        try:

            # Validar disponibilidad
            if not self.disponible:
                registrar_error(
                    "AlquilerEquipo: servicio no disponible"
                )
                raise ErrorValidacion(
                    "Servicio no disponible"
                )

            # Validar días
            if dias <= 0:
                registrar_error(
                    "AlquilerEquipo: días inválidos"
                )
                raise ErrorValidacion(
                    "Días inválidos para alquiler de equipo"
                )

            # Calcular costo
            costo_total = dias * tarifa
            return costo_total

        except Exception as e:
            registrar_error(
                f"Error en AlquilerEquipo.calcular_costo: {e}"
            )
            raise

    def descripcion(self):
        """
        Devuelve la descripción del servicio.
        """
        return (
            f"Servicio: {self.nombre} - "
            f"Alquiler de equipos"
        )


# =========================
# CLASE: AsesoriaEspecializada
# =========================
class AsesoriaEspecializada(Servicio):

    def __init__(self, codigo, nombre, precio, disponible=True):
        super().__init__(codigo, nombre, precio, disponible)

    def calcular_costo(
        self,
        horas,
        tarifa=100,
        descuento=0.10
    ):
        """
        Calcula el costo de la asesoría
        aplicando descuento.
        """
        try:

            # Validar disponibilidad
            if not self.disponible:
                registrar_error(
                    "AsesoriaEspecializada: servicio no disponible"
                )
                raise ErrorValidacion(
                    "Servicio no disponible"
                )

            # Validar horas
            if horas <= 0:
                registrar_error(
                    "AsesoriaEspecializada: horas inválidas"
                )
                raise ErrorValidacion(
                    "Horas inválidas en asesoría"
                )

            # Validar descuento
            if not (0 <= descuento <= 1):
                registrar_error(
                    "AsesoriaEspecializada: descuento inválido"
                )
                raise ErrorValidacion(
                    "Descuento inválido"
                )

            # Calcular total
            total = horas * tarifa
            total_con_descuento = (
                total - (total * descuento)
            )

            return total_con_descuento

        except Exception as e:
            registrar_error(
                f"Error en AsesoriaEspecializada.calcular_costo: {e}"
            )
            raise

    def descripcion(self):
        """
        Devuelve la descripción del servicio.
        """
        return (
            f"Servicio: {self.nombre} - "
            f"Asesoría especializada"
        )
