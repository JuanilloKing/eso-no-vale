import sys
import random 

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
    Muestra 'A' (Agua), 'H' (Hit/Impacto), 'M' (Miss/Agua fallada) y 'B' (Barco).
    """
    columnas = len(matriz[0])
    
    etiquetas_columnas = " " * 3 + " ".join([chr(65 + i) for i in range(columnas)])
    print(f"\n {"Jugador 1: " + nombre_tablero.upper()}")
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
            elif casilla == 'M':  
                visual_fila.append('M')
            else:
                visual_fila.append('.')
        
        contenido_fila = " ".join(visual_fila)
        print(f"{etiqueta_fila}{contenido_fila}")
        
def esta_vivo(matriz):
    """
    Recorre la matriz para verificar si queda algún barco ('B').
    Retorna True si hay al menos un barco vivo, False si no queda ninguno.
    """
    for fila in matriz:
        for casilla in fila:
            if casilla == 'B':
                return True  
    return False


def colocar_barcos_aleatorios(tablero, barcos_a_colocar):
    """Coloca los barcos del diccionario en el tablero de forma aleatoria."""
    
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

def juego():
    """Bucle que dirige el programa de todo el juego"""
    print("-" * 50)
    print("INICIALIZANDO NUEVA PARTIDA...")
    nombre = input("Introduce tu nombre para jugar: ")
    
    tablero_maquina_oculto = crear_matriz_base(tamano_tablero)
    tablero_maquina_oculto = colocar_barcos_aleatorios(tablero_maquina_oculto, barcos)
    
    tablero_jugador_ataque = crear_matriz_base(tamano_tablero)
    tablero_jugador = crear_matriz_base(tamano_tablero)
    colocar_barcos_aleatorios(tablero_jugador, barcos)
    
    print("\nBarcos del rival colocados aleatoriamente.")
    
    mostrar_tablero_consola(tablero_jugador_ataque, nombre)
    print("-" * 50)

    while esta_vivo(tablero_maquina_oculto) and esta_vivo(tablero_jugador):
        
        mostrar_tablero_consola(tablero_jugador_ataque, f"RADAR DE {nombre}")
        
        print("\n--- TU TURNO ---")
        try:
            fila = int(input("Introduce Fila (1-10): ")) - 1
            col_letra = input("Introduce Columna (A-J): ").upper()
            letras = 'ABCDEFGHIJ'

            # Verificamos que las coordenadas estén dentro del tablero
            if 0 <= fila < 10 and col_letra in letras:
                for i in range(len(letras)):
                    if letras[i] == col_letra:
                        col = i
                celda_objetivo = tablero_maquina_oculto[fila][col]

                if celda_objetivo == 'B':
                    print("¡¡IMPACTO!! Le has dado a un barco enemigo.")
                    tablero_maquina_oculto[fila][col] = 'H' # Marcamos daño en el secreto
                    tablero_jugador_ataque[fila][col] = 'H'  # Marcamos acierto en tu radar
                elif celda_objetivo == '~':
                    print("¡Agua! No has dado a nada.")
                    tablero_maquina_oculto[fila][col] = 'M'
                    tablero_jugador_ataque[fila][col] = 'M'
                else:
                    print("Eres tonto. Pierdes el turno.")
            else:
                print("Coordenadas fuera de rango. Pierdes el turno.")
        
        except ValueError:
            print("Entrada no válida. Pierdes el turno.")

        print("\n--- TURNO DE LA MÁQUINA ---")
        f_maq = random.randint(0, 9)
        c_maq = random.randint(0, 9)
        
        if tablero_jugador[f_maq][c_maq] == 'B':
            tablero_jugador[f_maq][c_maq] = 'H'
            print(f"La máquina ha disparado en {f_maq+1}{chr(c_maq+65)} y... ¡TE HA DADO!")
        elif tablero_jugador[f_maq][c_maq] == '~':
            tablero_jugador[f_maq][c_maq] = 'M'
            print(f"La máquina ha disparado en {f_maq+1}{chr(c_maq+65)} y... ha fallado.")
        else:
            print("La máquina ha disparado a una zona ya bombardeada.")

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