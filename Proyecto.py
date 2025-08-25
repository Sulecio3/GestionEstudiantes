#Se crea la clase Actividad
class Actividad:
    def __init__(self, titulo, fecha, categoria, prioridad, descripcion):
        self.titulo = titulo
        self.fecha = fecha
        self.categoria = categoria
        self.prioridad = prioridad
        self.descripcion = descripcion
    def show(self):
        return f"{self.nombre} ({self.fecha}) - {self.categoria} - Prioridad: {self.prioridad}"
#Se crea la clase que se encargara de gestionar las Actividades
class GestorActividades:
    def __init__(self):
        self.actividades = []
        self.categorias_validas = ["Clase", "Tarea", "Proyecto", "Examen", "Lectura", "Reunion", "Taller", "Laboratorio", "Tramite", "Ejercicio", "Social", "Oseo", "Personal"]
    def pedir_fecha(self):
        #Aca pedimos la fecha, primero dia, luego mes luego año
        while True:
            try:
                print("Ingrese la fecha: ")
                dia = int(input(" Día (1-31):"))
                mes = int(input(" Mes: (1-12)"))
                year = int(input(" Año: "))
                if dia < 1 or dia > 31:
                    print("ERROR. El dia debe estar entre 1 y 31")
                    continue
                if mes < 1 or mes > 12:
                    print("ERROR. El mes debe estar entre 1 y 12")
                    continue
                if year < 2000 or year > 2150:
                    print("ERROR. El año debe estar entre 2000 y 2150")
                    continue
                fecha_show = f"{dia}/{mes}/{year}"
                return fecha_show
            except ValueError:
                print('ERROR. Por favor ingresar numeros validos.')

    def convertir_fecha_a_numero(self, fecha_str):
        #Aca convertimos la fecha a un numero normal, para ordenarlo de menor a mayor
        partes = fecha_str.split('/')
        dia = int(partes[0])
        mes = int(partes[1])
        year = int(partes[2])
        numero_fecha = year * 10000 + mes * 100 + dia
        return numero_fecha

    def ordenar_por_fecha(self, actividades):
        # Creamos una lista de tuplas (número_fecha, actividad)
        actividades_con_numeros = []
        for actividad in actividades:
            numero_fecha = self.convertir_fecha_a_numero(actividad.fecha)
            actividades_con_numeros.append((numero_fecha, actividad))
        # Ordenar por el número de fecha con la funcion sort
        actividades_con_numeros.sort()
        # Extraer solo las actividades ordenadas
        actividades_ordenadas = []
        for numero, actividad in actividades_con_numeros:
            actividades_ordenadas.append(actividad)
        return actividades_ordenadas
    def validar_categoria(self, categoria):
        return categoria.lower() in self.categorias_validas
    def validad_prioridad(self, prioridad):
        prioridades_validas = ["urgente", 'alta', 'media', 'baja']
        return prioridad.lower() in prioridades_validas
    def mostrar_menu_categorias(self):
        print("\n🏷️  --- CATEGORÍAS DISPONIBLES ---")
        for i, categoria in enumerate(self.categorias_validas, 1):
            print(f"{i}. {categoria.capitalize()}")
    def seleccion_categorias(self):
        while True:
            self.mostrar_menu_categorias()
            try:
                opcion = input("\n Seleccione una categoria por su numero: ").strip()
                numero = int(opcion)
                if 1 <= numero <= len(self.categorias_validas):
                    categoria_seleccion = self.categorias_validas[numero - 1]
                    print(f'Seleccionada: {categoria_seleccion}')
                    return categoria_seleccion
                else:
                    print("ERROR. El numero esta fuera del rango, intentar nuevamente.")
            except ValueError:
                print('ERROR. Ingresar un numero valido')
    def agregar_actividad(self):
        print("\n--- Agregar nueva actividad ---")
        # Se piden datos
        titulo = input("Ingrese el título de la actividad: ")
        fecha = input("Ingrese la fecha (ejemplo: YYYY-MM-DD): ")
        categoria = input("Ingrese la categoría (clase, tarea, examen, reunion, evento, personal): ").lower()
        try:
            prioridad = int(input("Ingrese la prioridad (1 a 5): "))
        except ValueError:
            print("La prioridad debe ser un número entero.")
            return
        nueva = Actividad(titulo, fecha, categoria, prioridad)
        self.actividades.append(nueva)
        print("Actividad agregada con éxito.")

    def listar_actividades(self):
        print("\n ----- ACTIVIDADES -----")
        if not self.actividades:
            print("No hay actividades registradas.")
            return
        actividades_ordenadas = self.ordenar_por_fecha(self.actividades)
        for i, actividad in enumerate(actividades_ordenadas, 1):
            print(f"{i}. {actividad}")
        print(f"\n Por categoria:")
        for categoria in self.categorias_validas:
            count = 0
            for actividad in actividades_ordenadas:
                if actividad.categoria == categoria:
                    count += 1
                if count > 0:
                    print( f"Total general: {len(self.actividades)} actividades")

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
