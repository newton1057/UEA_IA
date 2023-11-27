import copy
import sys

def Obtener_Hash_Estado (Tablero):
    # Convierte la matriz en una tupla
    Tupla_Tablero = tuple(map(tuple, Tablero))
    # Calcula el hash de la tupla
    hash_valor = hash(Tupla_Tablero)
    return hash_valor

def Imprimir_Tablero (Tablero):
    Reporte_Bitacora("Tablero")
    for Fila in Tablero:
        print (Fila)
        Reporte_Bitacora(str(Fila))

def Movimiento(Tablero, Posicion, Movimientos_Realizados):
    if Tablero[Posicion[0]][Posicion[1]] == "*":
        # Regla 1:
        if Posicion[1]+1 < len(Tablero[Posicion[0]]) and 1 not in Movimientos_Realizados:
            if Tablero[Posicion[0]][Posicion[1]+1] == ' ':
                Tablero[Posicion[0]][Posicion[1]] = ' '
                Posicion[1] = Posicion[1] + 1
                Tablero[Posicion[0]][Posicion[1]] = '*'
                return 1
        # Regla 2:
        if Posicion[1]-1 >= 0 and 2 not in Movimientos_Realizados:
            if Tablero[Posicion[0]][Posicion[1]-1] == ' ':
                Tablero[Posicion[0]][Posicion[1]] = ' '
                Posicion[1] = Posicion[1] - 1
                Tablero[Posicion[0]][Posicion[1]] = '*'
                return 2
        
        # Regla 3:
        if Posicion[0]-1 >= 0 and 3 not in Movimientos_Realizados:
            if Tablero[Posicion[0]-1][Posicion[1]] == ' ':
                Tablero[Posicion[0]][Posicion[1]] = ' '
                Posicion[0] = Posicion[0] - 1
                Tablero[Posicion[0]][Posicion[1]] = '*'
                return 3
            
        # Regla 4:
        if Posicion[0]+1 < len(Tablero[Posicion[0]]) and 4 not in Movimientos_Realizados:
            if Tablero[Posicion[0]+1][Posicion[1]] == ' ':
                Tablero[Posicion[0]][Posicion[1]] = ' '
                Posicion[0] = Posicion[0] + 1
                Tablero[Posicion[0]][Posicion[1]] = '*'
                return 4
            
    if Tablero[Posicion[0]][Posicion[1]] == "|":
        # Regla 5:
        if Posicion[0]-1 >= 0 and 5 not in Movimientos_Realizados:
            if Tablero[Posicion[0]-1][Posicion[1]] == ' ':
                Tablero[Posicion[0]][Posicion[1]] = ' '
                Posicion[0] = Posicion[0] - 1
                Tablero[Posicion[0]][Posicion[1]] = '|'
                return 5
            
        # Regla 6:
        if Posicion[0]+1 < len(Tablero[Posicion[0]]) and 6 not in Movimientos_Realizados:
            if Tablero[Posicion[0]+1][Posicion[1]] == ' ':
                Tablero[Posicion[0]][Posicion[1]] = ' '
                Posicion[0] = Posicion[0] + 1
                Tablero[Posicion[0]][Posicion[1]] = '|'
                return 6

def Validar_Estado (Lista_Estado, Estado):
    if Estado in Lista_Estado:
        return True
    else:
        Lista_Estado[Estado] = Estado
        return False

def Validar_Solucion (Tablero, Tablero_Objetivo):
    if Tablero == Tablero_Objetivo:
        print ("Solución Encontrada")
        return True
    else:
        print ("Solución no encontrada")
        return False

def Encontrar_Posicion_Ficha (Tablero , Ficha):
    Posicion = []
    for i in range(len(Tablero)):
        for j in range(len(Tablero[i])):
            if Tablero[i][j] == Ficha:
                Posicion.append(i)
                Posicion.append(j)
    return Posicion

def Reporte_Bitacora (linea):
    with open('Bitacora.txt', 'a') as archivo:
        # Escribe el contenido en el archivo
        linea = linea + "\n"
        archivo.write(linea)

