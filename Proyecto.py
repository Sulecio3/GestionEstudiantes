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

    def agregar_actividad(self):
        print("\n--- Agregar nueva actividad ---")
        # Se piden datos
        titulo = input("Ingrese el título de la actividad: ")
        fecha = input("Ingrese la fecha (ejemplo: YYYY-MM-DD): ")
        categoria = input("Ingrese la categoría (clase, tarea, examen, reunion, evento, personal): ").lower()
        #La pripridad sera de 1 a 5
        try:
            prioridad = int(input("Ingrese la prioridad (1 a 5): "))
        except ValueError:
            print("La prioridad debe ser un número entero.")
            return

        if titulo == "":
            print("⚠️ El título no puede estar vacío.")
            return
        if fecha == "":
            print("⚠️ La fecha no puede estar vacía.")
            return

        #Aqui habra otra validacion de CATEGORIA pero las categorias estan en posibles cambios, entonces despues se verá

        if prioridad < 1 or prioridad > 5:
            print("⚠️ La prioridad debe estar entre 1 y 5.")
            return

        nueva = Actividad(titulo, fecha, categoria, prioridad)
        self.actividades.append(nueva)
        print("Actividad agregada con éxito.")