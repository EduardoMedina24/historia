import random

# Definir las listas iniciales de personajes, lugares y acciones
personajes = ["el valiente caballero", "la astuta hechicera", "el dragón amistoso"]
lugares = ["en el bosque encantado", "en el castillo oscuro", "en la montaña mística"]
acciones = ["enfrenta sus miedos", "encuentra un tesoro", "libera a un prisionero"]

# Función para agregar un nuevo personaje
def agregar_personaje():
    nuevo_personaje = input("Ingresa un nuevo personaje: ")
    personajes.append(nuevo_personaje)

# Función para agregar un nuevo lugar
def agregar_lugar():
    nuevo_lugar = input("Ingresa un nuevo lugar: ")
    lugares.append(nuevo_lugar)

# Función para agregar una nueva acción
def agregar_accion():
    nueva_accion = input("Ingresa una nueva acción: ")
    acciones.append(nueva_accion)

# Función para generar y mostrar la historia aleatoria
def generar_historia():
    personaje = random.choice(personajes)
    lugar = random.choice(lugares)
    accion = random.choice(acciones)
    historia = f"{personaje} {accion} {lugar}."
    print("\nHistoria generada:")
    print(historia)

# Menú de opciones
def menu():
    while True:
        print("\n--- Generador de Historias Interactivas ---")
        print("1. Agregar un nuevo personaje")
        print("2. Agregar un nuevo lugar")
        print("3. Agregar una nueva acción")
        print("4. Generar una historia aleatoria")
        print("5. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            agregar_personaje()
        elif opcion == "2":
            agregar_lugar()
        elif opcion == "3":
            agregar_accion()
        elif opcion == "4":
            generar_historia()
        elif opcion == "5":
            print("¡Gracias por usar el generador de historias!")
            break
        else:
            print("Opción no válida. Por favor, selecciona una opción del menú.")


menu()
