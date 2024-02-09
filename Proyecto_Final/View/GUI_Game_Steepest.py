import tkinter as tk
from tkinter import PhotoImage, font
from PIL import Image, ImageTk, ImageFilter
from Config.config import Color_Primary, Color_Text, Color_Button, Color_Button_Text

from Model.Config_Objetive import Read_JSON
import threading

import pyautogui
import time
import copy
import types
import sys
import logging

class Main_Game:
    def __init__(self, opciones, ventana):
        """
        Clase que representa el menú de juego.

        Args:
            opciones (list): Lista de opciones del menú.
            ventana (tkinter.Tk): Ventana principal del juego.
        """

        self.opciones = opciones
        self.indice_opcion_actual = 0

        # Crear un marco para organizar las etiquetas
        self.marco = tk.Frame(ventana, bg="#244D24")
        self.marco.pack()

        # Crear etiquetas para cada opción en el menú
        self.etiquetas_opciones = []
        for opcion in opciones:
            etiqueta = tk.Label(self.marco, text=opcion, font=("Game Over", 50), fg="white", bg="black", width=100)
            self.etiquetas_opciones.append(etiqueta)

        # Mostrar las etiquetas en el marco
        self.actualizar_resaltado()

    def navegar_arriba(self, event):
        """
        Método para navegar hacia arriba en el menú.

        Args:
            event (tkinter.Event): Evento de tecla presionada.
        """
        if self.indice_opcion_actual > 0:
            self.indice_opcion_actual -= 1
            self.actualizar_resaltado()

    def navegar_abajo(self, event):
        """
        Método para navegar hacia abajo en el menú.

        Args:
            event (tkinter.Event): Evento de tecla presionada.
        """
        if self.indice_opcion_actual < len(self.opciones) - 1:
            self.indice_opcion_actual += 1
            self.actualizar_resaltado()

    def seleccionar_opcion(self, ventana):
        """
        Método para seleccionar una opción del menú.

        Args:
            ventana (tkinter.Tk): Ventana principal del juego.
        """
        opcion_seleccionada = self.opciones[self.indice_opcion_actual]
       
        if opcion_seleccionada == "- COMENZAR -":
            logging.info("Se ha comenzado el juego con el algoritmo Steepest.")
            return True
        else:
            return False
            

    def actualizar_resaltado(self):
        """
        Método para actualizar el resaltado de la opción seleccionada en el menú.
        """
        for i, etiqueta in enumerate(self.etiquetas_opciones):
            if i == self.indice_opcion_actual:
                etiqueta.config(fg=Color_Button_Text,bg=Color_Button, font=("Game Over", 50))
            else:
                etiqueta.config(fg=Color_Button, bg=Color_Button_Text, font=("Game Over", 50))

    def iniciar(self):
        """
        Método para iniciar el menú de juego.
        """
        for etiqueta in self.etiquetas_opciones:
            etiqueta.pack(pady=5)
    
    def destroy(self):
        for etiqueta in self.etiquetas_opciones:
            etiqueta.destroy()
        self.marco.destroy()

def center_window(window: tk.Tk):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 2)
    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))

