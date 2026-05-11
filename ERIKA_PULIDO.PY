from abc import ABC,abstractmethod
from datetime import datetime

# Registro de datos  automatico 

def registar_long(texto):
    with open('logs.txt','a',ecoding='utf-8')as f:
     f.write(f"[{datetime.now().strftime('%y-%m-%d %H:%M:%S')}]{texto}\n")

# ---- EXCEPCIONES ---

class ReservaError(Exception):
   pass
class ServicioNoDisponible(ReservaError):
   pass
class EstadoInvalidoError(ReservaError):
   pass


class Reserva:
   contador = 1

   def __init__(self,cliente,servcio,duracion):
      self.id_reserva=Reserva.contador
      Reserva.contador +=1

      self.cliente=cliente
      self.servicio=servcio
      self.duracion=duracion
      self.fecha=datetime.now()
      self.estado="pendiente"

   def comfirmar(self):
        try:
            if not self.servicio.disponble:
              raise ServicioNoDisponible( "El servicio no se encuentra dosponible")
            
            self.estado="comfirmada"
            self.servicio.disponible=False
            print("La reserva fue comfirmada de manera correcta")

        except ServicioNoDisponible as e:
           print("Error:",e)




