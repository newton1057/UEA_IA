from PIL import Image, ImageTk, ImageFilter
import tkinter as tk
from tkinter import font
from View.GUI_Modos_Juego import Modos_Juego
from Config.config import Color_Primary, Color_Text, Color_Button, Color_Button_Text
from pygame import mixer

import time
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
        if opcion_seleccionada == "- SALIR -":
            from The_Game import detener_musica
            detener_musica()
            logging.info('Se ha seleccionado la opción de salir.')
            ventana.destroy()
        elif opcion_seleccionada == "- INICIAR PARTIDA -":
            ventana.destroy()
            logging.info('Se ha seleccionado la opción de iniciar partida.')
            app = Modos_Juego()
            app.run()

        elif opcion_seleccionada == "-CONFIGURACIÓN-":
            ventana.destroy()
            logging.info('Se ha seleccionado la opción de configuración.')
            from View.GUI_Settings import GUI_Settings
            app = GUI_Settings()
            app.run()

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

def center_window(window: tk.Tk):
    """
    Función para centrar una ventana en la pantalla.

    Args:
        window (tkinter.Tk): Ventana a centrar.
    """
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 2)
    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))

class JuegoApp:
    def __init__(self):
        """
        Clase que representa la aplicación principal del juego.
        """
        self.ventana = tk.Tk()
        self.ventana.geometry("600x600")
        self.ventana.title("The Game")
        self.ventana.configure(bg=Color_Primary)
        self.ventana.resizable(False, False)
        center_window(self.ventana)

        self.frame = tk.Frame(self.ventana, width=600, height=600)
        self.frame.pack(fill='both', expand=1)

        # Cargar la imagen
        imagen_b = Image.open("./Textures/Background.jpg")  # Reemplaza "ruta_de_la_imagen.jpg" con la ruta de tu imagen
         # Escalar la imagen al tamaño del Frame
        imagen_redimensionada = imagen_b.resize((600, 600))

        imagen_b = ImageTk.PhotoImage(imagen_redimensionada)

        # Agregar la imagen al fondo del Frame usando un Label
        fondo_label = tk.Label(self.frame, image=imagen_b)
        fondo_label.place(relwidth=1, relheight=1)

        self.frame.config(cursor="circle")
        self.frame.config(bg=Color_Primary)
        self.frame.config(bd=20)
        self.frame.config(relief="sunken")

        # Asegurarse de mantener una referencia a la imagen para evitar que sea eliminada por el recolector de basura
        self.frame.imagen = imagen_b

        self.title_label = tk.Label(self.frame, text=" The Game ", fg=Color_Text, bg="#489848", font=("Game Over", 200))
        self.title_label.pack(pady=(100, 0))
        

        self.subtitle_label = tk.Label(self.frame, text=" For IA by Eduardo Bernal ", fg="#377537", bg="#489848", font=("Game Over", 60))
        self.subtitle_label.pack(pady=(0, 50))

        self.canvas = tk.Canvas(self.frame, width=600, height=64, highlightthickness=0, bg=Color_Primary)
        
        self.canvas.pack(pady=(0, 0))

        self.gif_path = "./Textures/Bomberman_Menu.gif"
        
        self.gif_frames = self.extract_gif_frames()

        self.gif_frames = [frame.resize((int(frame.width * 0.25), int(frame.height * 0.25))) for frame in self.gif_frames]

        # Mostrar el primer frame
        self.current_frame_index = 0
        self.current_frame = ImageTk.PhotoImage(self.gif_frames[self.current_frame_index])

        # Iniciar la animación
        self.position = 0
        self.direction = "R"
        self.animate()

        self.menu_juego = Main_Game(["- INICIAR PARTIDA -","-CONFIGURACIÓN-","- SALIR -"], self.frame)

        self.ventana.bind("<Up>", self.on_arrow_up)
        self.ventana.bind("<Down>", self.on_arrow_down)
        self.ventana.bind("<Return>", self.on_enter)

        self.menu_juego.iniciar()
    
    def extract_gif_frames(self):
        """
        Función para extraer los frames de un archivo GIF.

        Returns:
            list: Lista de frames del GIF.
        """
        gif = Image.open(self.gif_path)
        frames = []
        try:
            while True:
                frames.append(gif.copy())
                gif.seek(len(frames))
        except EOFError:
            pass
        return frames

    def animate(self):
        """
        Método para animar el GIF en el lienzo.
        """
        if self.direction == "R":
            self.position += 10
        
        if self.position == 500:
            self.direction = "L"
        
        if self.direction == "L":
            self.position -= 10

        if self.position == 0:
            self.direction = "R"
            self.position = 0

        # Cambiar al siguiente frame
        self.current_frame_index = (self.current_frame_index + 1) % len(self.gif_frames)
        self.current_frame = ImageTk.PhotoImage(self.gif_frames[self.current_frame_index])
        
        # Actualizar la imagen en el lienzo
        self.canvas.create_image(self.position, 0, anchor=tk.NW, image=self.current_frame)
        
        # Llamar a la función animate después de un cierto tiempo (en milisegundos)
        self.frame.after(100, self.animate)
    

    def on_arrow_up(self, event):
        """
        Método para manejar el evento de tecla de flecha hacia arriba.

        Args:
            event (tkinter.Event): Evento de tecla presionada.
        """
        self.menu_juego.navegar_arriba(event)

    def on_arrow_down(self, event):
        """
        Método para manejar el evento de tecla de flecha hacia abajo.

        Args:
            event (tkinter.Event): Evento de tecla presionada.
        """
        self.menu_juego.navegar_abajo(event)

    def on_enter(self, event):
        """
        Método para manejar el evento de tecla Enter.

        Args:
            event (tkinter.Event): Evento de tecla presionada.
        """
        self.menu_juego.seleccionar_opcion(self.ventana)

    def run(self):
        """
        Método para ejecutar la aplicación principal del juego.
        """
        logging.info('Se ha iniciado la GUI_Principal del juego.')
        self.ventana.mainloop()