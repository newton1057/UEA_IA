import numpy as np

def log(message):
    with open("Bitacora.log", "a") as file:
        file.write(message + "\n")

def asignacion_tareas_poda_ramificacion(matriz_costos):
    n = len(matriz_costos)
    asignacion_actual = []
    costo_actual = 0
    mejor_asignacion = []
    mejor_costo = float('inf')

    def podar(asignacion, costo_actual):
        global numero_iteraciones_poda
        numero_iteraciones_poda += 1
        print (f"Generacion de estados: Cantidad de estados: {len(asignacion)} - Asignacion: {asignacion}, Costo Actual: {costo_actual}")
        log(f"Generacion de estados: Cantidad de estados: {len(asignacion)} - Asignacion: {asignacion}, Costo Actual: {costo_actual}")
        nonlocal mejor_costo, mejor_asignacion
        if len(asignacion) == n:
            print("Encontré una asignación completa:", asignacion)
            log(f"Encontré una asignación completa: {asignacion}")
            print("Costo de la asignación:", costo_actual)
            log(f"Costo de la asignación: {costo_actual}")
            if costo_actual < mejor_costo:
                mejor_costo = costo_actual
                print(f"Mejor costo hasta el momento: {costo_actual} ✅")
                log(f"Mejor costo hasta el momento: {costo_actual} ✅")
                mejor_asignacion = asignacion.copy()
            return

        persona = len(asignacion)
        for tarea in range(n):
            if tarea not in asignacion:
                nuevo_costo = costo_actual + matriz_costos[persona][tarea]
                if nuevo_costo < mejor_costo:
                    podar(asignacion + [tarea], nuevo_costo)

    log("Inicio de la búsqueda por Poda y Ramificación ⚙️")
    podar(asignacion_actual, costo_actual)
    log("Fin de la búsqueda por Poda y Ramificación")
    return mejor_asignacion, mejor_costo

# Las funciones para búsqueda por amplitud y búsqueda por profundidad también se modifican de manera similar.

# Implementación de búsqueda por amplitud con bitácora
from queue import Queue

def asignacion_tareas_busqueda_amplitud(matriz_costos):
    global numero_iteraciones_amplitud
    n = len(matriz_costos)
    mejor_asignacion = []
    mejor_costo = float('inf')

    cola = Queue()
    cola.put(([], 0))  # Estado inicial: asignación vacía y costo cero

    log("Inicio de la búsqueda por Amplitud")
    while not cola.empty():
        numero_iteraciones_amplitud += 1
        asignacion, costo_actual = cola.get()
        print (f"Generacion de estados: Cantidad de estados: {len(asignacion)} - Asignacion: {asignacion}, Costo Actual: {costo_actual}")
        log(f"Generacion de estados: Cantidad de estados: {len(asignacion)} - Asignacion: {asignacion}, Costo Actual: {costo_actual}")
        if len(asignacion) == n:
            print("Encontré una asignación completa:", asignacion)
            log(f"Encontré una asignación completa: {asignacion}")
            print("Costo de la asignación:", costo_actual)
            log(f"Costo de la asignación: {costo_actual}")
            if costo_actual < mejor_costo:
                mejor_costo = costo_actual
                print(f"Mejor costo hasta el momento: {costo_actual} ✅")
                log(f"Mejor costo hasta el momento: {costo_actual} ✅")
                mejor_asignacion = asignacion
            continue

        persona = len(asignacion)
        for tarea in range(n):
            if tarea not in asignacion:
                nuevo_costo = costo_actual + matriz_costos[persona][tarea]
                cola.put((asignacion + [tarea], nuevo_costo))

    log("Fin de la búsqueda por Amplitud")
    return mejor_asignacion, mejor_costo

