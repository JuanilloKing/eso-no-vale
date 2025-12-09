import sys
import random 

TAMANO_TABLERO = 10
BARCOS = {
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
    Muestra 'A', 'H' (Hit/Impacto), 'M' (Miss/Agua fallada) y 'B' (Barco).
    """
    columnas = len(matriz[0])
    
    etiquetas_columnas = " " * 3 + " ".join([chr(65 + i) for i in range(columnas)])
    print(f"\n {"Jugador 1: " + nombre_tablero.upper()}")
    print(etiquetas_columnas)
    print("---" + "---" * columnas)
    
    for i, fila in enumerate(matriz):
        numero_fila = i + 1
        etiqueta_fila = f"{numero_fila:2d}|"
        
        visual_fila = []
        for casilla in fila:
            if casilla == 'A':    
                visual_fila.append('.')
            elif casilla == 'B':  
                visual_fila.append('B') 
            elif casilla == 'H':  
                visual_fila.append('💥')
            elif casilla == 'M':  
                visual_fila.append('o')
            else:
                visual_fila.append('.')
        
        contenido_fila = " ".join(visual_fila)
        print(f"{etiqueta_fila}{contenido_fila}")


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

def iniciar_juego():
    """Inicializa matrices, coloca barcos y comienza el ciclo de juego."""
    print("-" * 50)
    print("INICIALIZANDO NUEVA PARTIDA...")
    nombre = input("Introduce tu nombre para jugar: ")
    
    tablero_maquina_secreto = crear_matriz_base(TAMANO_TABLERO)
    tablero_maquina_secreto = colocar_barcos_aleatorios(tablero_maquina_secreto, BARCOS)
    
    tablero_jugador_ataque = crear_matriz_base(TAMANO_TABLERO)
    
    print("\n✅ Barcos del rival colocados aleatoriamente.")
    
    mostrar_tablero_consola(tablero_jugador_ataque, nombre)
    
    
    print("-" * 50)
    input("Presiona Enter para volver al menú...")


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

def ejecutar_menu():
    """Función principal que maneja la navegación del menú."""
    while True: 
        mostrar_menu_inicial()
        opcion = input("Elige una opción (1-3): ").strip()
        
        if opcion == '1':
            iniciar_juego()
        elif opcion == '2':
            mostrar_reglas()
        elif opcion == '3':
            salir_del_juego()
        else:
            print("❌ Opción no válida. Por favor, introduce 1, 2 o 3.")

if __name__ == "__main__":
    ejecutar_menu()