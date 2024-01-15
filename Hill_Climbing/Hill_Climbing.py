import copy
import sys

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
    #Regla 1: Moverse al sur
    if 1 not in Movimientos_Realizados:
        if Tablero[Posicion[0]+1][Posicion[1]] == ' ':
            Tablero[Posicion[0]][Posicion[1]] = ' '
            Posicion[0] = Posicion[0] + 1
            Tablero[Posicion[0]][Posicion[1]] = 'R'

            Evaluacion = 1

            if Tablero[Posicion[0]+1][Posicion[1]] == ' ':
                Evaluacion = Evaluacion + 1
                
            return 1 , Evaluacion

    #Regla 2: Moverse al oeste
    if 2 not in Movimientos_Realizados:
        if Tablero[Posicion[0]][Posicion[1]-1] == ' ':
            Tablero[Posicion[0]][Posicion[1]] = ' '
            Posicion[1] = Posicion[1] - 1
            Tablero[Posicion[0]][Posicion[1]] = 'R'

            Evaluacion = -3

            return 2 , Evaluacion
    
    #Regla 3: Moverse al este
    if 3 not in Movimientos_Realizados:
        if Tablero[Posicion[0]][Posicion[1]+1] == ' ':
            Tablero[Posicion[0]][Posicion[1]] = ' '
            Posicion[1] = Posicion[1] + 1
            Tablero[Posicion[0]][Posicion[1]] = 'R'

            Evaluacion = -3

            return 3 , Evaluacion
    
    #Regla 4: Moverse al suroeste
    if 4 not in Movimientos_Realizados:
        if Tablero[Posicion[0]+1][Posicion[1]-1] == ' ':
            Tablero[Posicion[0]][Posicion[1]] = ' '
            Posicion[0] = Posicion[0] + 1
            Posicion[1] = Posicion[1] - 1
            Tablero[Posicion[0]][Posicion[1]] = 'R'

            Evaluacion = 1

            if Tablero[Posicion[0]+1][Posicion[1]] == ' ':
                Evaluacion = Evaluacion + 1

            return 4 , Evaluacion
    
    #Regla 5: Moverse al sureste
    if 5 not in Movimientos_Realizados:
        if Tablero[Posicion[0]+1][Posicion[1]+1] == ' ':
            Tablero[Posicion[0]][Posicion[1]] = ' '
            Posicion[0] = Posicion[0] + 1
            Posicion[1] = Posicion[1] + 1
            Tablero[Posicion[0]][Posicion[1]] = 'R'

            Evaluacion = 1

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
    
def Hill_Climbing(Tablero, Evaluacion_Estado):
    if Validar_Solucion(Tablero, Tablero_Objetivo):
        print("🤖 Robot llego a la meta!")
        Reporte_Bitacora("🤖 Robot llego a la meta!")
        sys.exit()
    else:
        Movimientos_Realizados = []
        for i in range(5):
            Tablero_AUX = copy.deepcopy(Tablero)
            print("Tablero auxiliar")
            Reporte_Bitacora("Tablero auxiliar")
            Visualizar_Tablero(Tablero_AUX)
            
            print("Movimientos realizados: " + str(Movimientos_Realizados))
            Reporte_Bitacora("Movimientos realizados: " + str(Movimientos_Realizados))

            Regla_Aplicada , Evaluacion = Movimiento(Tablero_AUX, Movimientos_Realizados)
            if Regla_Aplicada is None and Evaluacion is None:
                print("🤖 Robot no puede llegar a la meta!")
                Reporte_Bitacora("🤖 Robot no puede llegar a la meta!")
                print("Maximo local alcanzado!")
                Reporte_Bitacora("Maximo local alcanzado!")
                sys.exit()

            print("Regla aplicada: " + str(Regla_Aplicada))
            Reporte_Bitacora("Regla aplicada: " + str(Regla_Aplicada))

            print("Evaluacion: " + str(Evaluacion))
            Reporte_Bitacora("Evaluacion: " + str(Evaluacion))

            Evaluacion_Aux = Evaluacion_Estado + Evaluacion

            print("Evaluacion Estado: " + str(Evaluacion_Estado))
            Reporte_Bitacora("Evaluacion Estado: " + str(Evaluacion_Estado))            
            
            if (Evaluar_Estado(Evaluacion_Estado, Evaluacion_Aux)):
                Tablero = copy.deepcopy(Tablero_AUX)
                Evaluacion_Estado = Evaluacion_Estado + Evaluacion
                Movimientos_Realizados.append(Regla_Aplicada)
                
                print("Regla aplicada: " + str(Regla_Aplicada))
                Reporte_Bitacora("Regla aplicada: " + str(Regla_Aplicada))
                
                print("Evaluacion del estado: " + str(Evaluacion_Estado))
                Reporte_Bitacora("Evaluacion del estado: " + str(Evaluacion_Estado))

                print("Tablero Actualizado")
                Reporte_Bitacora("Tablero Actualizado")

                Visualizar_Tablero(Tablero)
                Hill_Climbing(Tablero, Evaluacion_Estado)
            else:
                Movimientos_Realizados.append(Regla_Aplicada)
                print("🤖 Robot aun no puede llegar a la meta!")
                Reporte_Bitacora("🤖 Robot aun no puede llegar a la meta!")

Evaluacion_Estado = 0

print ("Heuristica Hill Climbing 🚀")
Reporte_Bitacora("Heuristica Hill Climbing 🚀")
print ("Desarrollado por: Eduardo Isaac Dávila Bernal 🤓")
Reporte_Bitacora("Desarrollado por: Eduardo Isaac Dávila Bernal 🤓")
print ("Matricula: 2193076785 \n")
Reporte_Bitacora("Matricula: 2193076785 \n")

print ("Tablero inicial")
Reporte_Bitacora("Tablero inicial")
Visualizar_Tablero(Tablero)
print("")

Hill_Climbing(Tablero, Evaluacion_Estado)