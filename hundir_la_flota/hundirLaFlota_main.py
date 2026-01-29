import copy
import sys
import random
# TODO: Cambiar la 'X' de impacto del rival, por emojis
# TODO: Cuando destruyes un barco, que te lo haga saber
# TODO: mejorar la visibilidad en la colocación de barcos
tamano_tablero = 10
barcos = {
    "Portaaviones": 5,
    "Acorazado": 4,
    "Submarino": 3,
    "Destructor": 3,
    "Lancha": 2
}


def crear_matriz_base(tamano):
    """Crea y devuelve una matriz (lista de listas) inicializada"""
    return [['~'] * tamano for _ in range(tamano)]


def mostrar_tablero_consola(matriz, nombre_tablero):
    """
    Imprime un tablero de 10x10 en la consola a partir de la matriz.
    Muestra 'A' (Agua), 'H' (Hit/Impacto), 'N' (Nada (disparo en agua) ) y 'B' (Barco).
    """
    columnas = len(matriz[0])

    etiquetas_columnas = " " * 3 + \
        " ".join([chr(65 + i) for i in range(columnas)])
    print(f"\n {'Jugador 1: ' + nombre_tablero.upper()}")
    print(etiquetas_columnas)
    print("------" * columnas)

    for i, fila in enumerate(matriz):
        numero_fila = i + 1
        etiqueta_fila = f"{numero_fila:2d}|"

        visual_fila = []
        for casilla in fila:
            if casilla == 'A':
                visual_fila.append('A')
            elif casilla == 'B':
                visual_fila.append('B')
            elif casilla == 'H':
                visual_fila.append('H')
            elif casilla == 'N':
                visual_fila.append('N')
            else:
                visual_fila.append('.')

        contenido_fila = " ".join(visual_fila)
        print(f"{etiqueta_fila}{contenido_fila}")


def mostrar_ambos_tableros(matriz_ataque, matriz_defensa, nombre):
    """
    Imprime el radar y el tablero de barcos uno al lado del otro.
    """
    tamano = len(matriz_ataque)
    letras = [chr(65 + i) for i in range(tamano)]
    separador = "        "

    print(f"\n{' ' * 5}radar de ataque (Rival){' ' * 15}barcos de {nombre} (Defensa)")

    cabecera_letras = "    " + " ".join(letras)
    print(cabecera_letras + separador + cabecera_letras)
    print("    " + "-" * (tamano * 2) + separador + "    " + "-" * (tamano * 2))

    for i in range(tamano):
        fila_ataque = []
        for casilla in matriz_ataque[i]:
            if casilla == 'H':
                fila_ataque.append('X')
            elif casilla == 'N':
                fila_ataque.append('A')
            else:
                fila_ataque.append('.')

        fila_defensa = []
        for casilla in matriz_defensa[i]:
            if casilla == 'B':
                fila_defensa.append('B')
            elif casilla == 'H':
                fila_defensa.append('X')
            elif casilla == 'N':
                fila_defensa.append('A')
            else:
                fila_defensa.append('.')

        num_fila = f"{i + 1:2d} | "
        linea_a = " ".join(fila_ataque)
        linea_b = " ".join(fila_defensa)

        print(f"{num_fila}{linea_a}{separador}{num_fila}{linea_b}")


def esta_vivo(matriz):
    """
    Retorna True si hay al menos un barco vivo, False si no queda ninguno.
    """
    for fila in matriz:
        for casilla in fila:
            if casilla == 'B':
                return True
    return False


def colocar_barcos_aleatorios(tablero, barcos_a_colocar):
    """Coloca los barcos en el tablero de forma aleatoria."""

    tamano = len(tablero)

    for nombre, longitud in barcos_a_colocar.items():
        colocado = False
        while not colocado:
            orientacion = random.randint(0, 1)

            if orientacion == 0:
                fila = random.randint(0, tamano - 1)
                columna = random.randint(0, tamano - longitud)
            else:
                fila = random.randint(0, tamano - longitud)
                columna = random.randint(0, tamano - 1)

            es_valido = True
            for i in range(longitud):
                r = fila + (i if orientacion == 1 else 0)
                c = columna + (i if orientacion == 0 else 0)

                if tablero[r][c] == 'B':
                    es_valido = False
                    break

            if es_valido:
                for i in range(longitud):
                    r = fila + (i if orientacion == 1 else 0)
                    c = columna + (i if orientacion == 0 else 0)
                    tablero[r][c] = 'B'
                colocado = True

    return tablero


