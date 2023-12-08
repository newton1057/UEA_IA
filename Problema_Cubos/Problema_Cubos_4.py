import copy
import sys
from queue import Queue

def Reporte_Bitacora (linea):
    with open('Bitacora.log', 'a') as archivo:
        # Escribe el contenido en el archivo
        linea = linea + "\n"
        archivo.write(linea)

def Obtener_Hash_Estado (Area_Trabajo):
    Tupla_Area = tuple(map(tuple, Area_Trabajo)) # Convierte la matriz en una tupla
    hash_valor = hash(Tupla_Area) # Calcula el hash de la tupla
    return hash_valor

 
def Crear_Area_Trabajo():
    print ("Crear area de trabajo 📦")
    Columna_Entrada = []
    Columna_Objetivo = ['D','C','B','A']

    Area_Trabajo = []

    #N_Cubos = int (input("Numero de cubos: "))
    N_Cubos = 4
    """for i in range (N_Cubos):
        Letra = input(f"Letra del cubo numero {i} : ")
        Columna_Entrada.append(Letra)"""
    
    Columna_Entrada.append('A')
    Columna_Entrada.append('B')
    Columna_Entrada.append('C')
    Columna_Entrada.append('D')

    Area_Trabajo.append(Columna_Entrada)
    for i in range (N_Cubos-1):
        Area_Trabajo.append([])

    print ("")

    return Area_Trabajo, Columna_Objetivo

def Mostrar_Area_Trabajo(Area_Trabajo):
    print ("Mostrar area de trabajo 👀")
    for i in range (len(Area_Trabajo)):
        print (Area_Trabajo[i])
        Reporte_Bitacora(str(Area_Trabajo[i]))


def Validar_Solucion(Area_Trabajo, Columna_Salida):
    print ("Validar solucion 🔍")
    for Columna in Area_Trabajo:
        if Columna == Columna_Salida:
            print ("Solucion correcta ✅")
            return True    
    print ("Solucion incorrecta ❌")
    return False

