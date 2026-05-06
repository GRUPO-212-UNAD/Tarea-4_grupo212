# =========================
# SERVICIOS DERIVADOS (DIEGO)
#servicios-derivados.py
#Implementación de servicios derivados usando herencia, polimorfismo y validación de datos.
#Autor: Diego Claro Silva
#Rama: Feature/servicios-derivados 
# =========================

class ReservaSala(Servicio):
    def calcular_costo(self, horas, tarifa=50):
        if horas <= 0:
            raise ErrorValidacion("Horas inválidas para reserva de sala")
        return horas * tarifa

    def descripcion(self):
        return f"Servicio: {self.nombre} - Reserva de sala por horas"


class AlquilerEquipo(Servicio):
    def calcular_costo(self, dias, tarifa=30):
        if dias <= 0:
            raise ErrorValidacion("Días inválidos para alquiler de equipo")
        return dias * tarifa

    def descripcion(self):
        return f"Servicio: {self.nombre} - Alquiler de equipos"


class AsesoriaEspecializada(Servicio):
    def calcular_costo(self, horas, tarifa=100, descuento=0.1):
        if horas <= 0:
            raise ErrorValidacion("Horas inválidas en asesoría")
        total = horas * tarifa
        return total - (total * descuento)

    def descripcion(self):
        return f"Servicio: {self.nombre} - Asesoría especializada"