def colocar_barcos_jugador(tablero, barcos):
    barcos_a_colocar = barcos.copy()
    mostrar_tablero_consola(tablero, "Tu tablero actual")
    print(f"A CONTINUACIÓN DEBERÁS COLOCAR TUS BARCOS EN EL TABLERO")
    while not barcos_a_colocar == {}:

        print("Estos son los barcos que te quedan por colocar:")
        i = 1
        for nombre, longitud in barcos.items():  # Itera TODOS los barcos en orden fijo
            if nombre in barcos_a_colocar:  # Solo muestra los que aún están disponibles
                print(f"{i}- Barco: {nombre}, longitud del barco: {longitud}")
            i += 1  # Incrementa SIEMPRE para mantener numeración fija

        try:
            opcion = int(
                input("Selecciona un barco escribiendo su número para ponerlo en tu tablero: "))
        except ValueError:
            print("Introduce una opción válida")
            continue

        match opcion:
            case 1:
                if "Portaaviones" in barcos_a_colocar:
                    nombreBarcoSelec = "Portaaviones"
                    longBarcoSelec = 5
                    letrasValidas = "ABCDEF"
                    barcos_a_colocar.pop("Portaaviones")
                else:

                    print("¡Ya has colocado ese barco!")
                    continue
            case 2:
                if "Acorazado" in barcos_a_colocar:
                    nombreBarcoSelec = "Acorazado"
                    longBarcoSelec = 4
                    letrasValidas = "ABCDEFG"
                    barcos_a_colocar.pop("Acorazado")
                else:

                    print("¡Ya has colocado ese barco!")
                    continue
            case 3:
                if "Submarino" in barcos_a_colocar:
                    nombreBarcoSelec = "Submarino"
                    longBarcoSelec = 3
                    letrasValidas = "ABCDEFGH"
                    barcos_a_colocar.pop("Submarino")
                else:

                    print("¡Ya has colocado ese barco!")
                    continue
            case 4:
                if "Destructor" in barcos_a_colocar:
                    nombreBarcoSelec = "Destructor"
                    longBarcoSelec = 3
                    letrasValidas = "ABCDEFGH"
                    barcos_a_colocar.pop("Destructor")
                else:

                    print("¡Ya has colocado ese barco!")
                    continue
            case 5:
                if "Lancha" in barcos_a_colocar:
                    nombreBarcoSelec = "Lancha"
                    longBarcoSelec = 2
                    letrasValidas = "ABCDEFGHI"
                    barcos_a_colocar.pop("Lancha")
                else:

                    print("¡Ya has colocado ese barco!")
                    continue
            case _:
                print("Por favor, introduce una opción válida")
                continue

        print(
            f"Barco seleccionado: {nombreBarcoSelec}, longitud: {longBarcoSelec}")
        while True:
            verticalHorizontal = int(
                input("Selecciona como quieres poner el barco: 1-horizontal, 2- vertical: "))
            if verticalHorizontal == 1 or verticalHorizontal == 2:
                break
            print("Opción inválida")

        print("Ahora seleccionarás la casilla donde quieres posicionar el barco.\n"
              "Si seleccionaste horizontal, el barco se colocara desde la casilla seleccionada hacia la derecha\n"
              "Si seleccionaste vertical, el barco se colocará desde la casilla seleccionada hacia abajo")
        while True:
            try:
                fila = int(input("Introduce Fila (1-10): ")) - 1
            except ValueError:
                print("Introduce una fila valida por favor")
                continue

            col_letra = input("Introduce Columna (A-J): ").upper()
            if verticalHorizontal == 1 and 0 <= fila < 10 and col_letra in letrasValidas:
                if colocarBarcoSeleccionado(tablero, longBarcoSelec, fila, col_letra, verticalHorizontal):
                    break  # salió bien
            elif verticalHorizontal == 2 and 0 <= fila < 11-longBarcoSelec and col_letra in letrasValidas:
                if colocarBarcoSeleccionado(tablero, longBarcoSelec, fila, col_letra, verticalHorizontal):
                    break  # salió bien
            print("Casilla inválida o el barco no cabe en el tablero")
        mostrar_tablero_consola(tablero, "Tu tablero actual")

    return tablero


def colocarBarcoSeleccionado(tablero, longBarcoSelec, fila, col_letra, verticalHorizontal):
    letras = "ABCDEFGHIJ"
    columna = letras.index(col_letra)

    if verticalHorizontal == 1:  # horizontal
        for i in range(longBarcoSelec):
            if tablero[fila][columna + i] == "B":
                print("El barco colisiona con otro")
                return False
        for i in range(longBarcoSelec):
            tablero[fila][columna + i] = "B"

    elif verticalHorizontal == 2:  # vertical
        for i in range(longBarcoSelec):
            if tablero[fila + i][columna] == "B":
                print("El barco colisiona con otro")
                return False
        for i in range(longBarcoSelec):
            tablero[fila + i][columna] = "B"
    else:
        print("Ha ocurrido un error")
        exit()

    return True