def Reglas_Movimiento(Area_Trabajo, Movimientos_Realizados):
    #print ("Reglas de movimiento 🔃")

    def Buscar_Cubo (Area_Trabajo, Cubo):
        for Columna in range(len(Area_Trabajo)):
            for Fila in range(len(Area_Trabajo[Columna])):
                if Area_Trabajo[Columna][Fila] == Cubo:
                    return Columna, Fila

    if 1 not in Movimientos_Realizados:
        # Regla 1 - Mueve cubo D al piso : SI D no está en el piso y D no tiene cubo arriba ENTONCES Mueve cubo D al piso
        Columna, Fila = Buscar_Cubo(Area_Trabajo, "D")
        Logitud = len(Area_Trabajo[Columna])

        if Area_Trabajo[Columna][-1] == "D" and Logitud > 1:
            #print ("Cubo D en al piso")
            for Lista in Area_Trabajo:
                if len(Lista) == 0:
                    Lista.append(Area_Trabajo[Columna].pop())
                    break
            print ("Retorno 1")
            return 1
        
    if 2 not in Movimientos_Realizados:
        # Regla 2 - Mueve cubo D sobre C : SI D no tiene cubo arriba y C no tiene cubo arriba ENTONCES Mueve cubo D sobre C
        Columna_D, Fila_D = Buscar_Cubo(Area_Trabajo, "D")

        Logitud = len(Area_Trabajo[Columna_D])
        if Logitud == Fila_D + 1:
            Columna_C, Fila_C = Buscar_Cubo(Area_Trabajo, "C")
            Logitud = len(Area_Trabajo[Columna_C])
            if Logitud == Fila_C + 1:
                Area_Trabajo[Columna_C].append(Area_Trabajo[Columna_D].pop())
                print ("Retorno 2")
                return 2
    
    if 3 not in Movimientos_Realizados:
        # Regla 3 - Mueve cubo D sobre B : SI D no tiene cubo arriba y B no tiene cubo arriba ENTONCES Mueve cubo D sobre B
        Columna_D, Fila_D = Buscar_Cubo(Area_Trabajo, "D")

        Logitud = len(Area_Trabajo[Columna_D])
        if Logitud == Fila_D + 1:
            Columna_B, Fila_B = Buscar_Cubo(Area_Trabajo, "B")
            Logitud = len(Area_Trabajo[Columna_B])
            if Logitud == Fila_B + 1:
                Area_Trabajo[Columna_B].append(Area_Trabajo[Columna_D].pop())
                print ("Retorno 3")
                return 3
    
    if 4 not in Movimientos_Realizados:
        # Regla 4 - Mueve cubo D sobre A : SI D no tiene cubo arriba y A no tiene cubo arriba ENTONCES Mueve cubo D sobre A
        Columna_D, Fila_D = Buscar_Cubo(Area_Trabajo, "D")

        Logitud = len(Area_Trabajo[Columna_D])
        if Logitud == Fila_D + 1:
            Columna_A, Fila_A = Buscar_Cubo(Area_Trabajo, "A")
            Logitud = len(Area_Trabajo[Columna_A])
            if Logitud == Fila_A + 1:
                Area_Trabajo[Columna_A].append(Area_Trabajo[Columna_D].pop())
                print ("Retorno 4")
                return 4
    
    if 5 not in Movimientos_Realizados:
        # Regla 5 - Mueve cubo C al piso : SI C no está en el piso y C no tiene cubo arriba ENTONCES Mueve cubo C al piso
        Columna, Fila = Buscar_Cubo(Area_Trabajo, "C")
        Logitud = len(Area_Trabajo[Columna])

        if Area_Trabajo[Columna][-1] == "C" and Logitud > 1:
            #print ("Cubo C en al piso")
            for Lista in Area_Trabajo:
                if len(Lista) == 0:
                    Lista.append(Area_Trabajo[Columna].pop())
                    break
            print ("Retorno 5")
            return 5
    
    if 6 not in Movimientos_Realizados:
        # Regla 6 - Mueve cubo C sobre D : SI C no tiene cubo arriba y D no tiene cubo arriba ENTONCES Mueve cubo C sobre D
        Columna_C, Fila_C = Buscar_Cubo(Area_Trabajo, "C")

        Logitud = len(Area_Trabajo[Columna_C])
        if Logitud == Fila_C + 1:
            Columna_D, Fila_D = Buscar_Cubo(Area_Trabajo, "D")
            Logitud = len(Area_Trabajo[Columna_D])
            if Logitud == Fila_D + 1:
                Area_Trabajo[Columna_D].append(Area_Trabajo[Columna_C].pop())
                print ("Retorno 6")
                return 6
    
    if 7 not in Movimientos_Realizados:
        # Regla 7 - Mueve cubo C sobre B : SI C no tiene cubo arriba y B no tiene cubo arriba ENTONCES Mueve cubo C sobre B
        Columna_C, Fila_C = Buscar_Cubo(Area_Trabajo, "C")

        Logitud = len(Area_Trabajo[Columna_C])
        if Logitud == Fila_C + 1:
            Columna_B, Fila_B = Buscar_Cubo(Area_Trabajo, "B")
            Logitud = len(Area_Trabajo[Columna_B])
            if Logitud == Fila_B + 1:
                Area_Trabajo[Columna_B].append(Area_Trabajo[Columna_C].pop())
                print ("Retorno 7")
                return 7
    
    if 8 not in Movimientos_Realizados:
        # Regla 8 - Mueve cubo C sobre A : SI C no tiene cubo arriba y A no tiene cubo arriba ENTONCES Mueve cubo C sobre A
        Columna_C, Fila_C = Buscar_Cubo(Area_Trabajo, "C")

        Logitud = len(Area_Trabajo[Columna_C])
        if Logitud == Fila_C + 1:
            Columna_A, Fila_A = Buscar_Cubo(Area_Trabajo, "A")
            Logitud = len(Area_Trabajo[Columna_A])
            if Logitud == Fila_A + 1:
                Area_Trabajo[Columna_A].append(Area_Trabajo[Columna_C].pop())
                print ("Retorno 8")
                return 8
    
    if 9 not in Movimientos_Realizados:
        # Regla 9 - Mueve cubo B al piso : SI B no está en el piso y B no tiene cubo arriba ENTONCES Mueve cubo B al piso
        Columna, Fila = Buscar_Cubo(Area_Trabajo, "B")
        Logitud = len(Area_Trabajo[Columna])

        if Area_Trabajo[Columna][-1] == "B" and Logitud > 1:
            #print ("Cubo B en al piso")
            for Lista in Area_Trabajo:
                if len(Lista) == 0:
                    Lista.append(Area_Trabajo[Columna].pop())
                    break
            print ("Retorno 9")
            return 9
    
    if 10 not in Movimientos_Realizados:
        # Regla 10 - Mueve cubo B sobre D : SI B no tiene cubo arriba y D no tiene cubo arriba ENTONCES Mueve cubo B sobre D
        Columna_B, Fila_B = Buscar_Cubo(Area_Trabajo, "B")

        Logitud = len(Area_Trabajo[Columna_B])
        if Logitud == Fila_B + 1:
            Columna_D, Fila_D = Buscar_Cubo(Area_Trabajo, "D")
            Logitud = len(Area_Trabajo[Columna_D])
            if Logitud == Fila_D + 1:
                Area_Trabajo[Columna_D].append(Area_Trabajo[Columna_B].pop())
                print ("Retorno 10")
                return 10
    
    if 11 not in Movimientos_Realizados:
        # Regla 11 - Mueve cubo B sobre C : SI B no tiene cubo arriba y C no tiene cubo arriba ENTONCES Mueve cubo B sobre C
        Columna_B, Fila_B = Buscar_Cubo(Area_Trabajo, "B")

        Logitud = len(Area_Trabajo[Columna_B])
        if Logitud == Fila_B + 1:
            Columna_C, Fila_C = Buscar_Cubo(Area_Trabajo, "C")
            Logitud = len(Area_Trabajo[Columna_C])
            if Logitud == Fila_C + 1:
                Area_Trabajo[Columna_C].append(Area_Trabajo[Columna_B].pop())
                print ("Retorno 11")
                return 11
    
    if 12 not in Movimientos_Realizados:
        # Regla 12 - Mueve cubo B sobre A : SI B no tiene cubo arriba y A no tiene cubo arriba ENTONCES Mueve cubo B sobre A
        Columna_B, Fila_B = Buscar_Cubo(Area_Trabajo, "B")

        Logitud = len(Area_Trabajo[Columna_B])
        if Logitud == Fila_B + 1:
            Columna_A, Fila_A = Buscar_Cubo(Area_Trabajo, "A")
            Logitud = len(Area_Trabajo[Columna_A])
            if Logitud == Fila_A + 1:
                Area_Trabajo[Columna_A].append(Area_Trabajo[Columna_B].pop())
                print ("Retorno 12")
                return 12
    
    if 13 not in Movimientos_Realizados:
        # Regla 13 - Mueve cubo A al piso : SI A no está en el piso y A no tiene cubo arriba ENTONCES Mueve cubo A al piso
        Columna, Fila = Buscar_Cubo(Area_Trabajo, "A")
        Logitud = len(Area_Trabajo[Columna])

        if Area_Trabajo[Columna][-1] == "A" and Logitud > 1:
            #print ("Cubo A en al piso")
            for Lista in Area_Trabajo:
                if len(Lista) == 0:
                    Lista.append(Area_Trabajo[Columna].pop())
                    break
            print ("Retorno 13")
            return 13
        
    if 14 not in Movimientos_Realizados:
        # Regla 14 - Mueve cubo A sobre D : SI A no tiene cubo arriba y D no tiene cubo arriba ENTONCES Mueve cubo A sobre D
        Columna_A, Fila_A = Buscar_Cubo(Area_Trabajo, "A")

        Logitud = len(Area_Trabajo[Columna_A])
        if Logitud == Fila_A + 1:
            Columna_D, Fila_D = Buscar_Cubo(Area_Trabajo, "D")
            Logitud = len(Area_Trabajo[Columna_D])
            if Logitud == Fila_D + 1:
                Area_Trabajo[Columna_D].append(Area_Trabajo[Columna_A].pop())
                print ("Retorno 14")
                return 14
    
    if 15 not in Movimientos_Realizados:
        # Regla 15 - Mueve cubo A sobre C : SI A no tiene cubo arriba y C no tiene cubo arriba ENTONCES Mueve cubo A sobre C
        Columna_A, Fila_A = Buscar_Cubo(Area_Trabajo, "A")

        Logitud = len(Area_Trabajo[Columna_A])
        if Logitud == Fila_A + 1:
            Columna_C, Fila_C = Buscar_Cubo(Area_Trabajo, "C")
            Logitud = len(Area_Trabajo[Columna_C])
            if Logitud == Fila_C + 1:
                Area_Trabajo[Columna_C].append(Area_Trabajo[Columna_A].pop())
                print ("Retorno 15")
                return 15
    
    if 16 not in Movimientos_Realizados:
        # Regla 16 - Mueve cubo A sobre B : SI A no tiene cubo arriba y B no tiene cubo arriba ENTONCES Mueve cubo A sobre B
        Columna_A, Fila_A = Buscar_Cubo(Area_Trabajo, "A")

        Logitud = len(Area_Trabajo[Columna_A])
        if Logitud == Fila_A + 1:
            Columna_B, Fila_B = Buscar_Cubo(Area_Trabajo, "B")
            Logitud = len(Area_Trabajo[Columna_B])
            if Logitud == Fila_B + 1:
                Area_Trabajo[Columna_B].append(Area_Trabajo[Columna_A].pop())
                print ("Retorno 16")
                return 16
    
    
