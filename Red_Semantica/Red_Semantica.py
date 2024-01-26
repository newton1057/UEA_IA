import time
import sys

def simulate_typing(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)  # Ajusta este valor para cambiar la velocidad de escritura
    print()

if __name__ == "__main__":
    text_to_type = "Este es un ejemplo de texto que se está generando."
    simulate_typing(text_to_type)
