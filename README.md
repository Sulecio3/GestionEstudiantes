# GestionEstudiantes
Proyecto: Gestor de Actividades

Este proyecto es un programa en Python que permite organizar y gestionar actividades de manera sencilla. El usuario puede crear, listar, buscar y eliminar actividades, además de clasificarlas según categoría y nivel de prioridad.

Clases

1. Actividad: Representa una actividad individual.

Atributos: titulo (nombre de la actividad), categoria (tipo de actividad, ej. tarea, proyecto, examen), prioridad (nivel de importancia: urgente, alta, media, baja).

Método: show() devuelve la información de la actividad en un formato legible.

2. GestorActividades: Administra todas las actividades creadas y contiene una lista interna self.actividades de objetos Actividad.

Atributos internos: categorias_validas (Clase, Tarea, Proyecto, etc.), prioridades_validas (Urgente, Alta, Media, Baja).

Métodos principales:

mostrar_menu_categorias(): imprime las categorías disponibles.

seleccion_categorias(): permite al usuario elegir una categoría válida.

seleccion_prioridad(): permite seleccionar una prioridad válida.

agregar_actividad(): solicita título, categoría y prioridad, crea la actividad y la guarda.

listar_actividades(): muestra todas las actividades registradas o indica si la lista está vacía.

buscar_por_categoria(): filtra actividades según la categoría elegida.

buscar_por_prioridad(): filtra actividades según la prioridad seleccionada.

buscar_por_palabra_clave(): busca coincidencias en los títulos de las actividades.

eliminar_actividad(): muestra la lista con índice y permite seleccionar cuál eliminar.

Menú principal

El programa ejecuta un bucle interactivo con opciones: Agregar actividad, Listar actividades, Buscar por palabra clave, Buscar por categoría, Buscar por prioridad, Eliminar actividad y Salir. El menú usa match case para dirigir al método correspondiente.

Flujo de uso: al iniciar, el programa muestra el menú principal. El usuario elige una opción, luego puede registrar, revisar, buscar o eliminar actividades. El bucle continúa hasta seleccionar “Salir”.