def Validar_Estado (Estado):
    global Estados
    if Estado in Estados:
        return True
    else:
        Estados[Estado] = Estado
        return False
    
def Backtracking (Area_Trabajo, Limite):
    global Columna_Objetivo
    global Limite_Maximo

    if Limite <= int(Limite_Maximo):
        print("")
        print ("Backtracking 🔄")
        print ("Nivel de Profundidad: ", Limite)

        if Validar_Solucion(Area_Trabajo, Columna_Objetivo) == False:
            print ("")
            Estado = Obtener_Hash_Estado(Area_Trabajo)

            if Validar_Estado(Estado) == False:
                Reporte_Bitacora("Backtracking 🔄")
                Texto = "Nivel de Profundidad: " + str(Limite)
                Reporte_Bitacora(Texto)
                Mostrar_Area_Trabajo(Area_Trabajo)
                print ("Estado no repetido")

                Movimientos_Realizados = []

                for i in range (16):
                    Area_Trabajo_AUX = copy.deepcopy(Area_Trabajo)
                    Movimiento = Reglas_Movimiento(Area_Trabajo_AUX, Movimientos_Realizados)
                    
                    if Movimiento != None:
                        Movimientos_Realizados.append(Movimiento)
                        Reporte_Bitacora("Regla de movimiento aplicada: " + str(Movimiento))
                        if Backtracking(Area_Trabajo_AUX, Limite+1):
                            return True

                Movimiento = Reglas_Movimiento(Area_Trabajo_AUX, Movimientos_Realizados)
                Movimientos_Realizados.append(Movimiento)
            else:
                print ("Estado repetido")
                Reporte_Bitacora("Regla de movimiento no aplicada - Estado repetido ❌")  

        else:
            Reporte_Bitacora("Backtracking 🔄")
            Texto = "Nivel de Profundidad: " + str(Limite)
            Reporte_Bitacora(Texto)
            Mostrar_Area_Trabajo(Area_Trabajo)
            Reporte_Bitacora("Solucion encontrada ✅")
            print ("Solucion encontrada ✅")
            return True
    else:
        print ("Solucion no encontrada ❌ por limite de profundidad")
        Reporte_Bitacora("Solucion no encontrada ❌ por limite de profundidad")
        return False

