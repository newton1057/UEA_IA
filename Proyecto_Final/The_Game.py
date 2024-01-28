from View.GUI_Principal import JuegoApp
from pygame import mixer

mixer.init()

# Reproduce la música de fondo del juego.
def play_music():
    mixer.music.load("Sounds/Sound_Menu.mp3")
    mixer.music.play(-1) 
    mixer.music.set_volume(0.2)

# Detiene la reproducción de la música de fondo del juego.    
def detener_musica():
    mixer.music.stop()

# Función principal del juego.
def main():
    # Reproduce la música de fondo, crea una instancia de la clase JuegoApp y la ejecuta.
    play_music()
    app = JuegoApp()
    app.run()

if __name__ == "__main__":
    main()