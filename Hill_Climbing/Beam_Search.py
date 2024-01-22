import copy
import sys
from queue import Queue

from colorama import init, Fore, Back, Style

def Reporte_Bitacora (linea):
    with open('Bitacora.txt', 'a') as archivo:
        # Escribe el contenido en el archivo
        linea = linea + "\n"
        archivo.write(linea)

def Crear_Tablero():
    Tablero = [
        ['*', 'R', ' ', ' ', ' ', ' '],
        ['*', '*', ' ', ' ', ' ', ' '],
        ['*', ' ', '*', ' ', ' ', ' '],
        [' ', ' ', ' ', '*', ' ', ' '],
        ['*', '*', '*', '*', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' '],
    ]

    Tablero_Objetivo = [
        ['*', ' ', ' ', ' ', ' ', ' '],
        ['*', '*', ' ', ' ', ' ', ' '],
        ['*', ' ', '*', ' ', ' ', ' '],
        [' ', ' ', ' ', '*', ' ', ' '],
        ['*', '*', '*', '*', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', 'R'],
    ]

    return Tablero, Tablero_Objetivo

Tablero , Tablero_Objetivo = Crear_Tablero()

def Visualizar_Tablero(Tablero):
    for i in range(len(Tablero)):
        print(Tablero[i])
        Reporte_Bitacora(str(Tablero[i]))

def Encontrar_Posicion_Robot (Tablero):
    Posicion = []
    for i in range(len(Tablero)):
        for j in range(len(Tablero[i])):
            if Tablero[i][j] == 'R':
                Posicion.append(i)
                Posicion.append(j)
    return Posicion

def Movimiento(Tablero, Movimientos_Realizados):
        
    Posicion = Encontrar_Posicion_Robot(Tablero)
    print (" - Posicion del robot Fila: " + str(Posicion[0]) + " Columna: " + str(Posicion[1]))

    #Regla 1: Moverse al sur
    if 1 not in Movimientos_Realizados:
        if Posicion[0] <= len(Tablero[Posicion[0]])-1:
            if Tablero[Posicion[0]+1][Posicion[1]] == ' ':

                Tablero[Posicion[0]][Posicion[1]] = ' '
                Posicion[0] = Posicion[0] + 1
                Tablero[Posicion[0]][Posicion[1]] = 'R'

                Evaluacion = 1

                if Posicion[0] + 1 <= len(Tablero[0])-1:
                    if Tablero[Posicion[0]+1][Posicion[1]] == ' ':
                        Evaluacion = Evaluacion + 1
                    
                return 1 , Evaluacion

    #Regla 2: Moverse al oeste
    if 2 not in Movimientos_Realizados:
        if Posicion[1] > 0:
            if Tablero[Posicion[0]][Posicion[1]-1] == ' ':
                Tablero[Posicion[0]][Posicion[1]] = ' '
                Posicion[1] = Posicion[1] - 1
                Tablero[Posicion[0]][Posicion[1]] = 'R'

                Evaluacion = -3

                return 2 , Evaluacion
    
    #Regla 3: Moverse al este
    if 3 not in Movimientos_Realizados:
        if Posicion[1] < len(Tablero[Posicion[0]])-1:
            if Tablero[Posicion[0]][Posicion[1]+1] == ' ' :
                Tablero[Posicion[0]][Posicion[1]] = ' '
                Posicion[1] = Posicion[1] + 1
                Tablero[Posicion[0]][Posicion[1]] = 'R'

                Evaluacion = -3

                return 3 , Evaluacion
    
    #Regla 4: Moverse al suroeste
    if 4 not in Movimientos_Realizados:
        if Posicion[0] < len(Tablero[Posicion[0]])-1 and Posicion[1] > 0:
            if Tablero[Posicion[0]+1][Posicion[1]-1] == ' ':
                Tablero[Posicion[0]][Posicion[1]] = ' '
                Posicion[0] = Posicion[0] + 1
                Posicion[1] = Posicion[1] - 1
                Tablero[Posicion[0]][Posicion[1]] = 'R'

                Evaluacion = 1
                if Posicion[0]+1 < len(Tablero[Posicion[0]])-1:
                    if Tablero[Posicion[0]+1][Posicion[1]] == ' ':
                        Evaluacion = Evaluacion + 1

                return 4 , Evaluacion
    
    #Regla 5: Moverse al sureste
    if 5 not in Movimientos_Realizados:
        if Posicion[0] < len(Tablero[Posicion[0]])-1 and Posicion[1] < len(Tablero[Posicion[0]])-1:
            if Tablero[Posicion[0]+1][Posicion[1]+1] == ' ':
                Tablero[Posicion[0]][Posicion[1]] = ' '
                Posicion[0] = Posicion[0] + 1
                Posicion[1] = Posicion[1] + 1
                Tablero[Posicion[0]][Posicion[1]] = 'R'

                Evaluacion = 1

                
                if Posicion[0]+1 < len(Tablero[Posicion[0]])-1:
                    if Tablero[Posicion[0]+1][Posicion[1]] == ' ':
                        Evaluacion = Evaluacion + 1

                return 5 , Evaluacion
    
    return None, None

def Evaluar_Estado(Evaluacion_Actual, Evaluacion_Siguiente):
    if Evaluacion_Actual > Evaluacion_Siguiente:
        return False
    else:
        return True

def Validar_Solucion (Tablero, Tablero_Objetivo):
    if Tablero == Tablero_Objetivo:
        return True
    else:
        return False

def Mejores_Opciones(Lista, Reglas, Evaluacion_Estado):
    Maximo_Opciones = 2
    Lista_Mejores = []
    Lista_Reglas = []
    Contador = 1
    for i in range(len(Lista)):
        if Lista[i] > Evaluacion_Estado and Contador <= Maximo_Opciones:
            Lista_Mejores.append(Lista[i])
            Lista_Reglas.append(Reglas[i])
            Contador = Contador + 1

    return Lista_Mejores, Lista_Reglas

def Mejores_Estados(Valores_Evaluacion):
    Valores_Evaluacion.sort(reverse=True)
    Mejores_Estados = []
    for i in range(3):
        Mejores_Estados.append(Valores_Evaluacion[i])
    return Mejores_Estados

def Estado_Mayor_Evaluacion(Valores_Evaluacion):
    Mayor = Valores_Evaluacion[0]
    Posicion_Mayor = 0
    for i in range(len(Valores_Evaluacion)):
        if Valores_Evaluacion[i] > Mayor:
            Mayor = Valores_Evaluacion[i]
            Posicion_Mayor = i
    return Mayor , Posicion_Mayor

class Nodo:
    def __init__(self, Tablero, Evaluacion, Nivel):
        self.Tablero = Tablero
        self.Evaluacion = Evaluacion
        self.Nivel = Nivel

Nodos = Queue()

def Beam_Search():
    Nodo_Actual = Nodos.get()
    Evaluacion_Estado = Nodo_Actual.Evaluacion
    if Validar_Solucion(Nodo_Actual.Tablero, Tablero_Objetivo):
        print("🤖 Robot llego a la meta!")
        Reporte_Bitacora("🤖 Robot llego a la meta!")
        print("Tablero Actual")
        Reporte_Bitacora("Tablero Actual")
        Visualizar_Tablero(Nodo_Actual.Tablero)
        sys.exit()
    else:
        print(Fore.GREEN)
        print (" ** Nodo en el nivel: " + str(Nodo_Actual.Nivel) + " ** \n")
        Reporte_Bitacora("Nodo en el nivel: " + str(Nodo_Actual.Nivel))
        Reporte_Bitacora("Nodo Actual")
        Visualizar_Tablero(Nodo_Actual.Tablero)
        print("")
        print("Evaluacion del nodo actual: " + str(Nodo_Actual.Evaluacion))
        Reporte_Bitacora("Evaluacion del nodo actual: " + str(Nodo_Actual.Evaluacion))
        print("")
        input("Presiona Enter para continuar...")
        print("")

        Movimientos_Realizados = []
        Reglas = []
        Valores_Evaluacion = []

        print(Fore.CYAN)
        print(" ** Evaluacion de los posibles movimientos **")
        Reporte_Bitacora("Evaluacion de los posibles movimientos")
        input("Presiona Enter para continuar...")
        print("")
        for i in range(5):
            Tablero_AUX = copy.deepcopy(Nodo_Actual.Tablero)

            print(" ** Tablero con posible movimiento ** ")
            Reporte_Bitacora(" ** Tablero con posible movimiento ** ")
            print("")

            Regla_Aplicada , Evaluacion = Movimiento(Tablero_AUX, Movimientos_Realizados)
            if Regla_Aplicada is None and Evaluacion is None:
                print (" ** No se puede aplicar ninguna regla **")
                Reporte_Bitacora(" ** No se puede aplicar ninguna regla **")
                break
            
            print(" - Regla aplicada: " + str(Regla_Aplicada))
            Reporte_Bitacora("Regla aplicada: " + str(Regla_Aplicada))
            print(" - Evaluacion del nodo: " + str(Evaluacion))
            Reporte_Bitacora("Evaluacion del nodo: " + str(Evaluacion))
            print("")
            Visualizar_Tablero(Tablero_AUX)
            print("") 

            Movimientos_Realizados.append(Regla_Aplicada)
            print(" - Movimientos realizados: " + str(Movimientos_Realizados))
            Reporte_Bitacora(" - Movimientos realizados: " + str(Movimientos_Realizados))

            Evaluacion_Aux = Evaluacion_Estado + Evaluacion
            Reglas.append(Regla_Aplicada)
            Valores_Evaluacion.append(Evaluacion_Aux)
            
            print(" - Evaluacion del estado: " + str(Evaluacion_Aux))
            Reporte_Bitacora(" - Evaluacion del estado: " + str(Evaluacion_Aux))

            print(" - Reglas: " + str(Reglas))
            Reporte_Bitacora(" - Reglas: " + str(Reglas))

            print(" - Valores de evaluacion: " + str(Valores_Evaluacion))
            Reporte_Bitacora(" - Valores de evaluacion: " + str(Valores_Evaluacion))
            print("")
            input("Presiona Enter para continuar...")
            print("")

        print(Fore.YELLOW)
        print("\n\n\n ** Evaluacion de las reglas posibles ** \n")
        Reporte_Bitacora("Evaluacion de las reglas posibles")
        if len(Reglas) > 0:            
            Movimientos_No_Realizados = []

            print(" - Reglas: " + str(Reglas))
            Reporte_Bitacora(" - Reglas: " + str(Reglas))
            print(" - Valores de evaluacion: " + str(Valores_Evaluacion))
            Reporte_Bitacora(" - Valores de evaluacion: " + str(Valores_Evaluacion))
            
            Valores_Evaluacion_AUX = copy.deepcopy(Valores_Evaluacion)
            Reglas_AUX = copy.deepcopy(Reglas)

            Mejores_Evaluaciones , Reglas_Mejores = Mejores_Opciones(Valores_Evaluacion_AUX, Reglas_AUX, Evaluacion_Estado)

            print(" - Mejores evaluaciones: " + str(Mejores_Evaluaciones))
            Reporte_Bitacora(" - Mejores evaluaciones: " + str(Mejores_Evaluaciones))
            print(" - Reglas mejores: " + str(Reglas_Mejores))
            Reporte_Bitacora(" - Reglas mejores: " + str(Reglas_Mejores))

            Movimientos_No_Realizados_AUX = []
            for i in range(1,6):
                if i not in Reglas_Mejores:
                    Movimientos_No_Realizados_AUX.append(i)

            print ( " - Movimientos no realizados AUX: " + str(Movimientos_No_Realizados_AUX))

            Mayor_Evaluacion , Posicion = Estado_Mayor_Evaluacion(Valores_Evaluacion)

            print("Mayor evaluacion: " + str(Mayor_Evaluacion))
            Reporte_Bitacora("Mayor evaluacion: " + str(Mayor_Evaluacion))

            print("Posicion de la mayor evaluacion: " + str(Posicion))
            
            

            print("Regla aplicada: " + str(Reglas[Posicion]))
            Reporte_Bitacora("Regla aplicada: " + str(Reglas[Posicion]))
            
            for i in range(1,6):
                if i != Reglas[Posicion]:
                    Movimientos_No_Realizados.append(i)
            
            print ( "Movimientos no realizados: " + str(Movimientos_No_Realizados))
            input("Presiona Enter para continuar...")

            for i in range(1,6):
                Tablero_AUX = copy.deepcopy(Nodo_Actual.Tablero)
                print ( " - Movimientos no realizados AUX: " + str(Movimientos_No_Realizados_AUX))
                Reporte_Bitacora(" - Movimientos no realizados: " + str(Movimientos_No_Realizados_AUX))

                Regla_Aplicada , Evaluacion = Movimiento(Tablero_AUX, Movimientos_No_Realizados_AUX)
                print ( " - * * * Regla aplicada: " + str(Regla_Aplicada))
                
                if Regla_Aplicada is None and Evaluacion is None:
                    print (" ** No se puede aplicar ninguna regla **")
                    Reporte_Bitacora(" ** No se puede aplicar ninguna regla **")
                    break

                Movimientos_No_Realizados_AUX.append(Regla_Aplicada)

                Evaluacion_Aux = Evaluacion_Estado + Evaluacion
                
                if Evaluar_Estado(Evaluacion_Estado, Evaluacion_Aux):
                    Tablero = copy.deepcopy(Tablero_AUX)
                    Evaluacion_Estado = Evaluacion_Estado + Evaluacion
                    
                    Nodos.put(Nodo(Tablero, Evaluacion_Estado, Nodo_Actual.Nivel+1))

                    #Movimientos_Realizados.append(Regla_Aplicada)

                    print("Regla aplicada: " + str(Regla_Aplicada))
                    Reporte_Bitacora("Regla aplicada: " + str(Regla_Aplicada))

                    print("Evaluacion del estado: " + str(Evaluacion_Estado))
                    Reporte_Bitacora("Evaluacion del estado: " + str(Evaluacion_Estado))
                    
                else:
                    print("🤖 Robot no puede llegar a la meta!")       
                    Reporte_Bitacora("🤖 Robot no puede llegar a la meta!")  
                    print("Maximo local alcanzado!")
                    Reporte_Bitacora("Maximo local alcanzado!")   
            
            Beam_Search()
            

Evaluacion_Estado = 0

print(Fore.RED)
print ("Heuristica Beam Search 🚀")
Reporte_Bitacora("Heuristica Beam Search 🚀")
print ("Desarrollado por: Eduardo Isaac Dávila Bernal 🤓")
Reporte_Bitacora("Desarrollado por: Eduardo Isaac Dávila Bernal 🤓")
print ("Matricula: 2193076785 \n")
Reporte_Bitacora("Matricula: 2193076785 \n")


Nodo_Inicial = Nodo(Tablero, Evaluacion_Estado, 0)
Nodos.put(Nodo_Inicial)
Beam_Search()