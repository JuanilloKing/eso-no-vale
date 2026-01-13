def jugar():
    dificultad = menu()
    desplegar_tablero(dificultad)
    
def menu():
    print("¡Bienvenido a Buscaminas!")
    print("[1] Fácil")
    print("[2] Medio")
    print("[3] Difícil")
    dificultad = input("Selecciona la dificultad: ")
    
    if dificultad == "1":
        return 1
    elif dificultad == "2":
        return 2
    elif dificultad == "3":
        return 3
    
def desplegar_tablero(dificultad):
    tablero = generar_tablero(dificultad)
    for fila in tablero:
        print(" ".join(fila))
        
def generar_tablero(dificultad):
    if dificultad == 1:
        return [["." for _ in range(5)] for _ in range(5)]
    elif dificultad == 2:
        return [["." for _ in range(8)] for _ in range(8)]
    elif dificultad == 3:
        return [["." for _ in range(10)] for _ in range(10)]
    