# Implementación de búsqueda por profundidad con bitácora
def asignacion_tareas_busqueda_profundidad(matriz_costos):
    global numero_iteraciones_profundidad
    n = len(matriz_costos)
    mejor_asignacion = []
    mejor_costo = float('inf')

    def buscar_profundidad(asignacion, costo_actual):
        global numero_iteraciones_profundidad
        numero_iteraciones_profundidad += 1
        nonlocal mejor_costo, mejor_asignacion
        print (f"Generacion de estados: Cantidad de estados: {len(asignacion)} - Asignacion: {asignacion}, Costo Actual: {costo_actual}")
        log(f"Generacion de estados: Cantidad de estados: {len(asignacion)} - Asignacion: {asignacion}, Costo Actual: {costo_actual}")
        if len(asignacion) == n:
            print("Encontré una asignación completa:", asignacion)
            log(f"Encontré una asignación completa: {asignacion}")
            print("Costo de la asignación:", costo_actual)
            log(f"Costo de la asignación: {costo_actual}")
            if costo_actual < mejor_costo:
                mejor_costo = costo_actual
                print(f"Mejor costo hasta el momento: {costo_actual} ✅")
                log(f"Mejor costo hasta el momento: {costo_actual} ✅")
                mejor_asignacion = asignacion
            return

        persona = len(asignacion)
        for tarea in range(n):
            if tarea not in asignacion:
                nuevo_costo = costo_actual + matriz_costos[persona][tarea]
                log(f"Explorando: Persona {persona} -> Tarea {tarea}, Costo acumulado: {nuevo_costo}")
                buscar_profundidad(asignacion + [tarea], nuevo_costo)

    log("Inicio de la búsqueda por Profundidad")
    buscar_profundidad([], 0)
    log("Fin de la búsqueda por Profundidad")
    return mejor_asignacion, mejor_costo

# Matriz de costos implementada como una lista de listas
matriz_costos = [
    [9, 2, 7, 8],
    [6, 4, 3, 7],
    [5, 8, 1, 8],
    [7, 6, 9, 4]
]

log("Inicio del proceso de asignación de tareas")

print ("\nProblema propio: Asignación de tareas 📚")
print ("Desarrollado por: Eduardo Isaac Dávila Bernal 🤓")
print ("Matricula: 2193076785")

print ("\nMatriz de costos:")
log("Matriz de costos:")
print(np.matrix(matriz_costos))
log(str(np.matrix(matriz_costos)))

print ("\nAlgortimo de Poda y Ramificación")
numero_iteraciones_poda = 0
asignacion, costo = asignacion_tareas_poda_ramificacion(matriz_costos)
log("\nResultados de la búsqueda por Poda y Ramificación ⚙️")
print("Mejor asignación:", asignacion)
log(f"Mejor asignación: {asignacion}")
print("Mejor costo:", costo)
log(f"Mejor costo: {costo}")
print("Número de iteraciones en Poda y Ramificación: ", numero_iteraciones_poda)
log(f"Número de iteraciones en Poda y Ramificación: {numero_iteraciones_poda}")
log("\n\n")

print ("\nAlgortimo de Búsqueda por Amplitud")
numero_iteraciones_amplitud = 0
asignacion, costo = asignacion_tareas_busqueda_amplitud(matriz_costos)
log("\nResultados de la búsqueda por Amplitud")
print("Mejor asignación en búsqueda por Amplitud: ", asignacion)
log(f"Mejor asignación en búsqueda por Amplitud: {asignacion}")
print("Mejor en búsqueda por Amplitud: ", costo)
log(f"Mejor en búsqueda por Amplitud: {costo}")
print("Número de iteraciones en búsqueda por Amplitud: ", numero_iteraciones_amplitud)
log(f"Número de iteraciones en búsqueda por Amplitud: {numero_iteraciones_amplitud}")
log("\n\n")

print ("\nAlgortimo de Búsqueda por Profundidad")
numero_iteraciones_profundidad = 0
asignacion, costo = asignacion_tareas_busqueda_profundidad(matriz_costos)
log("\nResultados de la búsqueda por Profundidad")
print("Mejor asignación:", asignacion)
log(f"Mejor asignación: {asignacion}")
print("Mejor costo:", costo)
log(f"Mejor costo: {costo}")
print("Número de iteraciones en búsqueda por Profundidad: ", numero_iteraciones_profundidad)
log(f"Número de iteraciones en búsqueda por Profundidad: {numero_iteraciones_profundidad}")
log("\n\n")

log("Fin del proceso de asignación de tareas 📚")
