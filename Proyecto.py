# Se crea la clase Actividad
class Actividad:
    def __init__(self, titulo, categoria, prioridad):
        self.titulo = titulo
        self.categoria = categoria
        self.prioridad = prioridad

    def show(self):
        return f"Titulo: {self.titulo} - Categoria: {self.categoria} - Prioridad: {self.prioridad}"

# Se crea la clase que se encargara de gestionar las Actividades
class GestorActividades:
    def __init__(self):
        self.actividades = []
        # Lista de categorías válidas
        self.categorias_validas = ["Clase", "Tarea", "Proyecto", "Examen", "Lectura", "Reunion", "Taller", "Laboratorio", "Tramite", "Ejercicio", "Social", "Oseo", "Personal"]
        # Lista de prioridades validas
        self.prioridades_validas = ["Urgente", "Alta", "Media", "Baja"]

    def mostrar_menu_categorias(self):
        print("\n--- Categorías disponibles ---")
        i = 1
        for categoria in self.categorias_validas:
            print(f"{i}. {categoria}")
            i += 1

    def seleccion_categorias(self):
        while True:
            self.mostrar_menu_categorias()
            try:
                opcion = input("\nSeleccione una categoria por su numero: ").strip()
                numero = int(opcion)
                if 1 <= numero <= len(self.categorias_validas):
                    categoria_seleccion = self.categorias_validas[numero - 1]
                    print(f'Seleccionada: {categoria_seleccion}')
                    return categoria_seleccion
                else:
                    print("ERROR. El número está fuera del rango, intentar nuevamente.")
            except ValueError:
                print("ERROR. Ingresar un número válido :(")

    def seleccion_prioridad(self):
        """Función para seleccionar prioridad con validación y reintentos"""
        while True:
            print("\n--- Niveles de prioridad ---")
            i = 1
            for p in self.prioridades_validas:
                print(f"{i}. {p}")
                i += 1
            try:
                opcion = input("Elige la prioridad: ").strip()
                numero = int(opcion)
                if 1 <= numero <= len(self.prioridades_validas):
                    prioridad = self.prioridades_validas[numero - 1]
                    return prioridad
                else:
                    print("ERROR. Número fuera de rango. Intenta nuevamente.")
            except ValueError:
                print("ERROR. Debes ingresar un número válido. Intenta nuevamente.")

    def agregar_actividad(self):
        print("\n--- Agregar nueva actividad ---")
        titulo = input("Nombre de la actividad: ")
        categoria = self.seleccion_categorias()
        prioridad = self.seleccion_prioridad()  # Usamos la función con validación

        nueva = Actividad(titulo, categoria, prioridad)
        self.actividades.append(nueva)
        print("Actividad guardada con éxito :)")

    def listar_actividades(self):
        print("\n--- Tus actividades ---")
        if not self.actividades:
            print("Aún no tienes actividades registradas :(")
            return
        i = 1
        for act in self.actividades:
            print(f"{i}. {act.show()}")
            i += 1

    def buscar_por_categoria(self):
        categoria = self.seleccion_categorias()
        encontrados = [act for act in self.actividades if act.categoria.lower() == categoria.lower()]
        if encontrados:
            print(f"\nActividades en la categoría '{categoria}':")
            for act in encontrados:
                print(f"- {act.show()}")
        else:
            print("No hay actividades en esa categoría -_-")

    def buscar_por_prioridad(self):
        """Función mejorada para buscar por prioridad con validación y reintentos"""
        prioridad = self.seleccion_prioridad()  # Usamos la misma función de validación
        encontrados = [act for act in self.actividades if act.prioridad.lower() == prioridad.lower()]
        if encontrados:
            print(f"\nActividades con prioridad '{prioridad}':")
            for act in encontrados:
                print(f"- {act.show()}")
        else:
            print("No hay actividades con esa prioridad :(")

    def buscar_por_palabra_clave(self):
        palabra = input("Escribe una palabra clave para buscar en los títulos: ").lower()
        encontrados = []
        for act in self.actividades:
            if palabra in act.titulo.lower():
                encontrados.append(act)
        if encontrados:
            print(f"\nSe encontraron estas actividades con '{palabra}':")
            for act in encontrados:
                print(f"- {act.show()}")
        else:
            print("Nada encontrado con esa palabra :(")

    def eliminar_actividad(self):
        if not self.actividades:
            print("No tienes actividades para borrar :(")
            return
        self.listar_actividades()
        try:
            opcion = int(input("\nNúmero de la actividad que quieres borrar: "))
            if 1 <= opcion <= len(self.actividades):
                eliminada = self.actividades.pop(opcion - 1)
                print(f"Actividad eliminada: '{eliminada.titulo}' :)")
            else:
                print("Ese número no existe -_-")
        except ValueError:
            print("Pon un número válido :(")

# SE CREA EL MENU PRINCIPAL
gestor = GestorActividades()
while True:
    print("\n===== Menú principal =====")
    print("1. Agregar actividad")
    print("2. Listar actividades")
    print("3. Buscar por palabra clave (en títulos)")
    print("4. Buscar por categoría")
    print("5. Buscar por prioridad")
    print("6. Eliminar actividad")
    print("7. Salir")
    try:
        opcion = int(input("Elige una opción: "))
        match opcion:
            case 1:
                gestor.agregar_actividad()
            case 2:
                gestor.listar_actividades()
            case 3:
                gestor.buscar_por_palabra_clave()
            case 4:
                gestor.buscar_por_categoria()
            case 5:
                gestor.buscar_por_prioridad()
            case 6:
                gestor.eliminar_actividad()
            case 7:
                print("Cerrando el programa... bye :)")
                break
            case _:
                print("Opción inválida -_-")
    except ValueError:
        print("Eso no fue un número :(")