def hanoi(n, origen, auxiliar, destino):
    if n == 1:
        print(f"Mueve el disco 1 de {origen} a {destino}")
        return
    hanoi(n-1, origen, destino, auxiliar)
    print(f"Mueve el disco {n} de {origen} a {destino}")
    hanoi(n-1, auxiliar, origen, destino)

# Ejemplo de uso con 3 discos
n_discos = 3
hanoi(n_discos, 'Torre A', 'Torre B', 'Torre C')