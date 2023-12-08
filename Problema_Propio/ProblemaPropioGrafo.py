from queue import Queue

class Nodo:
    def __init__(self, Persona, Tarea, Costo):
        self.Persona = Persona
        self.Tarea = Tarea
        self.Costo = Costo
        self.Hijos = []

def Crear_Hijos(Matriz_Costos_Persona: [], Tareas_Ocupadas: [], Persona):
    Hijos = []
    for Tarea in range(len(Matriz_Costos)):
        if not Tarea in Tareas_Ocupadas:
            Costo = Matriz_Costos_Persona[Tarea]
            Nodo_ = Nodo( Persona, Tarea, Costo)
            Hijos.append(Nodo_)
    
    return Hijos

def Imprimir_Nodo (Nodo : Nodo):
    Tarea = Nodo.Tarea
    Persona = Nodo.Persona
    Costo = Nodo.Costo
    print (" Nodo -> Persona: " + str(Persona) + " - Tarea: "+ str(Tarea) + " - Costo: " + str(Costo))
    
def Crear_Grafo(Matriz_Costos: [], Nodo_Raiz: Nodo):
    N_Personas = len(Matriz_Costos)

    def Recorrer_Matriz_Grafo (Nodo_Padre: Nodo, Persona, Matriz_Costos, Tareas_Ocupadas: []):
        Hijos = Crear_Hijos(Matriz_Costos[Persona], Tareas_Ocupadas, Persona)
        Nodo_Padre.Hijos = Hijos
        Persona = Persona + 1
        for Hijo in Hijos:
            Imprimir_Nodo(Hijo)
            Tareas_Ocupadas.append(Hijo.Tarea)
            print(Tareas_Ocupadas)
            if Persona == N_Personas:
                Tareas_Ocupadas.pop()
                return
            Recorrer_Matriz_Grafo(Hijo, Persona, Matriz_Costos, Tareas_Ocupadas)   
            Tareas_Ocupadas.pop()

    Persona = 0
    Recorrer_Matriz_Grafo(Nodo_Raiz, Persona, Matriz_Costos, [])
    
def Poda_Ramificacion(Nodo_Raiz : Nodo):
    def Mejor_Costo_Hijos(Nodo:Nodo):
        Mejor_Costo = Nodo.Hijos[0].Costo
        Mejor_Costo_Hijo = Nodo.Hijos[0]
        for Hijo in Nodo.Hijos:
            if Mejor_Costo > Hijo.Costo:
                Mejor_Costo = Hijo.Costo
                Mejor_Costo_Hijo = Hijo        
        return Mejor_Costo, Mejor_Costo_Hijo

    def Costo_Rama_Optimista (Nodo: Nodo):
        Nodo_ = Nodo
        Cola = Queue()
        Cola.put(Nodo_)
        Mejor_Costo = 0
        Lista = []
        while not Cola.empty():
            Nodo_ = Cola.get()
            if len(Nodo_.Hijos) != 0:
                Costo, Nodo_ = Mejor_Costo_Hijos(Nodo_)
                Mejor_Costo = Mejor_Costo + Costo
                Lista.append(Nodo_)
                Cola.put(Nodo_)

        print("Mejor costo de la rama optimista: " + str(Mejor_Costo)) #15 + 9
        return Lista[0]
    
    def Costo_Ramas (Nodo: Nodo, Asignacion: Queue):
        Costo_Rama = 0
        Cola =  Queue()
        Lista_Costos = []

        for Hijo in Nodo.Hijos:
            Cola.put(Hijo)
            while not Cola.empty():
                Nodo_ = Cola.get()
                Costo_Rama = Costo_Rama + Nodo_.Costo
                if len(Nodo_.Hijos) != 0:
                    M = Nodo_.Hijos[0].Costo
                    Aux =  Nodo_.Hijos[0]
                    for Hijo in Nodo_.Hijos:
                        if M > Hijo.Costo:
                            M = Hijo.Costo
                            Aux = Hijo
                    Cola.put(Aux)
            Lista_Costos.append(Costo_Rama)
            Costo_Rama=0

        if len(Nodo.Hijos) == 0:
            return
        Asignacion.put(Nodo.Hijos[Lista_Costos.index(min(Lista_Costos))])        
        Costo_Ramas(Nodo.Hijos[Lista_Costos.index(min(Lista_Costos))], Asignacion)

    Asignacion = Queue()    
    Rama_Optimista = Costo_Rama_Optimista(Nodo_Raiz)
    Asignacion.put(Rama_Optimista)
    
    Costo_Ramas(Rama_Optimista, Asignacion)
    print("")
    print("")
    print("Asignacion:")
    Costo_Total = 0
    while not Asignacion.empty():
        Nodo_ = Asignacion.get()
        print ("* * Persona " + str(Nodo_.Persona) + " - Tarea " + str(Nodo_.Tarea) + " - Costo " + str(Nodo_.Costo)) 
        Costo_Total = Costo_Total + Nodo_.Costo
        #print("Costo " + str( Nodo_.Costo))
    #Costo_Optimista (Nodo_Raiz, 0)

    print("Costo de la operacion: " + str(Costo_Total))

"""
Matriz_Costos = [
#   T0 T1 T2 T1    
    [13, 7, 12, 12], #P0
    [10, 13, 15, 7], #P1 
    [10, 13, 15, 7], #P2   
    [13, 10, 8, 8]  #P3
]
"""

Matriz_Costos = [
#   T0 T1 T2 T1    
    [9, 2, 7, 8], #P0
    [6, 4, 3, 7], #P1
    [5, 8, 1, 8], #P2   
    [7, 6, 9, 4]  #P3
]


Nodo_Raiz = Nodo(None,None,None)

Crear_Grafo(Matriz_Costos, Nodo_Raiz)

Poda_Ramificacion(Nodo_Raiz)