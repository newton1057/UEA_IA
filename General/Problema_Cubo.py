import copy

def Obtener_Hash_Estado (Area_Trabajo):
    
    Tupla_Area = tuple(map(tuple, Area_Trabajo)) # Convierte la matriz en una tupla
    
    hash_valor = hash(Tupla_Area) # Calcula el hash de la tupla
    return hash_valor


def Crear_Area_Trabajo():
    print ("Crear area de trabajo 📦")
    Columna_Entrada = []
    Columna_Objetivo = ['A','B','C']

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

    print (Area_Trabajo)

    return Area_Trabajo, Columna_Objetivo

def Mostrar_Area_Trabajo(Area_Trabajo):
    print ("Mostrar area de trabajo 👀")
    for i in range (len(Area_Trabajo)):
        print (Area_Trabajo[i])


def Validar_Solucion(Columna_Entrada, Columna_Salida):
    print ("Validar solucion 🔍")
    if Columna_Entrada == Columna_Salida:
        print ("Solucion correcta ✅")
        return True
    else:
        print ("Solucion incorrecta ❌")
        return False

def Reglas_Movimiento(Area_Trabajo):
    global Estados
    print ("Reglas de movimiento 🔃")

    # Regla 1
    if any(Area_Trabajo):
        for Lista in Area_Trabajo:
            if len(Lista) == 0:
                Lista.append(Area_Trabajo[0].pop())
                break
    
    # Regla 2
    """for i, lista in enumerate(Area_Trabajo):
        if lista:
            print(f"La lista en la posición {i} tiene al menos un elemento.")
            break  # Terminar el bucle cuando se encuentra la primera lista con al menos un elemento
    else:
        print("No hay ninguna lista con al menos un elemento.")"""
    
    """# Regla 2
    if not Area_Trabajo[2]:
        Area_Trabajo[2].append(Area_Trabajo[0].pop())
        return 2"""
    

def Validar_Estado (Estado):
    global Estados

    if Estado in Estados:
        return True
    else:
        Estados[Estado] = Estado
        return False
    

Estados = {} # Diccionario de estados

Area_Trabajo, Columna_Objetivo = Crear_Area_Trabajo()

Estado = Obtener_Hash_Estado(Area_Trabajo)
Res = Validar_Estado(Estado)

print(Estados)
print("")

print("Original")
Mostrar_Area_Trabajo(Area_Trabajo)
Reglas_Movimiento(Area_Trabajo)

print("Aux")
Area_Trabajo_AUX = copy.deepcopy(Area_Trabajo)
Mostrar_Area_Trabajo(Area_Trabajo_AUX)

Reglas_Movimiento(Area_Trabajo_AUX)
print("Aux")
Mostrar_Area_Trabajo(Area_Trabajo_AUX)

Reglas_Movimiento(Area_Trabajo)
print("Original")
Mostrar_Area_Trabajo(Area_Trabajo)


# Validar_Solucion(Area_Trabajo[0], Columna_Objetivo)