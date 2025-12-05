print("Bienvenido al menú!")
print("¿Qué juego quieres jugar?")
print("[1] Hundir la Flota")
print("[2] Buscaminas")

opcion = input("Selecciona una opción (1 o 2): ")
if opcion == "1":
    import hundir_la_flota
    hundir_la_flota.jugar()
elif opcion == "2":
    import buscamina
    buscamina.jugar()
else:
    print("Opción no válida. Por favor, selecciona 1 o 2.")