def Busqueda_Amplitud(Area_Trabajo, Limite):
    global Columna_Objetivo
    global Limite_Maximo

    Hijos = Queue()    # En forma de Matriz
    Niveles = Queue()  # Numero de nivel

    Hijos.put(Area_Trabajo)
    Niveles.put(Limite)

    while Hijos.empty() == False:
        Area_Trabajo = Hijos.get()
        Limite = Niveles.get()
        print ("Por Amplitud 🚀")
        Reporte_Bitacora("Por Amplitud 🚀")
        print ("Nivel: " + str(Limite))
        Reporte_Bitacora("Nivel: " + str(Limite))
        Mostrar_Area_Trabajo(Area_Trabajo)

        if Validar_Solucion(Area_Trabajo, Columna_Objetivo) == False:
            
            Area_Trabajo_AUX = copy.deepcopy(Area_Trabajo)
            
            Estado = Obtener_Hash_Estado(Area_Trabajo_AUX)
            
            Validar_Estado(Estado)

            Movimientos_Realizados = []

            for i in range (16):
                Area_Trabajo_AUX = copy.deepcopy(Area_Trabajo)
                
                Movimiento = Reglas_Movimiento(Area_Trabajo_AUX, Movimientos_Realizados)
                #print ("Movimiento: ", Movimiento)
                #print ("Movimientos Realizados: ", Movimientos_Realizados)
                Estado = Obtener_Hash_Estado(Area_Trabajo_AUX)

                if Movimiento != None:
                    Movimientos_Realizados.append(Movimiento)
                    if Validar_Estado(Estado) == False:
                        print ("Estado no repetido")
                        Hijos.put(Area_Trabajo_AUX)
                        Niveles.put(Limite+1)
                    else:
                        print ("Estado repetido")
        else:
            print("🚀 Solucion Encontrada 🚀")
            Reporte_Bitacora("🚀 Solucion Encontrada 🚀")
            sys.exit() 



Estados = {} # Diccionario de estados

Area_Trabajo, Columna_Objetivo = Crear_Area_Trabajo()

Limite_Maximo = 4


print ("Problema de los Cubos 📦")
print ("Desarrollado por: Eduardo Isaac Dávila Bernal 🤓")
print ("Matricula: 2193076785 \n")

print ("1.- Búsqueda Por Profundida (Backtracking)")
print ("2.- Búsqueda Por Amplitud")

while True:
    Opcion = input("Coloque el numero de la opcion que desea:")

    if Opcion == "1":
        print ("\n Búsqueda Por Profundida (Backtracking)🚀 \n")
        Limite_Maximo = input("Ingrese el limite de profundidad: ")
        input ("\n Presiona Enter para continuar...")
        Backtracking(Area_Trabajo, 0)
        break

    elif Opcion == "2":
        print ("Búsqueda Por Amplitud 🚀")
        input ("\n Presiona Enter para continuar...")
        Busqueda_Amplitud(Area_Trabajo, 0)
        break
    else:
        print ("Opcion no valida")
        continue  