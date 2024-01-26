import random
import time
import sys
import os

Connects_Concepts = ["es un", "se clasifica como un", "se considera un", "entra en un" , "se identifica como un"]
Connects_Attributes = ["y", "que"]

def Reporte_Bitacora (linea):
    with open('Bitacora.log', 'a') as archivo:
        # Escribe el contenido en el archivo
        linea = linea + "\n"
        archivo.write(linea)

class Node:
    def __init__(self, Date, Classification):
        self.Date = Date
        self.Classification = Classification
        self.Relations = []

def Generate_Phrase (Node: Node, Phrase : str):
    if Node.Classification == "Concept_Relation":
        index_relation = random.randint(0, len(Connects_Concepts) - 1)
        Reporte_Bitacora("Conector elegido: " + Connects_Concepts[index_relation])
        Phrase += Connects_Concepts[index_relation] + " "
    
    if Node.Classification == "Connects_Attributes":
        index_relation = random.randint(0, len(Connects_Attributes) - 1)
        Reporte_Bitacora("Conector elegido: " + Connects_Attributes[index_relation])
        Phrase += Connects_Attributes[index_relation] + " "

    Phrase += Node.Date + " "
    Reporte_Bitacora("Frase: " + Phrase)
    
    if len(Node.Relations) == 0:
        Reporte_Bitacora("No hay mas relaciones")
        return Phrase
    
    index_relation = random.randint(0, len(Node.Relations) - 1)
    time.sleep(0.3)
    Phrase = Generate_Phrase(Node.Relations[index_relation], Phrase)

    return Phrase
    
def simulate_typing(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)  # Ajusta este valor para cambiar la velocidad de escritura
    print()

def Create_Semantic_Network():
    origin = Node("","")

    # Animal
    animal = Node("animal", "Concept")

    relation = Node("tiene", "Connects_Attributes")
    attribute = Node("vida", "")
    relation.Relations.append(attribute)
    animal.Relations.append(relation)

    relation = Node("puede", "Connects_Attributes")
    attribute = Node("moverse","")
    relation.Relations.append(attribute)
    animal.Relations.append(relation)


    relation = Node("puede", "Connects_Attributes")
    attribute = Node("sentir" , "")
    relation.Relations.append(attribute)
    animal.Relations.append(relation)

    # Mamifero
    mamifero = Node("mamifero", "Concept")

    relation = Node("da", "")
    attribute = Node("leche", "")
    relation.Relations.append(attribute)
    mamifero.Relations.append(relation)

    relation = Node("tiene", "")
    attribute = Node("pelo", "")
    relation.Relations.append(attribute)
    mamifero.Relations.append(relation)

    # Ave
    ave = Node("ave", "Concept")  

    relation = Node("vuela", "Connects_Attributes")
    attribute = Node("bien", "")
    relation.Relations.append(attribute)
    ave.Relations.append(relation)

    relation = Node("tiene", "Connects_Attributes")
    attribute = Node("plumas", "")
    relation.Relations.append(attribute)
    ave.Relations.append(relation)

    relation = Node("pone", "Connects_Attributes")
    attribute = Node("huevos", "")
    relation.Relations.append(attribute)
    ave.Relations.append(relation)

    # Ave a Animal

    relation = Node("tipo de", "Concept_Relation")
    relation.Relations.append(animal)
    ave.Relations.append(relation)

    # Mamifero a Animal

    relation = Node("tipo de", "Concept_Relation")
    relation.Relations.append(animal)
    mamifero.Relations.append(relation)


    relation = Node("tipo de", "Concept_Relation")
    relation.Relations.append(ave)


    # Avestruz
    avestruz = Node("avestruz", "Concept")  
    avestruz.Relations.append(relation)

    relation = Node("tiene patas","")
    attribute = Node("largas","")
    relation.Relations.append(attribute)
    avestruz.Relations.append(relation)

    relation = Node("vuela", "")
    attribute = Node("mal", "")
    relation.Relations.append(attribute)
    avestruz.Relations.append(relation)

    # Origen a Avestruz
    origin.Relations.append(avestruz)


    relation = Node("tipo de", "Concept_Relation")
    relation.Relations.append(ave)

    # Albatros
    albatros = Node("albatros", "Concept")
    albatros.Relations.append(relation)

    relation = Node("vuela", "")
    attribute = Node("muy bien", "")
    relation.Relations.append(attribute)
    albatros.Relations.append(relation)

    # Origen a Albatros
    origin.Relations.append(albatros)


    relation = Node("tipo de", "Concept_Relation")
    relation.Relations.append(mamifero)

    # Ballena
    ballena = Node("ballena", "Concept")  
    ballena.Relations.append(relation)

    relation = Node("tiene", "")
    attribute = Node("piel", "")
    relation.Relations.append(attribute)
    ballena.Relations.append(relation)

    relation = Node("vive en", "")
    attribute = Node("el mar", "")
    relation.Relations.append(attribute)
    ballena.Relations.append(relation)

    # Origen a Ballena
    origin.Relations.append(ballena)

    relation = Node("tipo de", "Concept_Relation")
    relation.Relations.append(mamifero)
    
    # Tigre
    tigre = Node("tigre", "Concept")
    tigre.Relations.append(relation)

    relation = Node("come", "")
    attribute = Node("carne", "")
    relation.Relations.append(attribute)
    tigre.Relations.append(relation)

    # Origen a Tigre
    origin.Relations.append(tigre)


    return origin