def juego():
    """Bucle que dirige el programa de todo el juego"""
    print("-" * 50)
    print("INICIALIZANDO NUEVA PARTIDA...")
    nombre = input("Introduce tu nombre para jugar: ")

    tablero_maquina_oculto = crear_matriz_base(tamano_tablero)
    tablero_maquina_oculto = colocar_barcos_aleatorios(
        tablero_maquina_oculto, barcos)

    tablero_jugador_ataque = crear_matriz_base(tamano_tablero)
    tablero_jugador = crear_matriz_base(tamano_tablero)
    colocar_barcos_jugador(tablero_jugador, barcos)

    print("\nBarcos del rival colocados aleatoriamente.")

    print("-" * 50)
    turno = 1
    while esta_vivo(tablero_maquina_oculto) and esta_vivo(tablero_jugador):
        mostrar_ambos_tableros(tablero_jugador_ataque, tablero_jugador, nombre)
        print(f"\n--- TURNO {turno} ---")

        # MODIFICACIÓN SOLICITADA: Bucle para permitir repetir disparo
        disparo_valido = False
        while not disparo_valido:
            try:
                fila = int(input("Introduce Fila (1-10): ")) - 1
                col_letra = input("Introduce Columna (A-J): ").upper()
                letras = 'ABCDEFGHIJ'

                if 0 <= fila < 10 and col_letra in letras:
                    for i in range(len(letras)):
                        if letras[i] == col_letra:
                            col = i
                    celda_objetivo = tablero_maquina_oculto[fila][col]

                    if celda_objetivo == 'B':
                        print("¡¡IMPACTO!! Le has dado a un barco enemigo.")
                        tablero_maquina_oculto[fila][col] = 'H'
                        tablero_jugador_ataque[fila][col] = 'H'
                        disparo_valido = True
                    elif celda_objetivo == '~':
                        print("¡Agua! No has dado a nada.")
                        tablero_maquina_oculto[fila][col] = 'N'
                        tablero_jugador_ataque[fila][col] = 'N'
                        disparo_valido = True
                    else:
                        print("Pierdes el turno, disparaste a una casilla ya bombardeada.")
                        print("Vuelve a intentarlo.")
                else:
                    print("Coordenadas fuera de rango. Vuelve a intentarlo")

            except ValueError:
                print("Entrada no válida. Vuelve a intentarlo.")

        if not esta_vivo(tablero_maquina_oculto):
            break

        print("\n--- TURNO DE LA MÁQUINA ---")
        f_maq = random.randint(0, 9)
        c_maq = random.randint(0, 9)

        if tablero_jugador[f_maq][c_maq] == 'B':
            tablero_jugador[f_maq][c_maq] = 'H'
            print(
                f"La máquina ha disparado en {f_maq+1}{chr(c_maq+65)} y... ¡TE HA DADO!")
        elif tablero_jugador[f_maq][c_maq] == '~':
            tablero_jugador[f_maq][c_maq] = 'N'
            print(
                f"La máquina ha disparado en {f_maq+1}{chr(c_maq+65)} y... ha fallado.")
        else:
            print("La máquina ha disparado a una zona ya bombardeada.")
            
        turno += 1

    print("-" * 50)
    if esta_vivo(tablero_jugador):
        print(f"¡FELICIDADES {nombre}! Has hundido toda la flota enemiga.")
    else:
        print("¡GAME OVER! La máquina ha hundido toda tu flota.")
    print("-" * 50)


def mostrar_menu_inicial():
    """Muestra el menú principal del juego Hundir la Flota."""
    print("🚢🌊 ¡HUNDIR LA FLOTA (Battleship)! 🌊🚢")
    print("-" * 35)
    print("1. Iniciar Nuevo Juego")
    print("2. Mostrar Reglas")
    print("3. Salir")
    print("-" * 35)


def mostrar_reglas():
    """Muestra las reglas básicas de Hundir la Flota."""
    print("\n📜 Reglas de Hundir la Flota 📜")
    print("---------------------------------")
    print("- El juego se juega en una cuadrícula.")
    print("- Colocas tus barcos en su cuadrícula de forma secreta, y jugarás contra la maquina")
    print("- Los jugadores se turnan para disparar a coordenadas específicas del enemigo.")
    print("- Si aciertas un barco, es un 'impacto'. Si fallas, es 'agua'.")
    print("- Gana el primer jugador que hunda todos los barcos del oponente.")
    print("---------------------------------")
    input("\nPresiona Enter para volver al menú...")


def salir_del_juego():
    """Sale del programa."""
    print("\n¡Gracias por jugar! ¡Hasta pronto!")
    sys.exit()


def jugar():
    """Función principal que maneja la navegación del menú."""
    while True:
        mostrar_menu_inicial()
        opcion = input("Elige una opción (1-3): ").strip()
        if opcion == '1':
            juego()
        elif opcion == '2':
            mostrar_reglas()
        elif opcion == '3':
            salir_del_juego()
        else:
            print("Opción no válida. Por favor, introduce 1, 2 o 3.")


if __name__ == "__main__":
    jugar()
