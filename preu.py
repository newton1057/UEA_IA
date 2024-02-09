import logging

def Motion_Right(self, x, y):
    if self.Game_Board[y][x+1] == " ":
        logging.info('Se ha movido el robot hacia la derecha.')
        self.Game_Board[y][x] = " "
        self.Game_Board[y][x+1] = "R"
        
        # Inicializamos la evaluación con un valor base de -3
        Evaluacion = -3
        
        # Si la posición objetivo en el eje X es mayor que la posición actual del robot,
        # se suma 1 a la evaluación
        if self.Objetive_X > x:
            Evaluacion += 1
        
        # Si la posición objetivo en el eje Y es mayor que la posición actual del robot,
        # se suma 1 a la evaluación
        if self.Objetive_Y > y:
            Evaluacion += 1

        # Se retorna True para indicar que el movimiento fue exitoso y la evaluación resultante
        # dando un plus si el objetivo está hacia la derecha
        if self.Objetive_X == x + 1:
            Evaluacion += 2

        return True, Evaluacion
    else:
        # En caso de que el movimiento no sea posible, se retorna False y una evaluación de 0
        return False, 0
