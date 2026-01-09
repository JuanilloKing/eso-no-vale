import random

def jugar():
    print("¡Bienvenido a Buscaminas!")
    print("[1] Fácil")
    print("[2] Medio")
    print("[3] Difícil")
    dificultad = int(input("Selecciona la dificultad: "))
    
    minas = generarMinas(dificultad)
    
    tablero_real = generar_tablero(dificultad, minas)
    tamaño = len(tablero_real)
    
    tablero_visible = [["-" for _ in range(tamaño)] for _ in range(tamaño)]
    
    while True:
        mostrar_tablero(tablero_visible)

        accion = input("¿Descubrir (d), marcar mina (m) o reiniciar (r)? ").lower()
        
        if accion == "r":
            jugar()
            return
        
        if accion not in ["d", "m"]:
            print("Acción no válida.")
            continue
        
        fila = int(input("Ingresa la fila: "))
        columna = int(input("Ingresa la columna: "))

        if accion == "d":
            if tablero_real[fila][columna] == "M":
                print("💥 ¡Has pisado una mina! Juego terminado.")
                mostrar_tablero(tablero_real)
                return
            descubrir_celda(tablero_real, tablero_visible, fila, columna)

        elif accion == "m":
            marcar_mina(tablero_visible, fila, columna)

    
def generar_tablero(dificultad, minas):
    tamaño = dificultad * 10
    tablero = [["-" for _ in range(tamaño)] for _ in range(tamaño)]
    
    # Colocar minas
    minas_colocadas = 0
    while minas_colocadas < minas:
        fila = random.randint(0, tamaño - 1)
        columna = random.randint(0, tamaño - 1)
        if tablero[fila][columna] != "M":
            tablero[fila][columna] = "M"
            minas_colocadas += 1

    # Contar minas alrededor
    for i in range(tamaño):
        for j in range(tamaño):
            if tablero[i][j] != "M":
                contador = 0
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        if dx == 0 and dy == 0:
                            continue
                        ni = i + dx
                        nj = j + dy
                        if 0 <= ni < tamaño and 0 <= nj < tamaño:
                            if tablero[ni][nj] == "M":
                                contador += 1
                tablero[i][j] = str(contador)

    return tablero
    
def descubrir_celda(tablero_real, tablero_visible, fila, columna):
    tamaño = len(tablero_real)

    if fila < 0 or fila >= tamaño or columna < 0 or columna >= tamaño:
        return

    if tablero_visible[fila][columna] != "-":
        return

    tablero_visible[fila][columna] = tablero_real[fila][columna]

    if tablero_real[fila][columna] != "0":
        return

    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx != 0 or dy != 0:
                descubrir_celda(
                    tablero_real,
                    tablero_visible,
                    fila + dx,
                    columna + dy
                )


def generarMinas(dificultad):
    # lógica para generar minas según la dificultad
    return 10 * dificultad

def marcar_mina(tablero_visible, fila, columna):
    if tablero_visible[fila][columna] == "-":
        tablero_visible[fila][columna] = "⚑"
    elif tablero_visible[fila][columna] == "⚑":
        tablero_visible[fila][columna] = "-"

    
def mostrar_tablero(tablero):
    for fila in tablero:
        print(" ".join(fila))
    print()
