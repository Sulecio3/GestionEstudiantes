class Actividad:
    def __init__(self, titulo, fecha, categoria, prioridad):
        self.titulo = titulo
        self.fecha = fecha
        self.categoria = categoria
        self.prioridad = prioridad

class GestorActividades:
    def __init__(self):
        self.actividades = []

    def agregar_actividad(self):
        print("\n--- Agregar nueva actividad ---")
        titulo = input("Ingrese el título de la actividad: ")
        fecha = input("Ingrese la fecha (ejemplo: YYYY-MM-DD): ")
        categoria = input("Ingrese la categoría (clase, tarea, examen, reunion, evento, personal): ").lower()
        try:
            prioridad = int(input("Ingrese la prioridad (1 a 5): "))
        except ValueError:
            print("La prioridad debe ser un número entero.")
            return
        if titulo == "":
            print("El título no puede estar vacío.")
            return
        if fecha == "":
            print("La fecha no puede estar vacía.")
            return
        if prioridad < 1 or prioridad > 5:
            print("La prioridad debe estar entre 1 y 5.")
            return

        nueva = Actividad(titulo, fecha, categoria, prioridad)
        self.actividades.append(nueva)
        print("Actividad agregada con éxito.")

    def buscar_por_palabra_clave(self):
        print("\n--- Buscar actividades por palabra clave ---")
        palabra = input("Ingrese una palabra clave: ").lower()

        encontrados = []
        for act in self.actividades:
            if palabra in act.titulo.lower() or palabra in act.categoria.lower():
                encontrados.append(act)
        if encontrados:
            print(f"\nActividades encontradas con la palabra clave '{palabra}':")
            for act in encontrados:
                print(
                    f"- Título: {act.titulo}, Fecha: {act.fecha}, Categoría: {act.categoria}, Prioridad: {act.prioridad}")
        else:
            print(f"\nNo se encontraron actividades con la palabra clave '{palabra}'")

