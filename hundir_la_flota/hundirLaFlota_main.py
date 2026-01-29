import copy
import sys
import random
# TODO: Cuando destruyes un barco, que te lo haga saber
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
    print(f"\n {'TABLERO: ' + nombre_tablero.upper()}")
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
                visual_fila.append('💥')
            elif casilla == 'N':
                visual_fila.append('💧')
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
                fila_ataque.append('💥')
            elif casilla == 'N':
                fila_ataque.append('💧')
            else:
                fila_ataque.append('.')

        fila_defensa = []
        for casilla in matriz_defensa[i]:
            if casilla == 'B':
                fila_defensa.append('B')
            elif casilla == 'H':
                fila_defensa.append('💥')
            elif casilla == 'N':
                fila_defensa.append('💧')
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
    
    print(f"\n--- FASE DE DESPLIEGUE NAVAL ---")
    
    while not barcos_a_colocar == {}:
        mostrar_tablero_consola(tablero, "Tu flota")
        print("\nBarcos disponibles para colocar:")
        i = 1
        for nombre, longitud in barcos.items():
            if nombre in barcos_a_colocar:
                print(f"{i}- {nombre} (Tamaño: {longitud})")
            i += 1

        try:
            opcion = int(input("\nSelecciona el número del barco: "))
        except ValueError:
            print("Error: Introduce un número válido.")
            continue

        match opcion:
            case 1:
                if "Portaaviones" in barcos_a_colocar:
                    nombreBarcoSelec, longBarcoSelec, letrasValidas = "Portaaviones", 5, "ABCDEF"
                else: print("Ese barco ya está en el agua."); continue
            case 2:
                if "Acorazado" in barcos_a_colocar:
                    nombreBarcoSelec, longBarcoSelec, letrasValidas = "Acorazado", 4, "ABCDEFG"
                else: print("Ese barco ya está en el agua."); continue
            case 3:
                if "Submarino" in barcos_a_colocar:
                    nombreBarcoSelec, longBarcoSelec, letrasValidas = "Submarino", 3, "ABCDEFGH"
                else: print("Ese barco ya está en el agua."); continue
            case 4:
                if "Destructor" in barcos_a_colocar:
                    nombreBarcoSelec, longBarcoSelec, letrasValidas = "Destructor", 3, "ABCDEFGH"
                else: print("Ese barco ya está en el agua."); continue
            case 5:
                if "Lancha" in barcos_a_colocar:
                    nombreBarcoSelec, longBarcoSelec, letrasValidas = "Lancha", 2, "ABCDEFGHI"
                else: print("Ese barco ya está en el agua."); continue
            case _:
                print("Opción no válida."); continue

        print(f"\nColocando {nombreBarcoSelec}...")
        while True:
            try:
                verticalHorizontal = int(input("Orientación (1-Horizontal, 2-Vertical): "))
                if verticalHorizontal not in [1, 2]: raise ValueError
                
                fila = int(input("Fila inicial (1-10): ")) - 1
                col_letra = input("Columna inicial (A-J): ").upper()
                
                if verticalHorizontal == 1 and 0 <= fila < 10 and col_letra in letrasValidas:
                    if colocarBarcoSeleccionado(tablero, longBarcoSelec, fila, col_letra, verticalHorizontal):
                        barcos_a_colocar.pop(nombreBarcoSelec)
                        break
                elif verticalHorizontal == 2 and 0 <= fila < 11-longBarcoSelec and col_letra in "ABCDEFGHIJ":
                    if colocarBarcoSeleccionado(tablero, longBarcoSelec, fila, col_letra, verticalHorizontal):
                        barcos_a_colocar.pop(nombreBarcoSelec)
                        break
                print("Error: El barco no cabe o choca con otro. Inténtalo de nuevo.")
            except ValueError:
                print("Error: Datos de entrada incorrectos.")

    print("\n¡Toda la flota ha sido desplegada con éxito!")
    return tablero


def colocarBarcoSeleccionado(tablero, longBarcoSelec, fila, col_letra, verticalHorizontal):
    letras = "ABCDEFGHIJ"
    columna = letras.index(col_letra)

    if verticalHorizontal == 1:  # horizontal
        for i in range(longBarcoSelec):
            if tablero[fila][columna + i] == "B":
                return False
        for i in range(longBarcoSelec):
            tablero[fila][columna + i] = "B"

    elif verticalHorizontal == 2:  # vertical
        for i in range(longBarcoSelec):
            if tablero[fila + i][columna] == "B":
                return False
        for i in range(longBarcoSelec):
            tablero[fila + i][columna] = "B"
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

        disparo_valido = False
        while not disparo_valido:
            try:
                fila = int(input("Introduce Fila (1-10): ")) - 1
                col_letra = input("Introduce Columna (A-J): ").upper()
                letras = 'ABCDEFGHIJ'

                if 0 <= fila < 10 and col_letra in letras:
                    col = letras.index(col_letra)
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
                        print("Ya disparaste ahí. Vuelve a intentarlo.")
                else:
                    print("Coordenadas fuera de rango.")

            except ValueError:
                print("Entrada no válida.")

        if not esta_vivo(tablero_maquina_oculto):
            break

        print("\n--- TURNO DE LA MÁQUINA ---")
        f_maq = random.randint(0, 9)
        c_maq = random.randint(0, 9)

        if tablero_jugador[f_maq][c_maq] == 'B':
            tablero_jugador[f_maq][c_maq] = 'H'
            print(f"La máquina ha disparado en {f_maq+1}{chr(c_maq+65)}: ¡IMPACTO!")
        elif tablero_jugador[f_maq][c_maq] == '~':
            tablero_jugador[f_maq][c_maq] = 'N'
            print(f"La máquina ha disparado en {f_maq+1}{chr(c_maq+65)}: Agua.")
            
        turno += 1

    print("-" * 50)
    if esta_vivo(tablero_jugador):
        print(f"¡FELICIDADES {nombre}! Has ganado.")
    else:
        print("¡GAME OVER! La máquina ha vencido.")
    print("-" * 50)


def mostrar_menu_inicial():
    print("🚢🌊 ¡HUNDIR LA FLOTA (Battleship)! 🌊🚢")
    print("-" * 35)
    print("1. Iniciar Nuevo Juego")
    print("2. Mostrar Reglas")
    print("3. Salir")
    print("-" * 35)


def mostrar_reglas():
    print("\n📜 Reglas de Hundir la Flota 📜")
    print("---------------------------------")
    print("- Coloca tus barcos y dispara por turnos.")
    print("- 💥 = Impacto, 💧 = Agua.")
    print("- Gana quien hunda todos los barcos rivales.")
    print("---------------------------------")
    input("\nPresiona Enter para volver...")


def jugar():
    while True:
        mostrar_menu_inicial()
        opcion = input("Elige una opción (1-3): ").strip()
        if opcion == '1':
            juego()
        elif opcion == '2':
            mostrar_reglas()
        elif opcion == '3':
            sys.exit()


if __name__ == "__main__":
    jugar()
