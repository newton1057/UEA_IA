
import random

class Nodo:
    def __init__(self, Dato):
        self.Dato = Dato
        self.Relaciones = []


def Recorrer_Arbol(Concepto: Nodo):
    print(Concepto.Dato)
    print("Relaciones: ", len(Concepto.Relaciones))
    index_relation = random.randint(0, len(Concepto.Relaciones) - 1)
    print("Index: ", index_relation)
    for Relacion in Concepto.Relaciones:
        print(Relacion.Dato)
        
    

Atributo = Nodo("bien")
Relacion = Nodo("vuela")

Relacion.Relaciones.append(Atributo)

Concepto = Nodo("ave")
Concepto.Relaciones.append(Relacion)

print("Frase: ", Concepto.Dato ,Concepto.Relaciones[0].Dato, Concepto.Relaciones[0].Relaciones[0].Dato)


Atributo = Nodo("plumas")
Relacion = Nodo("tiene")

Relacion.Relaciones.append(Atributo)
Concepto.Relaciones.append(Relacion)

print("Frase: ", Concepto.Dato, Concepto.Relaciones[1].Dato, Concepto.Relaciones[1].Relaciones[0].Dato)

Atributo = Nodo("huevos")
Relacion = Nodo("pone")

Relacion.Relaciones.append(Atributo)
Concepto.Relaciones.append(Relacion)

print("Frase: ", Concepto.Dato, Concepto.Relaciones[2].Dato, Concepto.Relaciones[2].Relaciones[0].Dato)

Recorrer_Arbol(Concepto)