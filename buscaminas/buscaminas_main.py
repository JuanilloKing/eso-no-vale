import random
from colorama import Fore, Style, init

COLORES = {
    "0": Fore.WHITE,
    "1": Fore.BLUE,
    "2": Fore.GREEN,
    "3": Fore.RED,
    "4": Fore.MAGENTA,
    "5": Fore.YELLOW, 
    "6": Fore.CYAN, 
    "7": Fore.WHITE, 
    "8": Fore.LIGHTRED_EX, 
    "M": Fore.LIGHTBLACK_EX
}

def jugar():
    print("¡Bienvenido a Buscaminas!")
    print("[1] Fácil")
    print("[2] Medio")
    print("[3] Difícil")
    while True:
        try:
            entrada = input("Selecciona la dificultad (1-3): ")
            dificultad = int(entrada)
            
            if 1 <= dificultad <= 3:
                break 
            else:
                print("⚠️  Opción incorrecta. Por favor, elige 1, 2 o 3.")
        except ValueError:
            print("⚠️  Entrada no válida. Por favor, introduce un número.")
                
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
        
        
        try:
            fila = int(input(f"Ingresa la fila (0-{tamaño-1}): "))
            columna = int(input(f"Ingresa la columna (0-{tamaño-1}): "))
            
            if fila < 0 or fila >= tamaño or columna < 0 or columna >= tamaño:
                print(f"❌ Coordenadas fuera de rango. Usa valores entre 0 y {tamaño-1}.")
                continue
                
        except ValueError:
            print("❌ Por favor, ingresa números válidos.")
            continue

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
    tamaño = len(tablero)
    ancho_fila = len(str(tamaño - 1))
    
    print(" " * (ancho_fila + 1), end="") 
    
    for col in range(tamaño):
        print(f"{col:2}", end=" ") 
    print() 
    
    for i, fila in enumerate(tablero):
        print(f"{i:>{ancho_fila}} |", end=" ") 
        #print(" ".join(f"{celda:2}" for celda in fila))
        for celda in fila:
            color = COLORES.get(celda, Fore.WHITE)
            print(f"{color}{celda:2}{Style.RESET_ALL}", end=" ")
        print()
    print()


def comprobar_victoria(tablero_visible, tablero_real):
    tamaño = len(tablero_real)
    for i in range(tamaño):
        for j in range(tamaño):
            if tablero_real[i][j] != "M" and tablero_visible[i][j] == "-":
                return False
    return True
