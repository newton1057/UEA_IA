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
    Columna_Objetivo = ['C','B','A']

    Area_Trabajo = []

    #N_Cubos = int (input("Numero de cubos: "))
    N_Cubos = 3
    """for i in range (N_Cubos):
        Letra = input(f"Letra del cubo numero {i} : ")
        Columna_Entrada.append(Letra)"""
    
    Columna_Entrada.append('A')
    Columna_Entrada.append('B')
    Columna_Entrada.append('C')

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
        # Regla 1 - Mueve cubo C al piso : SI C no está en el piso y C no tiene cubo arriba ENTONCES Mueve cubo C al piso
        #print ("Regla 1")
        Columna, Fila = Buscar_Cubo(Area_Trabajo, "C")
        Logitud = len(Area_Trabajo[Columna])

        if Area_Trabajo[Columna][-1] == "C" and Logitud > 1:
            #print ("Cubo C en al piso")
            for Lista in Area_Trabajo:
                if len(Lista) == 0:
                    Lista.append(Area_Trabajo[Columna].pop())
                    break
            print ("Se ejecuto la regla 1")
            return 1
    
    if 2 not in Movimientos_Realizados:
        # Regla 2 - Mueve cubo C sobre B : SI C no tiene cubo arriba y B no tiene cubo arriba ENTONCES Mueve cubo C sobre B
        #print ("Regla 2")
        Columna_C, Fila_C = Buscar_Cubo(Area_Trabajo, "C")

        Logitud = len(Area_Trabajo[Columna_C])
        if Logitud == Fila_C + 1:
            Columna_B, Fila_B = Buscar_Cubo(Area_Trabajo, "B")
            Logitud = len(Area_Trabajo[Columna_B])
            if Logitud == Fila_B + 1:
                Area_Trabajo[Columna_B].append(Area_Trabajo[Columna_C].pop())
                print ("Retorno 2")
                return 2
    
    if 3 not in Movimientos_Realizados:
        # Regla 3 - Mueve cubo C sobre A : SI C no tiene cubo arriba y A no tiene cubo arriba ENTONCES Mueve cubo C sobre A
        #print ("Regla 3")
        Columna_C, Fila_C = Buscar_Cubo(Area_Trabajo, "C")

        Logitud = len(Area_Trabajo[Columna_C])
        if Logitud == Fila_C + 1:
            Columna_A, Fila_A = Buscar_Cubo(Area_Trabajo, "A")
            Logitud = len(Area_Trabajo[Columna_A])
            if Logitud == Fila_A + 1:
                Area_Trabajo[Columna_A].append(Area_Trabajo[Columna_C].pop())
                print ("Retorno 3")
                return 3
    
    if 4 not in Movimientos_Realizados:
        # Regla 4 - Mueve cubo B al piso : SI B no está en el piso y B no tiene cubo arriba ENTONCES Mueve cubo B al piso
        #print ("Regla 4")
        Columna, Fila = Buscar_Cubo(Area_Trabajo, "B")
        Logitud = len(Area_Trabajo[Columna])
        if Area_Trabajo[Columna][-1] == "B" and Logitud > 1:
            #print ("Cubo B en al piso")
            for Lista in Area_Trabajo:
                if len(Lista) == 0:
                    Lista.append(Area_Trabajo[Columna].pop())
                    break
            print ("Retorno 4")
            return 4
    
    if 5 not in Movimientos_Realizados:
        # Regla 5 - Mueve cubo B sobre C : SI B no tiene cubo arriba y C no tiene cubo arriba ENTONCES Mueve cubo B sobre C
        #print ("Regla 5")
        Columna_B, Fila_B = Buscar_Cubo(Area_Trabajo, "B")

        Logitud = len(Area_Trabajo[Columna_B])
        if Logitud == Fila_B + 1:
            Columna_C, Fila_C = Buscar_Cubo(Area_Trabajo, "C")
            Logitud = len(Area_Trabajo[Columna_C])
            if Logitud == Fila_C + 1:
                Area_Trabajo[Columna_C].append(Area_Trabajo[Columna_B].pop())
                print ("Retorno 5")
                return 5
    
    if 6 not in Movimientos_Realizados:
        # Regla 6 - Mueve cubo B sobre A : SI B no tiene cubo arriba y A no tiene cubo arriba ENTONCES Mueve cubo B sobre A
        #print ("Regla 6")
        Columna_B, Fila_B = Buscar_Cubo(Area_Trabajo, "B")

        Logitud = len(Area_Trabajo[Columna_B])
        if Logitud == Fila_B + 1:
            Columna_A, Fila_A = Buscar_Cubo(Area_Trabajo, "A")
            Logitud = len(Area_Trabajo[Columna_A])
            if Logitud == Fila_A + 1:
                Area_Trabajo[Columna_A].append(Area_Trabajo[Columna_B].pop())
                print ("Retorno 6")
                return 6
    
    if 7 not in Movimientos_Realizados:
        # Regla 7 - Mueve cubo A al piso : SI A no está en el piso y A no tiene cubo arriba ENTONCES Mueve cubo A al piso
        #print ("Regla 7")
        Columna, Fila = Buscar_Cubo(Area_Trabajo, "A")
        Logitud = len(Area_Trabajo[Columna])
        if Area_Trabajo[Columna][-1] == "A" and Logitud > 1:
            #print ("Cubo A en al piso")
            for Lista in Area_Trabajo:
                if len(Lista) == 0:
                    Lista.append(Area_Trabajo[Columna].pop())
                    break
            print ("Retorno 7")
            return 7
    
    if 8 not in Movimientos_Realizados:
        # Regla 8 - Mueve cubo A sobre B : SI A no tiene cubo arriba y B no tiene cubo arriba ENTONCES Mueve cubo A sobre B
        #print ("Regla 8")
        Columna_A, Fila_A = Buscar_Cubo(Area_Trabajo, "A")

        Logitud = len(Area_Trabajo[Columna_A])
        if Logitud == Fila_A + 1:
            Columna_B, Fila_B = Buscar_Cubo(Area_Trabajo, "B")
            Logitud = len(Area_Trabajo[Columna_B])
            if Logitud == Fila_B + 1:
                Area_Trabajo[Columna_B].append(Area_Trabajo[Columna_A].pop())
                print ("Retorno 8")
                return 8
    
    if 9 not in Movimientos_Realizados:
        # Regla 9 - Mueve cubo A sobre C : SI A no tiene cubo arriba y C no tiene cubo arriba ENTONCES Mueve cubo A sobre C
        #print ("Regla 9")
        Columna_A, Fila_A = Buscar_Cubo(Area_Trabajo, "A")

        Logitud = len(Area_Trabajo[Columna_A])
        if Logitud == Fila_A + 1:
            Columna_C, Fila_C = Buscar_Cubo(Area_Trabajo, "C")
            Logitud = len(Area_Trabajo[Columna_C])
            if Logitud == Fila_C + 1:
                Area_Trabajo[Columna_C].append(Area_Trabajo[Columna_A].pop())
                print ("Retorno 9")
                return 9
    
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

                for i in range (9):
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

            for i in range (9):
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