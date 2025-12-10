def jugar():
    print("¡Bienvenido a Buscaminas!")
    print("[1] Fácil")
    print("[2] Medio")
    print("[3] Difícil")
    dificultad = int(input("Selecciona la dificultad: "))
    
    minas = generarMinas(dificultad)
    tablero = desplegar_tablero(dificultad)
    
    for f in tablero:
        print(" ".join(f))
    
    while minas != 0:
        accion = input("¿Quieres descubrir una celda (d) o marcar una mina (m)? ")
        fila = int(input("Ingresa la fila: "))
        columna = int(input("Ingresa la columna: "))
        
        if accion == "d":
            descubrir_celda(fila, columna)
        elif accion == "m":
            marcar_mina(fila, columna)
        else:
            print("Acción no válida.")
    
def desplegar_tablero(dificultad):
    tablero = generar_tablero(dificultad)
        
    return tablero
        
def generar_tablero(dificultad):
    # agregar minas en posiciones aleatorias según la dificultad
    tablero = []
    
    for i in range(10*dificultad):
        fila = []
        for j in range(10):
            fila.append("-")
        tablero.append(fila)
    
def descubrir_celda(fila, columna):
    pass

def generarMinas(dificultad):
    # lógica para generar minas según la dificultad
    return 10 * dificultad