import tkinter as tk
from tkinter import PhotoImage, font
from PIL import Image, ImageTk, ImageFilter
from Config.config import Color_Primary, Color_Text, Color_Button, Color_Button_Text
from Algorithms.Hill_Climbing import Hill_Climbing , Main

def center_window(window: tk.Tk):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 2)
    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))


class Game:
    tablero = []

    def __init__(self, Tablero: list):
        self.ventana = tk.Tk()
        self.ventana.geometry("600x600")
        self.ventana.title("The Game")
        self.ventana.configure(bg=Color_Primary)
        self.ventana.resizable(False, False)
        center_window(self.ventana)
        self.tablero = Tablero

        self.title_label = tk.Label(self.ventana, text="** Hill Climbing **", fg=Color_Text, bg=Color_Primary, font=("Game Over", 70))
        self.title_label.pack(pady=(20, 20))
        self.ventana.bind("<Up>", self.on_arrow_up)
        self.ventana.bind("<Down>", self.on_arrow_down)
        self.ventana.bind("<Left>", self.on_arrow_left)
        self.ventana.bind("<Right>", self.on_arrow_right)
    
    
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

                    
                
    def Render(self):
        print("Renderizando")
        # Crear un lienzo (Canvas)
        
        self.canvas = tk.Canvas(self.ventana, width=480, height=480)
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

    def Render_Limits(self):
        print("Renderizando")
        
    def on_arrow_up(self, event):
        print("Arriba")
        self.canvas.delete("all")
        self.canvas.destroy()
        self.Render()

    def on_arrow_down(self, event):
        #Main(self.ventana)
        print("Abajo")

    def on_arrow_left(self, event):
        print("Izquierda")
    
    def on_arrow_right(self, event):
        print("Derecha")

    def run(self):
        self.ventana.mainloop()
        
        
