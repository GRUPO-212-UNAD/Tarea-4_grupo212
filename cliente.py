# Clase base (simula la clase abstracta Entidad)
class Entidad:
    def __init__(self, id):
        if id is None:
            raise ValueError("El ID no puede ser nulo")
        self._id = id


class Cliente(Entidad):
    def __init__(self, id, nombre, correo):
        try:
            super().__init__(id)

            # Validación nombre
            if not nombre or nombre.strip() == "":
                raise ValueError("El nombre no puede estar vacío")

            # Validación correo
            if "@" not in correo or "." not in correo:
                raise ValueError("Correo electrónico inválido")

            # Encapsulación
            self.__nombre = nombre.strip()
            self.__correo = correo.strip()

        except Exception as e:
            self.registrar_error(e)
            raise

    # Getter ID
    def get_id(self):
        return self._id

    # Getter nombre
    def get_nombre(self):
        return self.__nombre

    # Setter nombre
    def set_nombre(self, nombre):
        try:
            if not nombre or nombre.strip() == "":
                raise ValueError("El nombre no puede estar vacío")
            self.__nombre = nombre.strip()
        except Exception as e:
            self.registrar_error(e)
            raise

    # Getter correo
    def get_correo(self):
        return self.__correo

    # Setter correo
    def set_correo(self, correo):
        try:
            if "@" not in correo or "." not in correo:
                raise ValueError("Correo electrónico inválido")
            self.__correo = correo.strip()
        except Exception as e:
            self.registrar_error(e)
            raise

    # Mostrar info
    def mostrar_info(self):
        return f"Cliente ID: {self._id} | Nombre: {self.__nombre} | Correo: {self.__correo}"

    # Log de errores
    def registrar_error(self, error):
        try:
            with open("logs.txt", "a") as archivo:
                archivo.write(f"Error en Cliente: {str(error)}\n")
        except:
            print("No se pudo guardar el error en el log")