def Search_Concept(Node: Node, Concept: str):
    List_Concepts = Concept.split()
    for word in List_Concepts:
        if word == Node.Date:
            return Node
    
    if len(Node.Relations) == 0:
        return None
    
    for Relation in Node.Relations:
        result = Search_Concept(Relation, Concept)
        if result != None:
            return result
    
    return None

def limpiar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\033[H\033[J')  # Código de escape ANSI para limpiar la pantalla


def Create_Phrase_Promt():
    limpiar_terminal()
    print("Creando Frase con promt")
    Reporte_Bitacora("Creando Frase con promt")
    Star_Phrase = input("")
    Reporte_Bitacora("La frase inicial es: " + Star_Phrase)
    List_Concepts = Star_Phrase.split()
    origin = Create_Semantic_Network()
    print("Generarando Frase.... ")
    Reporte_Bitacora("Generarando Frase.... ")
    origin = Search_Concept(origin, Star_Phrase)
    if origin == None:
        print("No se encontro el concepto")
        Reporte_Bitacora("No se encontro el concepto")
        return
    Phrase = ""
    Phrase = Generate_Phrase(origin, Phrase)
    Phrase = List_Concepts[0] + " " + Phrase
    Reporte_Bitacora("La frase final es: " + Phrase)
    simulate_typing(Phrase)


def Create_Phrase_Random():
    limpiar_terminal()
    print("Creando Frase aleatoria")
    Reporte_Bitacora("Creando Frase aleatoria")
    origin = Create_Semantic_Network()
    print("Generarando Frase.... ")
    Reporte_Bitacora("Generarando Frase.... ")
    Phrase = ""
    Phrase = Generate_Phrase(origin, Phrase)
    Reporte_Bitacora("La frase final es: " + Phrase)
    simulate_typing(Phrase)

    
def Main():
    print("Opciones: ")
    print("1. Generar con un promt")
    print("2. Generar frase aleatoria")

    option = input("Opcion: ")

    return option

limpiar_terminal()
print("Creando una Red Semantica")
Reporte_Bitacora("Creando una Red Semantica")
print ("Desarrollado por: Eduardo Isaac Dávila Bernal 🤓")
Reporte_Bitacora("Desarrollado por: Eduardo Isaac Dávila Bernal 🤓")
print ("Matricula: 2193076785 \n")
Reporte_Bitacora("Matricula: 2193076785 \n")

option = Main()

if option == "1":
    Create_Phrase_Promt()
elif option == "2":
    Create_Phrase_Random()
else:
    while option != "1" and option != "2":
        limpiar_terminal()
        option = Main()
        if option == "1":
            Create_Phrase_Promt()
        elif option == "2":
            Create_Phrase_Random()
        else:
            print("Opcion no valida")