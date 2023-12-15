def asignacion_tareas_busqueda_profundidad(matriz_costos):
    n = len(matriz_costos)
    mejor_asignacion = []
    mejor_costo = float('inf')

    def buscar_profundidad(asignacion, costo_actual):
        print(asignacion, costo_actual)
        nonlocal mejor_costo, mejor_asignacion

        if len(asignacion) == n:
            print("Encontré una asignación completa:", asignacion)
            print("Costo de la asignación:", costo_actual)
            if costo_actual < mejor_costo:
                mejor_costo = costo_actual
                mejor_asignacion = asignacion
            return

        persona = len(asignacion)
        for tarea in range(n):
            if tarea not in asignacion:
                nuevo_costo = costo_actual + matriz_costos[persona][tarea]
                buscar_profundidad(asignacion + [tarea], nuevo_costo)

    buscar_profundidad([], 0)
    return mejor_asignacion, mejor_costo

matriz_costos = [
    [9, 2, 7, 8],
    [6, 4, 3, 7],
    [5, 8, 1, 8],
    [7, 6, 9, 4]
]
# Ejemplo de uso:
asignacion, costo = asignacion_tareas_busqueda_profundidad(matriz_costos)
print("Mejor asignación:", asignacion)
print("Mejor costo:", costo)