class Game:
    tablero = []

    def __init__(self, Title: str, Tablero: list):
        self.Confirmation = False
        self.data = Read_JSON()
        self.Objetive_X = self.data['x_axis']
        self.Objetive_Y = self.data['y_axis']
        
        self.ventana = tk.Tk()
        self.ventana.geometry("600x600")
        self.ventana.title("The Game")
        self.ventana.configure(bg=Color_Primary)
        self.ventana.resizable(False, False)
        center_window(self.ventana)

        self.frame = tk.Frame(self.ventana, width=600, height=600)
        self.frame.pack(fill='both', expand=1)

        # Cargar la imagen de fondo
        imagen_b = Image.open("./Textures/Background_Alternative.jpg")  # Reemplaza "ruta_de_la_imagen.jpg" con la ruta de tu imagen
        # Escalar la imagen al tamaño del Frame
        imagen_redimensionada = imagen_b.resize((600, 600))
        imagen_b = ImageTk.PhotoImage(imagen_redimensionada)

        # Agregar la imagen al Frame
        fondo_label = tk.Label(self.frame, image=imagen_b)
        fondo_label.place(relwidth=1, relheight=1)

        self.frame.config(cursor="circle")
        self.frame.config(bg=Color_Primary)
        self.frame.config(bd=20)
        self.frame.config(relief="sunken")

        self.frame.imagen = imagen_b

        self.tablero = Tablero
        self.Game_Board = Game_Board(self.tablero)
        self.menu_juego = None
        
        self.ventana.bind("<Up>", self.on_arrow_up)
        self.ventana.bind("<Down>", self.on_arrow_down)
        self.ventana.bind("<Return>", self.on_enter)
        self.ventana.bind("<Left>", self.on_arrow_left)
        self.ventana.bind("<Right>", self.on_arrow_right)
        self.ventana.bind("<R>", self.press_render)
        self.ventana.bind("<r>", self.press_render)
        self.ventana.bind("<S>", self.press_success)
        self.ventana.bind("<s>", self.press_success)
        self.ventana.bind("<F>", self.press_failed)
        self.ventana.bind("<f>", self.press_failed)

        self.title_label = tk.Label(self.frame, text= Title, fg=Color_Text, bg=Color_Primary, font=("Game Over", 70))
        self.title_label.pack(pady=(10, 10))
        logging.info("Se ha creado la ventana de juego.")
        self.Start_Game()
        
        
        
    def Start_Game(self):
        self.title_label = tk.Label(self.frame, text= " ¡Listo para comenzar! ", fg=Color_Text, bg=Color_Primary, font=("Game Over", 100))
        self.title_label.pack(pady=(100, 20))
        self.subtitle_label = tk.Label(self.frame, text=" Presione ENTER para continuar ", fg=Color_Text, bg=Color_Primary, font=("Game Over", 50))
        self.subtitle_label.pack(pady=(0, 50))
        self.menu_juego = Main_Game(["- COMENZAR -"], self.frame)
        self.menu_juego.iniciar()
        
    def Encontrar_Posicion_Robot(self, Tablero : list):
        logging.info('Encontrando posicion del robot.')
        for i in range(len(Tablero)):
            for j in range(len(Tablero)):
                if Tablero[i][j] == "R":
                    logging.info('Se ha encontrado el robot en la posicion: ' + str(i) + ', ' + str(j))
                    return j, i

    def Encontrar_Posiciones_Obstaculos(self, Tablero : list):
        logging.info('Encontrando posicion de los obstaculos.')
        Lista_Obstaculos = []
        for i in range(len(Tablero)):
            for j in range(len(Tablero)):
                if Tablero[i][j] == "*" and i != 0 and i != 11 and j != 0 and j != 11:
                    obstaculo = []
                    logging.info('Se ha encontrado un obstaculo en la posicion: ' + str(i) + ', ' + str(j))
                    obstaculo.append(j*40)
                    obstaculo.append(i*40)
                    Lista_Obstaculos.append(obstaculo)
        return Lista_Obstaculos
          
    def Render(self):
        # Crear un lienzo (Canvas)
        
        self.canvas = tk.Canvas(self.frame, width=480, height=480)
        self.canvas.pack()

        # Cargar la imagen
        self.imagen_path = "Textures/empty.png"  # Reemplaza con la ruta de tu imagen
        self.imagen_pillow = Image.open(self.imagen_path)
        self.imagen = ImageTk.PhotoImage(self.imagen_pillow)

        self.imagen_path2 = "Textures/indestructible_wall.png"  # Reemplaza con la ruta de tu imagen
        self.imagen_pillow2 = Image.open(self.imagen_path2)
        self.imagen2 = ImageTk.PhotoImage(self.imagen_pillow2)

        self.imagen_path3 = "Textures/Robot.png"  # Reemplaza con la ruta de tu imagen
        self.imagen_pillow3 = Image.open(self.imagen_path3)
        self.imagen_pillow3 = self.imagen_pillow3.resize((22, 40))
        self.imagen3 = ImageTk.PhotoImage(self.imagen_pillow3)

        x, y = self.Encontrar_Posicion_Robot(self.tablero)

        Lista_Obstaculos = self.Encontrar_Posiciones_Obstaculos(self.tablero)

        # Agregar la imagen al lienzo en las coordenadas (0, 0)
        for i in range(0, 480, 40):
            for j in range(0, 480, 40):
                #print("Posicion: ", i, j)
                if i == 0 or i == 440 or j == 0 or j == 440:
                    self.canvas.create_image(i, j, anchor=tk.NW, image=self.imagen2)
                else:
                    if [i, j] in Lista_Obstaculos:
                        self.canvas.create_image(i, j, anchor=tk.NW, image=self.imagen2)
                    else:
                        self.canvas.create_image(i, j, anchor=tk.NW, image=self.imagen)
                
                if i == x * 40 and j == y * 40:
                    self.canvas.create_image(i+9, j, anchor=tk.NW, image=self.imagen3)
        
        Axis_X_Objetive = self.Objetive_X * 40
        Axis_Y_Objetive = self.Objetive_Y * 40
        print("Posicion del objetivo: ", Axis_X_Objetive, Axis_Y_Objetive)
        self.canvas.create_line(Axis_X_Objetive, Axis_Y_Objetive, Axis_X_Objetive+40, Axis_Y_Objetive+40, fill="red", width=10)
        self.canvas.create_line(Axis_X_Objetive, Axis_Y_Objetive+40, Axis_X_Objetive+40, Axis_Y_Objetive, fill="red", width=10)
        logging.info('Se ha renderizado el tablero de juego.')

    def press_render(self, event):
        logging.info('Se esta renderizando el tablero de juego.')
        self.Game_Board.Print_GameBoard()
        self.tablero = self.Game_Board.Game_Board
        self.canvas.delete("all")
        self.canvas.destroy()
        self.Render()
    
    def press_success(self, event):
        pyautogui.alert("¡El robot a llegado a la Meta!", "¡Se encontro la meta!")
        logging.info('El robot a llegado a la Meta.')
    
    def press_failed(self, event):
        pyautogui.alert("¡El robot no a llegado a la Meta!", "¡No se encontro la meta!")
        logging.info('El robot no a llegado a la Meta.')

    def on_arrow_up(self, event):
        if self.Confirmation == True:
            x, y = self.Game_Board.Search_Robot()
            if self.Game_Board.Motion_Up(x, y) == True:
                self.canvas.delete("all")
                self.canvas.destroy()
                self.Render()
            else:
                print("No se puede mover hacia arriba")
        self.menu_juego.navegar_arriba(event)

    def on_arrow_down(self, event):
        if self.Confirmation == True:
            x, y = self.Game_Board.Search_Robot()
            if self.Game_Board.Motion_Down(x, y) == True:
                self.canvas.delete("all")
                self.canvas.destroy()
                self.Render()
            else:
                print("No se puede mover hacia abajo")
        self.menu_juego.navegar_abajo(event)
    
    def on_arrow_left(self, event):
        if self.Confirmation == True:
            x, y = self.Game_Board.Search_Robot()
            if self.Game_Board.Motion_Left(x, y) == True:
                self.canvas.delete("all")
                self.canvas.destroy()
                self.Render()
            else:
                print("No se puede mover hacia la izquierda")
        self.menu_juego.navegar_abajo(event)

    def on_arrow_right(self, event):
        if self.Confirmation == True:
            x, y = self.Game_Board.Search_Robot()
            if self.Game_Board.Motion_Right(x, y) == True:
                self.canvas.delete("all")
                self.canvas.destroy()
                self.Render()
            else:
                print("No se puede mover hacia la derecha")
        self.menu_juego.navegar_abajo(event)

    def on_enter(self, event):
        Option = self.menu_juego.seleccionar_opcion(self.ventana)
        if Option == True:
            self.Confirmation = True
            self.title_label.destroy()
            self.subtitle_label.destroy()
            self.menu_juego.destroy()
            self.Render()
            self.canvas.delete("all")
            self.canvas.destroy()
            self.Render()
            self.Implementation = Steepest(self.Game_Board)
            logging.info('Se ha iniciado el juego con el algoritmo Steepest.')
            hilo = threading.Thread(target=self.Implementation.Search)
            logging.info('Se ha iniciado el algoritmo Steepest en un subproceso aparte.')

            hilo.start()
            
    def run(self):
        logging.info('Se iniciara el juego con el algoritmo Steepest.')
        self.ventana.mainloop()

