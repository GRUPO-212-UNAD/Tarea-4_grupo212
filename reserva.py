from datetime import datetime
import logger

class ReservaError(Exception):
   pass

class ServicioNoDisponible(ReservaError):
   pass

class EstadoInvalidoError(ReservaError):
   pass

class Reserva:
   contador = 1

   def __init__(self, cliente, servicio, duracion):
      self.id_reserva = Reserva.contador
      Reserva.contador += 1
      self.cliente = cliente
      self.servicio = servicio
      self.duracion = duracion
      self.fecha = datetime.now()
      self.estado = "pendiente"

   def confirmar(self):
        try:
            if not self.servicio.esta_disponible():
                raise ServicioNoDisponible("El servicio no se encuentra disponible")
            self.estado = "confirmada"
            self.servicio.set_disponible(False)
        except ServicioNoDisponible as e:
            print("Error:", e)
            logger.registrar_error(f"Reserva {self.id_reserva}: {e}")
        else:
            print("La reserva fue confirmada correctamente")
            logger.registrar_evento(f"Reserva {self.id_reserva} confirmada")
        finally:
            print("El proceso ha culminado")

   def mostrar(self):
      print(f"""
          ID Reserva: {self.id_reserva}
          Cliente: {self.cliente.get_nombre()}
          Servicio: {self.servicio.get_nombre()}
          Duración: {self.duracion}
          Estado: {self.estado}
          Fecha: {self.fecha}""") 
      