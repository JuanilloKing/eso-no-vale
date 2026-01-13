def play():
    print("Bienvenido al menú!")
    print("¿Qué juego quieres jugar?")
    print("[1] Hundir la Flota")
    print("[2] Buscaminas")

    opcion = input("Selecciona una opción (1 o 2): ")

    if opcion == "1":
        # Import desde subcarpeta hundir-la-flota
        from hundir_la_flota.hundirLaFlota_main import jugar
        jugar()

    elif opcion == "2":
        # Import desde subcarpeta buscaminas
        from buscaminas.buscaminas_main import jugar
        jugar()

    else:
        print("Opción no válida. Por favor, selecciona 1 o 2.")

play()