class Game_Board:
    def __init__(self, Game_Board : list):
        self.Game_Board = Game_Board
        self.data = Read_JSON()
        self.Objetive_X = self.data['x_axis']
        self.Objetive_Y = self.data['y_axis']
        logging.info('Se ha creado el GameBoard de juego.')
    
    def Print_GameBoard(self):
        for i in range(len(self.Game_Board)):
            print(self.Game_Board[i])

    def Search_Robot(self):
        for i in range(len(self.Game_Board)):
            for j in range(len(self.Game_Board[i])):
                if self.Game_Board[i][j] == "R":
                    return j, i
                
    def Search_Objetive(self):
        return self.Objetive_X, self.Objetive_Y
        
    
    def Motion_Up(self, x, y):
        logging.info('Se ha movido el robot hacia arriba.')
        if self.Game_Board[y-1][x] == " ":
            self.Game_Board[y][x] = " "
            self.Game_Board[y-1][x] = "R"
            return True
        else:
            return False
        
    def Motion_Down(self, x, y):
        if self.Game_Board[y+1][x] == " ":
            logging.info('Se ha movido el robot hacia abajo.')
            self.Game_Board[y][x] = " "
            self.Game_Board[y+1][x] = "R"

            Evaluacion = 1
            if self.Game_Board[y+2][x] == " ":
                Evaluacion = Evaluacion + 1

            return True , Evaluacion
        else:
            return False , 0
    
    def Motion_Left(self, x, y):
        if self.Game_Board[y][x-1] == " ":
            logging.info('Se ha movido el robot hacia la izquierda.')
            self.Game_Board[y][x] = " "
            self.Game_Board[y][x-1] = "R"

            Evaluacion = -3
            
            return True , Evaluacion
        else:
            return False , 0
    
    def Motion_Right(self, x, y):
        if self.Game_Board[y][x+1] == " ":
            logging.info('Se ha movido el robot hacia la derecha.')
            self.Game_Board[y][x] = " "
            self.Game_Board[y][x+1] = "R"

            Evaluacion = -3

            return True , Evaluacion
        else:
            return False , 0
        
    def Motion_Suroeste(self, x, y):
        if self.Game_Board[y+1][x-1] == " ":
            logging.info('Se ha movido el robot hacia el suroeste.')
            self.Game_Board[y][x] = " "
            self.Game_Board[y+1][x-1] = "R"

            Evaluacion = 1
            if self.Game_Board[y+2][x-1] == " ":
                Evaluacion = Evaluacion + 1

            return True , Evaluacion
        else:
            return False , 0
        
    def Motion_Sureste(self, x, y):
        if self.Game_Board[y+1][x+1] == " ":
            logging.info('Se ha movido el robot hacia el sureste.')
            self.Game_Board[y][x] = " "
            self.Game_Board[y+1][x+1] = "R"

            Evaluacion = 1
            if self.Game_Board[y+2][x+1] == " ":
                Evaluacion = Evaluacion + 1

            return True , Evaluacion
        else:
            return False , 0
        
        
