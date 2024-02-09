import tkinter as tk
from tkinter import font
from Config.config import Color_Primary, Color_Text, Color_Button, Color_Button_Text
from PIL import Image, ImageTk, ImageFilter
import logging

class MenuJuego:
    def __init__(self, opciones, ventana):
        self.opciones = opciones
        self.indice_opcion_actual = 0

        # Crear un marco para organizar las etiquetas
        self.marco = tk.Frame(ventana, bg=Color_Button_Text)
        self.marco.pack()

        # Crear etiquetas para cada opción en el menú
        self.etiquetas_opciones = []
        for opcion in opciones:
            etiqueta = tk.Label(self.marco, text=opcion, font=("Game Over", 60), fg="white", bg="black", width=100)
            self.etiquetas_opciones.append(etiqueta)

        # Mostrar las etiquetas en el marco
        self.actualizar_resaltado()

    def navegar_arriba(self, event):
        if self.indice_opcion_actual > 0:
            self.indice_opcion_actual -= 1
            self.actualizar_resaltado()

    def navegar_abajo(self, event):
        if self.indice_opcion_actual < len(self.opciones) - 1:
            self.indice_opcion_actual += 1
            self.actualizar_resaltado()

    def seleccionar_opcion(self, ventana):
        # ... (tu código actual)
        opcion_seleccionada = self.opciones[self.indice_opcion_actual]
        print(f"Opción seleccionada: {opcion_seleccionada}")

        if opcion_seleccionada == "Atrás":
            ventana.destroy()
            logging.info('Se ha regresado al menú principal.')
            from View.GUI_Principal import JuegoApp
            app = JuegoApp()
            app.run()

        elif opcion_seleccionada == "Hill Climbing":
            ventana.destroy()
            logging.info('Se ha seleccionado el algoritmo Hill Climbing.')
            from View.GUI_Game_Hill_Climbing import Game
            from Model.Config_GameBoard import Config_GameBoard

            Tablero = Config_GameBoard()

            app = Game(" Algoritmo Hill Climbing Original ",Tablero)
            app.run()
            

        elif opcion_seleccionada == "Hill Climbing Alternativo":
            ventana.destroy()
            logging.info('Se ha seleccionado el algoritmo Hill Climbing Alternativo.')
            from View.GUI_Game_Hill_Climbing_Alternativo import Game
            from Model.Config_GameBoard import Config_GameBoard

            Tablero = Config_GameBoard()
            
            app = Game(" Algoritmo Hill Climbing Alternativo",Tablero)
            app.run()
        
        elif opcion_seleccionada == "Steepest":
            ventana.destroy()
            logging.info('Se ha seleccionado el algoritmo Steepest.')
            from View.GUI_Game_Steepest import Game
            from Model.Config_GameBoard import Config_GameBoard

            Tablero = Config_GameBoard()

            app = Game(" Algoritmo Steepest Original ",Tablero)
            app.run()

        elif opcion_seleccionada == "Steepest Alternativo":
            ventana.destroy()
            logging.info('Se ha seleccionado el algoritmo Steepest Alternativo.')
            from View.GUI_Game_Steepest_Alternativo import Game
            from Model.Config_GameBoard import Config_GameBoard

            Tablero = Config_GameBoard()

            app = Game(" Algoritmo Steepest Alternativo ",Tablero)
            app.run()

        elif opcion_seleccionada == "Beam Search":
            ventana.destroy()
            logging.info('Se ha seleccionado el algoritmo Beam Search.')
            from View.GUI_Game_Beam_Search import Game
            from Model.Config_GameBoard import Config_GameBoard

            Tablero = Config_GameBoard()

            app = Game(" Algoritmo Beam Search ",Tablero)
            app.run()
            

    def actualizar_resaltado(self):
        for i, etiqueta in enumerate(self.etiquetas_opciones):
            if i == self.indice_opcion_actual:
                etiqueta.config(fg=Color_Button_Text, bg=Color_Button, font=("Game Over", 50))
            else:
                etiqueta.config(fg=Color_Button, bg=Color_Button_Text, font=("Game Over", 50))

    def iniciar(self):
        for etiqueta in self.etiquetas_opciones:
            etiqueta.pack(pady=5)

def center_window(window: tk.Tk):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 2)
    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))

class Modos_Juego:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.geometry("600x600")
        self.ventana.title("The Game")
        self.ventana.configure(bg=Color_Primary)
        self.ventana.resizable(False, False)
        center_window(self.ventana)

        self.frame = tk.Frame(self.ventana, width=600, height=600)
        self.frame.pack(fill='both', expand=1)

        # Cargar la imagen de fondo
        imagen_b = Image.open("./Textures/Background_Alternative.jpg")
        imagen_redimensionada = imagen_b.resize((600, 600))

        imagen_b = ImageTk.PhotoImage(imagen_redimensionada)

        # Escalar la imagen al tamaño del Frame
        fondo_label = tk.Label(self.frame, image=imagen_b)
        fondo_label.place(relwidth=1, relheight=1)

        self.frame.config(cursor="circle")
        self.frame.config(bg=Color_Primary)
        self.frame.config(bd=20)
        self.frame.config(relief="sunken")

        self.frame.imagen = imagen_b

        self.title_label = tk.Label(self.frame, text=" MODOS DE JUEGO ", fg=Color_Text, bg=Color_Primary, font=("Game Over", 100))
        self.title_label.pack(pady=(50, 20))

        self.subtitle_label = tk.Label(self.frame, text=" Algoritmos a utilizar ", fg="#377537", bg=Color_Primary, font=("Game Over", 60))
        self.subtitle_label.pack(pady=(80,  20))

        self.menu_juego = MenuJuego(["Hill Climbing", "Hill Climbing Alternativo", "Steepest", "Steepest Alternativo","Beam Search", "Atrás"], self.frame)

        self.ventana.bind("<Up>", self.on_arrow_up)
        self.ventana.bind("<Down>", self.on_arrow_down)
        self.ventana.bind("<Return>", self.on_enter)

        self.menu_juego.iniciar()

    def on_arrow_up(self, event):
        self.menu_juego.navegar_arriba(event)

    def on_arrow_down(self, event):
        self.menu_juego.navegar_abajo(event)

    def on_enter(self, event):
        self.menu_juego.seleccionar_opcion(self.ventana)

    def run(self):
        logging.info('Se ha iniciado el menú de modos de juego.')
        self.ventana.mainloop()
