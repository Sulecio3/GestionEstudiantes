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
        self.categorias_validas = []

    def agregar_actividad(self):
        print("\n--- Agregar nueva actividad ---")
        # Se piden datos
        titulo = input("Ingrese el título de la actividad: ")
        fecha = input("Ingrese la fecha (ejemplo: YYYY-MM-DD): ")
        categoria = input("Ingrese la categoría (clase, tarea, examen, reunion, evento, personal): ").lower()#SUJETA A CAMBIOS
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


    #filtros por prioridad o tipo de eventos
    def filtrar_por_prioridad(self, prioridad_buscar):
        if prioridad_buscar < 1 or prioridad_buscar > 5:
            print("⚠️ La prioridad debe estar entre 1 y 5.")
            return []

        actividades_filtradas = []
        for act in self.actividades:
            if act.prioridad == prioridad_buscar:
                actividades_filtradas.append(act)
        return actividades_filtradas

    def filtrar_por_categoria(self, categoria_buscar):
        categoria_buscar = categoria_buscar.lower()

        if categoria_buscar not in self.categorias_validas:
            print(f"⚠️ Categoria no valida. Use una de: {', '.join(self.categorias_validas)}")
            return []

        actividades_filtradas = []
        for act in self.actividades:
            if act.categoria == categoria_buscar:
                actividades_filtradas.append(act)
        return actividades_filtradas

    def filtrar_por_prioridad_y_categoria(self, prioridad_buscar, categoria_buscar):
        if prioridad_buscar < 1 or prioridad_buscar > 5:
            print("⚠️ La prioridad debe estar entre 1 y 5.")
            return []

        categoria_buscar = categoria_buscar.lower()

        if categoria_buscar not in self.categorias_validas:
            print(f"⚠️ Categoría no valida. Use una de: {', '.join(self.categorias_validas)}")
            return []

        actividades_filtradas = []
        for act in self.actividades:
            if act.prioridad == prioridad_buscar and act.categoria == categoria_buscar:
                actividades_filtradas.append(act)
        return actividades_filtradas

    def mostrar_actividades(self, actividades, mensaje=""):
        if not actividades:
            print("No hay actividades que mostrar.")
            return

        if mensaje:
            print(f"\n{mensaje}")

        for i, actividad in enumerate(actividades, 1):
            print(f"{i}. {actividad.titulo} - {actividad.fecha} - {actividad.categoria} - Prioridad: {actividad.prioridad}")