class Steepest:
    def __init__(self, Game_Board : Game_Board):
        logging.info('Se ha iniciado el algoritmo Steepest en subproceso.')
        self.Game_Board = Game_Board
       
    def Movimientos(self, Movimientos_Realizados : list):
        logging.info('Se esta buscando realizar algun movimiento.')
        x, y = self.Game_Board.Search_Robot()
        
        if 1 not in Movimientos_Realizados:
            Validado , Evaluacion = self.Game_Board.Motion_Down(x, y)
            if Validado == True:
                return 1 , Evaluacion
        if 2 not in Movimientos_Realizados:
            Validado , Evaluacion = self.Game_Board.Motion_Left(x, y)
            if Validado == True:
                return 2 , Evaluacion
        if 3 not in Movimientos_Realizados:
            Validado , Evaluacion = self.Game_Board.Motion_Right(x, y)
            if Validado == True:
                return 3 , Evaluacion
        if 4 not in Movimientos_Realizados:
            Validado , Evaluacion = self.Game_Board.Motion_Suroeste(x, y)
            if Validado == True:
                return 4 , Evaluacion
        if 5 not in Movimientos_Realizados:
            Validado , Evaluacion = self.Game_Board.Motion_Sureste(x, y)
            if Validado == True:
                return 5 , Evaluacion
            
        return None, None
    
    def Evaluar_Estado(self, Evaluacion_Actual, Evaluacion_Siguiente):
        logging.info('Se esta evaluando el estado actual del tablero de juego con los valores de evaluación actual = ' + str(Evaluacion_Actual) + ' y evaluación siguiente = ' + str(Evaluacion_Siguiente) + '.')
        if Evaluacion_Actual > Evaluacion_Siguiente:
            logging.info('El estado actual del tablero de juego es mejor que el estado siguiente.')
            return False
        else:
            logging.info('El estado siguiente del tablero de juego es mejor que el estado actual.')
            return True
    
    def Validar_Solucion (self):
        Objetivo_X, Objetivo_Y = self.Game_Board.Search_Objetive()
        Robot_X , Robot_Y  = self.Game_Board.Search_Robot()
        logging.info('Se esta validando si el robot ha llegado a la meta.')
        if Robot_X == Objetivo_X and Robot_Y == Objetivo_Y:
            logging.info('El robot ha llegado a la meta.')
            return True
        else:
            logging.info('El robot no ha llegado a la meta.')
            return False
        
    def Estado_Mayor_Evaluacion(self, Valores_Evaluacion):
        logging.info('Se esta buscando el estado con la mayor evaluación.')
        Mayor = Valores_Evaluacion[0]
        Posicion_Mayor = 0
        for i in range(len(Valores_Evaluacion)):
            if Valores_Evaluacion[i] > Mayor:
                Mayor = Valores_Evaluacion[i]
                Posicion_Mayor = i
        return Mayor , Posicion_Mayor

        
    def Algoritmo_Steepest(self, Evaluacion_Estado):
        logging.info('Se esta aplicando el algoritmo Steepest.')
        logging.info('Evaluacion del estado: ' + str(Evaluacion_Estado))

        if self.Validar_Solucion():
            logging.info('🤖 El robot ha llegado a la meta.')
            pyautogui.press("R")
            pyautogui.press("S")

        else:
            pyautogui.press("R")
            Movimientos_Realizados = []
            Reglas = []
            Valores_Evaluacion = []

            Game_Board_Original = copy.deepcopy(self.Game_Board.Game_Board)
            logging.info('Se ha copiado el tablero de juego original.')

            for i in range(5):
                Game_Board_AUX = copy.deepcopy(self.Game_Board.Game_Board)
                logging.info('Se ha copiado el tablero de juego auxiliar.')

                self.Game_Board.Game_Board = Game_Board_AUX
                                
                Movimiento, Evaluacion = self.Movimientos(Movimientos_Realizados)
                logging.info('Se ha realizado el movimiento: ' + str(Movimiento))

                if Movimiento is not None and Evaluacion is not None:
                    Evaluacion_Aux = Evaluacion_Estado + Evaluacion
                    Reglas.append(Movimiento)
                    Valores_Evaluacion.append(Evaluacion_Aux)
                    Movimientos_Realizados.append(Movimiento)
                
                self.Game_Board.Game_Board = copy.deepcopy(Game_Board_Original)
                logging.info('Se ha restaurado el tablero de juego original.')
            
            logging.info('Reglas aplicables: ' + str(Reglas))
            
            if len(Reglas) > 0:
                Movimientos_No_Realizados = []

                Mayor_Evaluacion , Posicion = self.Estado_Mayor_Evaluacion(Valores_Evaluacion)
                
                logging.info('Mayor evaluación: ' + str(Mayor_Evaluacion))
                logging.info('Posición mayor evaluación: ' + str(Posicion))

                for i in range(1, 6):
                    if i != Reglas[Posicion]:
                        Movimientos_No_Realizados.append(i)

                logging.info('Movimientos no realizados: ' + str(Movimientos_No_Realizados))
                
                Game_Board_AUX = copy.deepcopy(Game_Board_Original)
                logging.info('Se ha copiado el tablero de juego auxiliar.')
                
                self.Game_Board.Game_Board = copy.deepcopy(Game_Board_AUX)
                logging.info('Se ha restaurado el tablero de juego original.')

                Regla_Aplicada , Evaluacion = self.Movimientos(Movimientos_No_Realizados)
                if Regla_Aplicada is not None and Evaluacion is not None:
                    logging.info('Se ha aplicado la regla: ' + str(Regla_Aplicada))
                    logging.info('Evaluación: ' + str(Evaluacion))
                    Evaluacion_Aux = Evaluacion_Estado + Evaluacion
                    logging.info('Evaluación del estado: ' + str(Evaluacion_Aux))

                    if (self.Evaluar_Estado(Evaluacion_Estado, Evaluacion_Aux)):
                        Evaluacion_Estado = Evaluacion_Estado + Evaluacion
                        Movimientos_Realizados.append(Regla_Aplicada)
                        logging.info('Evaluación del estado original: ' + str(Evaluacion_Estado))
                        self.Algoritmo_Steepest(Evaluacion_Estado)
                    else:
                        logging.info('🤖 Robot no puede llegar a la meta!')
                        print("Maximo local alcanzado!")
                        pyautogui.press("F")
    
    def Search(self):
        self.Algoritmo_Steepest(0)