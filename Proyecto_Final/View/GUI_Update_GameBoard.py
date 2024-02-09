from time import sleep
import tkinter as tk
from tkinter import PhotoImage, font
from PIL import Image, ImageTk, ImageFilter
from Config.config import Color_Primary, Color_Text, Color_Button, Color_Button_Text
from Algorithms.Hill_Climbing import Hill_Climbing , Main
from tkinter import messagebox
from Model.Config_Objetive import Read_JSON, Update_JSON
import logging

class Main_Game:
    def __init__(self, opciones, ventana):
        """
        Clase que representa el menú de juego.

        Args:
            opciones (list): Lista de opciones del menú.
            ventana (tkinter.Tk): Ventana principal del juego.
        """
        print("Iniciando menu de juego")
        print("Opciones: ", opciones)

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

        if opcion_seleccionada == "- NO -":
            logging.info('Se ha seleccionado la opción "NO" en el menú de juego.')
            return 0
        elif opcion_seleccionada == "- SI -":
            logging.info('Se ha seleccionado la opción "SI" en el menú de juego.')
            return 1
            

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


class GUI_Update_GameBoard:
    tablero = []

    def __init__(self, Title: str, Tablero: list):
        self.Confirmacion  = 0
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

        self.title_label = tk.Label(self.frame, text= Title, fg=Color_Text, bg=Color_Primary, font=("Game Over", 40))
        self.title_label.pack(pady=(5, 3))

        self.subtitle_label = tk.Label(self.frame, text=" Teclas:   V = Vacio   R = Robot   O = Obstaculo   M = Meta   ESC = Confirmar ", fg=Color_Text, bg=Color_Primary, font=("Game Over", 30))
        self.subtitle_label.pack(pady=(2, 5))

        self.x_puntero = 1
        self.y_puntero = 1
        self.actualizar_puntero = None

        self.ventana.bind("<Up>", self.on_arrow_up)
        self.ventana.bind("<Down>", self.on_arrow_down)
        self.ventana.bind("<Left>", self.on_arrow_left)
        self.ventana.bind("<Right>", self.on_arrow_right)
        self.ventana.bind("<space>", self.on_space)
        self.ventana.bind("<o>", self.on_letter_o)
        self.ventana.bind("<O>", self.on_letter_o)
        self.ventana.bind("<r>", self.on_letter_r)
        self.ventana.bind("<R>", self.on_letter_r)
        self.ventana.bind("<v>", self.on_letter_v)
        self.ventana.bind("<V>", self.on_letter_v)
        self.ventana.bind("<Escape>", self.on_letter_escape)
        self.ventana.bind("<Return>", self.on_enter)
        self.ventana.bind("<m>", self.on_letter_m)
        self.ventana.bind("<M>", self.on_letter_m)
        
    def get_Tablero(self):
        return self.tablero
     
    def set_Tablero(self, value):
        self.tablero = value


    def Reglas(self):
        print("Reglas")
        #Regla 0 - Moverse al norte
        print("Regla 0 - Moverse al norte")
        x, y = self.Encontrar_Posicion_Robot(self.tablero)

        
    def Encontrar_Posicion_Robot(self, Tablero : list):
        print("Encontrando posicion del robot")
        print(len(Tablero))
        print(len(Tablero[0]))
        for i in range(len(Tablero)):
            for j in range(len(Tablero)):
                if Tablero[i][j] == "R":
                    print("Posicion del robot: ", i, j)
                    return j, i

    def Encontrar_Posiciones_Obstaculos(self, Tablero : list):
        print("Encontrando posicion de los obstaculos")
        Lista_Obstaculos = []
        for i in range(len(Tablero)):
            for j in range(len(Tablero)):
                if Tablero[i][j] == "*" and i != 0 and i != 11 and j != 0 and j != 11:
                    obstaculo = []
                    print("Posicion de obstaculo: ", i, j)
                    obstaculo.append(j*40)
                    obstaculo.append(i*40)
                    Lista_Obstaculos.append(obstaculo)
        
        print("Lista de obstaculos: ", Lista_Obstaculos)
        return Lista_Obstaculos

    def Parpadear(self):
        if self.canvas.itemcget(self.puntero, "state") == "normal":
            self.canvas.itemconfigure(self.puntero, state="hidden")
        else:
            self.canvas.itemconfigure(self.puntero, state="normal")
        self.actualizar_puntero = self.frame.after(100, self.Parpadear)
    
                
    def Render(self):        
        # Crear un lienzo (Canvas)
        
        self.canvas = tk.Canvas(self.frame, width=480, height=480, highlightthickness=0)
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
        print("Posicion del robot: ", x, y)
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
                    print("Posicion de personaje: ", i, j)
                    self.canvas.create_image(i+9, j, anchor=tk.NW, image=self.imagen3)       

        self.puntero = self.canvas.create_rectangle(self.x_puntero * 40, self.y_puntero * 40, (self.x_puntero * 40) +  40, (self.y_puntero * 40 ) + 40, outline='yellow', width=5, state="hidden")
        self.Parpadear()
        Axis_X_Objetive = self.Objetive_X * 40
        Axis_Y_Objetive = self.Objetive_Y * 40
        print("Posicion del objetivo: ", Axis_X_Objetive, Axis_Y_Objetive)
        self.canvas.create_line(Axis_X_Objetive, Axis_Y_Objetive, Axis_X_Objetive+40, Axis_Y_Objetive+40, fill="red", width=10)
        self.canvas.create_line(Axis_X_Objetive, Axis_Y_Objetive+40, Axis_X_Objetive+40, Axis_Y_Objetive, fill="red", width=10)

    def Update_GameBoard_Obstacle(self, x, y):
        logging.info('Se ha actualizado el tablero del juego. Se ha añadido un obstáculo en la posición (' + str(x) + ', ' + str(y) + ').')
        self.tablero[y][x] = "*"
    
    def Update_GameBoard_Robot(self, x, y):
        logging.info('Se ha actualizado el tablero del juego. Se ha añadido un robot en la posición (' + str(x) + ', ' + str(y) + ').')
        self.tablero[y][x] = "R"
    
    def Update_GameBoard_Empty(self, x, y):
        logging.info('Se ha actualizado el tablero del juego. Se ha eliminado un elemento en la posición (' + str(x) + ', ' + str(y) + ').')
        self.tablero[y][x] = " "

    def Render_Limits(self):
        print("Renderizando")
        
    def on_arrow_up(self, event):
        if self.Confirmacion == 0:
            if self.y_puntero == 1:
                self.y_puntero = 11
            self.y_puntero = self.y_puntero - 1
            self.frame.after_cancel(self.actualizar_puntero)
            self.canvas.delete("all")
            self.canvas.destroy()
            self.Render()
        else:
            self.menu_juego.navegar_arriba(event)

    def on_arrow_down(self, event):
        if self.Confirmacion == 0:
            if self.y_puntero == 10:
                self.y_puntero = 0
            self.y_puntero = self.y_puntero + 1
            self.frame.after_cancel(self.actualizar_puntero)
            self.canvas.delete("all")
            self.canvas.destroy()
            self.Render()
        else:
            self.menu_juego.navegar_abajo(event)

    def on_arrow_left(self, event):
        if self.Confirmacion == 0:
            if self.x_puntero == 1:
                self.x_puntero = 11
            self.x_puntero = self.x_puntero - 1
            self.frame.after_cancel(self.actualizar_puntero)
            self.canvas.delete("all")
            self.canvas.destroy()
            self.Render()
    
    def on_arrow_right(self, event):
        if self.Confirmacion == 0:
            if self.x_puntero == 10:
                self.x_puntero = 0
            self.x_puntero = self.x_puntero + 1
            self.frame.after_cancel(self.actualizar_puntero)
            self.canvas.delete("all")
            self.canvas.destroy()
            self.Render()

    def on_space(self, event):
        print("Espacio")

    def on_letter_o(self, event):
        print("O")
        self.Update_GameBoard_Obstacle(self.x_puntero, self.y_puntero)
        self.frame.after_cancel(self.actualizar_puntero)
        self.canvas.delete("all")
        self.canvas.destroy()
        self.Render()

    def on_letter_r(self, event):
        print("R")
        x, y = self.Encontrar_Posicion_Robot(self.tablero)
        self.Update_GameBoard_Empty(x,y)
        self.Update_GameBoard_Robot(self.x_puntero, self.y_puntero)
        self.frame.after_cancel(self.actualizar_puntero)
        self.canvas.delete("all")
        self.canvas.destroy()
        self.Render()

    def on_letter_v(self, event):
        print("V")
        x, y = self.Encontrar_Posicion_Robot(self.tablero)
        if self.x_puntero == x and self.y_puntero == y:
            self.Update_GameBoard_Robot(self.x_puntero, self.y_puntero)
        else:
            self.Update_GameBoard_Empty(self.x_puntero,self.y_puntero)
        self.frame.after_cancel(self.actualizar_puntero)
        self.canvas.delete("all")
        self.canvas.destroy()
        self.Render()

    def on_letter_m(self, event):
        print("M")
        self.Update_GameBoard_Empty(self.Objetive_X, self.Objetive_Y)
        self.Objetive_X = self.x_puntero
        self.Objetive_Y = self.y_puntero
        self.frame.after_cancel(self.actualizar_puntero)
        self.canvas.delete("all")
        self.canvas.destroy()
        self.Render()

    def on_enter(self, event):
        option = self.menu_juego.seleccionar_opcion(self.ventana)
        if option == 0:
            self.pregunta.destroy()
            self.menu_juego.destroy()
            self.Confirmacion = 0
            self.Render()
        elif option == 1:
            print("Confirmado")
            from Model.Config_GameBoard import Update_GameBoard
            Update_GameBoard(self.tablero)
            print("Objetivo: ", self.Objetive_X, self.Objetive_Y)
            Update_JSON(self.Objetive_X, self.Objetive_Y)
            self.ventana.destroy()
            from View.GUI_Settings import GUI_Settings
            app = GUI_Settings()
            app.run()
    
    def on_letter_escape(self, event):
        if self.Confirmacion == 0:
            self.frame.after_cancel(self.actualizar_puntero)
            self.canvas.delete("all")
            self.canvas.destroy()

            self.pregunta = tk.Label(self.frame, text=" ¿Deseas confirmar la actualización del Game Board ", fg=Color_Text, bg=Color_Primary, font=("Game Over", 50))
            self.pregunta.pack(pady=(100, 50))
            self.Confirmacion = 1
            
            self.menu_juego = Main_Game(["- SI -","- NO -"], self.frame)
            self.menu_juego.iniciar()
        else:
            self.pregunta.destroy()
            self.menu_juego.destroy()
            self.Confirmacion = 0
            self.Render()

    def run(self):
        logging.info('Se ha iniciado la ventana de configuración del Game Board.')
        self.ventana.mainloop()