def Backtracking (Tablero, Tablero_Objetivo, Lista_Estado, Limite):
    if Limite <= int(Limite_Maximo):
        print ("Backtracking 🚀")
        print ("Nivel: " + str(Limite))
        Reporte_Bitacora("Nivel: " + str(Limite))
        print("🎯 Tablero")
        Imprimir_Tablero(Tablero)

        if Validar_Solucion(Tablero, Tablero_Objetivo) == False:

            Tablero_AUX = copy.deepcopy(Tablero)
            Estado = Obtener_Hash_Estado(Tablero_AUX)
            Validar_Estado(Lista_Estado, Estado)
            Reporte_Bitacora("Estado para el tablero: " + str(Estado))
            Reporte_Bitacora("")

            Posibles_Movimientos = []
            
            for i in range(4):
                Tablero_AUX = copy.deepcopy(Tablero)
                Roja = Encontrar_Posicion_Ficha(Tablero_AUX,"*")
                Movimiento_Realizado = Movimiento(Tablero_AUX, Roja, Posibles_Movimientos)
                Estado = Obtener_Hash_Estado(Tablero_AUX)
                if Movimiento_Realizado != None and Validar_Estado(Lista_Estado, Estado) == False:
                    Linea = "Ficha Roja 🟥 ✅ Movimiento Realizado: Regla " + str(Movimiento_Realizado)
                    print(Linea)
                    
                    Reporte_Bitacora(Linea)
                    Posibles_Movimientos.append(Movimiento_Realizado)
                    Backtracking(Tablero_AUX, Tablero_Objetivo, Lista_Estado, Limite+1)

            for i in range(2):
                Tablero_AUX = copy.deepcopy(Tablero)
                Amarilla = Encontrar_Posicion_Ficha(Tablero_AUX,"|")
                Movimiento_Realizado = Movimiento(Tablero_AUX, Amarilla, Posibles_Movimientos)
                Estado = Obtener_Hash_Estado(Tablero_AUX)
                
                if Movimiento_Realizado != None and Validar_Estado(Lista_Estado, Estado) == False:
                    Linea = "Ficha Amarilla 🟨 Movimiento Realizado: Regla " + str(Movimiento_Realizado)
                    print(Linea)
                    Reporte_Bitacora(Linea)
                    Posibles_Movimientos.append(Movimiento_Realizado)
                    Backtracking(Tablero_AUX, Tablero_Objetivo, Lista_Estado, Limite+1)
        else:
            Reporte_Bitacora("🚀 Solucion Encontrada 🚀")
            sys.exit()
    else:
        print ("Limite de profundidad alcanzado 😨")
        Reporte_Bitacora("Limite de profundidad alcanzado 😨")
        sys.exit()

def Definir_Fichas(Tablero, Ficha_Roja, Ficha_Amarilla):
    Tablero[Ficha_Roja[0]][Ficha_Roja[1]] = "*"
    Tablero[Ficha_Amarilla[0]][Ficha_Amarilla[1]] = "|"

def Imprimir_Tablero_Inicial (Tablero):
    print ("🎯 Tablero Inicial")
    for Fila in Tablero:
        print (Fila)

    input("Presiona Enter para continuar...")

# Se crea una matriz que representa el estado inicial del tablero.
Tablero = [
    [' ', ' ', ' '],
    [' ', ' '],
]

# Se crea una matriz que representa el estado final del tablero.
Tablero_Objetivo = [
    [' ', ' ', '*'],
    [' ', '|'],
]

Lista_Estado = {}
Limite = 0

# Ficha * es Ficha Roja
# Ficha | es Ficha Amarilla
print ("Algoritmo Backtracking 🚀")
print ("Desarrollado por: Eduardo Isaac Dávila Bernal 🤓")
print ("Matricula: 2193076785 \n")

Limite_Maximo = input("Ingrese el limite de profundidad: ")
Reporte_Bitacora("Algoritmo Backtracking 🚀")
Reporte_Bitacora("Limite de profundidad: " + str(Limite_Maximo))
Reporte_Bitacora("")

Posicion_Inicial_Roja_X = input("Ingrese la posicion inicial de la ficha roja - Eje X: ")
Posicion_Inicial_Roja_Y = input("Ingrese la posicion inicial de la ficha roja - Eje Y: ")
Posicion_Inicial_Amarilla_X = input("Ingrese la posicion inicial de la ficha amarilla - Eje X: ")
Posicion_Inicial_Amarilla_Y = input("Ingrese la posicion inicial de la ficha amarilla - Eje Y: ")
Ficha_Roja = [int(Posicion_Inicial_Roja_X), int(Posicion_Inicial_Roja_Y)]
Ficha_Amarilla = [int(Posicion_Inicial_Amarilla_X), int(Posicion_Inicial_Amarilla_Y)]
Definir_Fichas(Tablero, Ficha_Roja, Ficha_Amarilla)
Imprimir_Tablero_Inicial(Tablero)

Backtracking(Tablero, Tablero_Objetivo, Lista_Estado, Limite)