from View.GUI_Principal import JuegoApp
from View.GUI_Modos_Juego import Modos_Juego
from pygame import mixer


mixer.init()

def reproducir_musica():
    mixer.music.load("Sounds/Sound_Menu.mp3")  # Reemplaza "tu_archivo.wav" con la ruta de tu archivo .wav
    mixer.music.play(-1) 
    mixer.music.set_volume(0.1)
    
def detener_musica():
    print("Deteniendo musica")
    mixer.music.stop()

def main():
    reproducir_musica()
    app = JuegoApp()
    app.run()

if __name__ == "__main__":
    main()