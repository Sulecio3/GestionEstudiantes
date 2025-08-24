#Se crea la clase Actividad
class Actividad:
    def __init__(self, titulo, fecha, categoria, prioridad):
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
    def agregar_actividad(self):
        print("\n--- Agregar nueva actividad ---")
        # Se piden datos
        titulo = input("Ingrese el título de la actividad: ")
        fecha = input("Ingrese la fecha (ejemplo: YYYY-MM-DD): ")
        categoria = input("Ingrese la categoría (clase, tarea, examen, reunion, evento, personal): ").lower()#SUJETA A CAMBIOS
        #La prioridad sera de 1 a 5
        try:
            prioridad = int(input("Ingrese la prioridad (1 a 5): "))
        except ValueError:
            print("La prioridad debe ser un número entero.")
            return

        nueva = Actividad(titulo, fecha, categoria, prioridad)
        self.actividades.append(nueva)
        print("Actividad agregada con éxito.")
