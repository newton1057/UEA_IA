from queue import Queue

def Reporte_Bitacora (linea):
    with open('Bitacora.log', 'a') as archivo:
        # Escribe el contenido en el archivo
        linea = linea + "\n"
        archivo.write(linea)

def asignacion_tareas_busqueda_amplitud(matriz_costos):
    n = len(matriz_costos)
    mejor_asignacion = []
    mejor_costo = float('inf')

    cola = Queue()
    cola.put(([], 0))  # Estado inicial: asignación vacía y costo cero

    while not cola.empty():
        asignacion, costo_actual = cola.get()

        if len(asignacion) == n:
            if costo_actual < mejor_costo:
                mejor_costo = costo_actual
                mejor_asignacion = asignacion
            continue

        persona = len(asignacion)
        for tarea in range(n):
            if tarea not in asignacion:
                nuevo_costo = costo_actual + matriz_costos[persona][tarea]
                cola.put((asignacion + [tarea], nuevo_costo))

    return mejor_asignacion, mejor_costo

matriz_costos = [
    [9, 2, 7, 8],
    [6, 4, 3, 7],
    [5, 8, 1, 8],
    [7, 6, 9, 4]
]


# Ejemplo de uso:
asignacion, costo = asignacion_tareas_busqueda_amplitud(matriz_costos)
print("Mejor asignación:", asignacion)
print("Mejor costo:", costo)
