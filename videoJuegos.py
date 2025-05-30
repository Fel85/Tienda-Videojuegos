# Función para agregar un nuevo juego al inventario
def agregar_juego(juegos):
    # Pide el nombre del juego y strip para elimnar espacion en blanco, strip es opcional solo es para que vayan teniendo acceso a mas herramientas
    nombre = input("Ingrese el nombre del juego: ").strip()  
    while True:
        try:
            # Pide el precio y valida que sea un número entero (moneda chilena)            
            precio = int(input("Ingrese el precio del juego: "))  
            break
        except ValueError:
            print("Por favor, ingrese un número válido para el precio.")
    # Agrega el juego como DICCIONARIO a la LISTA      
    juegos.append({"nombre": nombre, "precio": precio})  
    print(f"Juego '{nombre}' agregado exitosamente.\n")
# Función para mostrar todos los juegos registrados
def mostrar_juegos(juegos):
    if not juegos:
        print("No hay juegos registrados.\n")
        return
    print("=== Lista de Juegos ===")
    # Recorre e imprime los juegos con su número por eso la funcion "Enumerate"
     for i, juego in enumerate(juegos, 1):  
        print(f"{i}. {juego['nombre']} - ${juego['precio']}")
    print()

# Función para buscar un juego por su nombre
def buscar_juego(juegos, nombre):
    # Compara sin importar mayúsculas/minúsculas pues lo pasamos todo a minusculas con lower
    encontrados = [j for j in juegos if j['nombre'].lower() == nombre.lower()]
    if encontrados:
        for j in encontrados:
            print(f"Juego encontrado: {j['nombre']} - ${j['precio']}\n")
    else:
        print("Juego no encontrado.\n")

# Función para calcular el precio promedio de todos los juegos
def calcular_promedio(juegos):
    if not juegos:
        print("No hay juegos para calcular el promedio.\n")
        return
    promedio = sum(j['precio'] for j in juegos) / len(juegos)  # Suma todos los precios y divide entre la cantidad de juegos
    print(f"El precio promedio de los juegos es: ${promedio}\n")

# Función para filtrar juegos con precio mayor a un valor dado
def filtrar_por_precio(juegos, precio_min):
    # Crea una lista con juegos cuyo precio es mayor al mínimo ingresado
    filtrados = [j for j in juegos if j['precio'] > precio_min]
    if filtrados:
        print(f"Juegos con precio mayor a ${precio_min}:")
        for j in filtrados:
            print(f"- {j['nombre']} - ${j['precio']}")
        print()
    else:
        print("No se encontraron juegos con ese criterio.\n")


juegos = [] #esta es la lista que iremos llenando con diccionarios (JSON)
while True:
    print("====== MENÚ ======")
    print("1. Agregar nuevo juego")
    print("2. Ver lista de juegos")
    print("3. Buscar juego por nombre")
    print("4. Calcular promedio de precios")
    print("5. Filtrar juegos por precio mínimo")
    print("6. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        agregar_juego(juegos)
    elif opcion == "2":
        mostrar_juegos(juegos)
    elif opcion == "3":
        nombre = input("Ingrese el nombre del juego a buscar: ")
        buscar_juego(juegos, nombre)
    elif opcion == "4":
        calcular_promedio(juegos)
    elif opcion == "5":
        try:
            precio_min = int(input("Ingrese el precio mínimo: "))
            filtrar_por_precio(juegos, precio_min)
        except ValueError:
            print("Por favor, ingrese un número válido.\n")
    elif opcion == "6":
        print("Saliendo del programa.....")
        break
    else:
        print("Opción no válida. Intente de nuevo.\n")

