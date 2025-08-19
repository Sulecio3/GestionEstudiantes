#Se crea la clase Actividad
class Actividad:
    def __init__(self, titulo, fecha, categoria, prioridad):
        self.titulo = titulo
        self.fecha = fecha
        self.categoria = categoria
        self.prioridad = prioridad

#Se crea la clase que se encargara de gestionar las Actividades
class GestorActividades:
    def __init__(self):
        self.actividades = []
