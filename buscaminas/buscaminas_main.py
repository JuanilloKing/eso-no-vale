import random

def jugar():
    print("¡Bienvenido a Buscaminas!")
    print("[1] Fácil")
    print("[2] Medio")
    print("[3] Difícil")
    dificultad = int(input("Selecciona la dificultad: "))
    
    minas = generarMinas(dificultad)
    tablero = desplegar_tablero(dificultad, minas)
    
    for f in tablero:
        print(" ".join(f))
    
    while minas != 0:
        accion = input("¿Quieres descubrir una celda (d) o marcar una mina (m)? ")
        fila = int(input("Ingresa la fila: "))
        columna = int(input("Ingresa la columna: "))
        
        if accion == "d":
            descubrir_celda(fila, columna)
        elif accion == "m":
            marcar_mina(tablero, fila, columna)
        else:
            print("Acción no válida.")
    
def desplegar_tablero(dificultad, minas):
    # lógica para desplegar el tablero según la dificultad
    tamaño = dificultad * 5
    tablero = [["-" for _ in range(tamaño)] for _ in range(tamaño)]
    
    # lógica para colocar minas en el tablero
    for _ in range(minas):
        fila = random.randint(0, tamaño - 1)
        columna = random.randint(0, tamaño - 1)
        tablero[fila][columna] = "M"
        
    return tablero
    
def descubrir_celda(fila, columna):
    pass

def generarMinas(dificultad):
    # lógica para generar minas según la dificultad
    return 10 * dificultad

def marcar_mina(tablero, fila, columna):
    for i in range(len(tablero)):
        for j in range(len(tablero)):
            if i == fila and j == columna:
                tablero[i][j] = "X"
                print("Mina marcada en ({}, {})".format(fila, columna))
                return
    
    