
# excepciones.py
# Excepciones personalizadas para Software FJ


class ErrorValidacion(Exception):
    """Error de validación general del sistema"""
    pass

class ServicioNoDisponibleError(ErrorValidacion):
    """Error cuando el servicio no está disponible"""
    pass

class ParametroInvalidoError(ErrorValidacion):
    """Error cuando un parámetro es inválido"""
    pass