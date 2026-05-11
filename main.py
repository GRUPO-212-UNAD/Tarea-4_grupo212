
# main.py
# Sistema de Gestión Software FJ
# Integración final — Grupo 212

import logger
from cliente import Cliente, Entidad
from reserva import Reserva, ServicioNoDisponible
from servicio_base import Servicio
from servicios_derivados import ReservaSala, AlquilerEquipo, AsesoriaEspecializada

logger.separador("INICIO DEL SISTEMA SOFTWARE FJ")


logger.separador("OP 1: Registro cliente válido")
try:
    c1 = Cliente(1, "Ana García", "ana@email.com")
    print(c1.mostrar_info())
except Exception as e:
    logger.registrar_error(f"Error: {e}")


# OPERACIÓN 2 — Cliente con correo inválido

logger.separador("OP 2: Cliente con correo inválido")
try:
    c2 = Cliente(2, "Luis", "correo-invalido")
except Exception as e:
    logger.registrar_error(f"Error esperado: {e}")


# OPERACIÓN 3 — Cliente con nombre vacío

logger.separador("OP 3: Cliente con nombre vacío")
try:
    c3 = Cliente(3, "", "valid@email.com")
except Exception as e:
    logger.registrar_error(f"Error esperado: {e}")


# OPERACIÓN 4 — Crear servicios válidos

logger.separador("OP 4: Crear servicios válidos")
try:
    sala = ReservaSala("S001", "Sala Ejecutiva", 100)
    equipo = AlquilerEquipo("E001", "Laptop Dell", 50)
    asesoria = AsesoriaEspecializada("A001", "Consultoría TI", 200)
    logger.registrar_evento("Servicios creados correctamente")
except Exception as e:
    logger.registrar_error(f"Error: {e}")


# OPERACIÓN 5 — Calcular costos

logger.separador("OP 5: Calcular costos de servicios")
try:
    costo_sala = sala.calcular_costo(3)
    logger.registrar_evento(f"Costo sala 3h: ${costo_sala}")

    costo_equipo = equipo.calcular_costo(5)
    logger.registrar_evento(f"Costo equipo 5 dias: ${costo_equipo}")

    costo_asesoria = asesoria.calcular_costo(2, descuento=0.10)
    logger.registrar_evento(f"Costo asesoria 2h con descuento: ${costo_asesoria}")
except Exception as e:
    logger.registrar_error(f"Error: {e}")


# OPERACIÓN 6
logger.separador("OP 6: Reserva exitosa")
try:
    r1 = Reserva(c1, sala, 3)
    r1.confirmar()
    r1.mostrar()
except Exception as e:
    logger.registrar_error(f"Error: {e}")

# OPERACIÓN 7
logger.separador("OP 7: Reserva servicio no disponible")
try:
    r2 = Reserva(c1, sala, 2)
    r2.confirmar()
except Exception as e:
    logger.registrar_error(f"Error: {e}")
    
# OPERACIÓN 8 — Servicio con precio inválido

logger.separador("OP 8: Servicio con precio inválido")
try:
    sala_mala = ReservaSala("S099", "Sala Mala", -100)
except Exception as e:
    logger.registrar_error(f"Error esperado: {e}")


# OPERACIÓN 9 — Calcular costo horas inválidas

logger.separador("OP 9: Calcular costo con horas inválidas")
try:
    equipo.calcular_costo(-5)
except Exception as e:
    logger.registrar_error(f"Error esperado: {e}")


# OPERACIÓN 10 — Actualizar datos cliente

logger.separador("OP 10: Actualizar datos de cliente")
try:
    c1.set_nombre("Ana García Actualizada")
    logger.registrar_evento(f"Nombre actualizado: {c1.get_nombre()}")
    c1.set_correo("correo-invalido")
except Exception as e:
    logger.registrar_error(f"Error esperado: {e}")

logger.separador("FIN DEL SISTEMA SOFTWARE FJ")