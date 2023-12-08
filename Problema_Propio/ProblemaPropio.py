from queue import Queue

def asignacion_tareas(matriz_costos):
    def calcular_costo_asignacion(asignacion, matriz_costos):
        costo_total = 0
        for persona, tarea in enumerate(asignacion):
            costo_total += matriz_costos[persona][tarea]
        return costo_total

    def poda_optimista(asignacion_parcial, matriz_costos):
        costo_parcial = calcular_costo_asignacion(asignacion_parcial, matriz_costos)
        for persona in range(len(matriz_costos)):
            if persona not in asignacion_parcial:
                costo_minimo = min(matriz_costos[persona])
                costo_parcial += costo_minimo
        return costo_parcial

    n = len(matriz_costos)
    m = len(matriz_costos[0])

    mejor_asignacion = None
    mejor_costo = float('inf')

    cola = Queue()
    cola.put((0, [], set())) 
    while not cola.empty():
        costo_actual, asignacion_parcial, personas_asignadas = cola.get()
        if len(asignacion_parcial) == n:
            costo_total = calcular_costo_asignacion(asignacion_parcial, matriz_costos)
            if costo_total < mejor_costo:
                mejor_costo = costo_total
                mejor_asignacion = asignacion_parcial
        else:
            persona = len(asignacion_parcial)
            for tarea in range(m):
                if tarea not in personas_asignadas:
                    nueva_asignacion = asignacion_parcial + [tarea]
                    costo_optimista = poda_optimista(nueva_asignacion, matriz_costos)
                    if costo_optimista < mejor_costo:
                        cola.put((costo_actual + matriz_costos[persona][tarea], nueva_asignacion, personas_asignadas | {tarea}))

    return mejor_asignacion, mejor_costo

matriz_costos = [
    [9, 2, 7, 8],
    [6, 4, 3, 7],
    [5, 8, 1, 8],
    [7, 6, 9, 4]
]

mejor_asignacion, mejor_costo = asignacion_tareas(matriz_costos)
print("Mejor asignación de tareas:", mejor_asignacion)
print("Mejor costo:", mejor_costo)

