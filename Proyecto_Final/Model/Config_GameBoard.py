def Config_GameBoard():
    """
    Configura el tablero de juego llamando a las funciones Extract_GameBoard y Format_GameBoard.

    Returns:
        list: Tablero de juego configurado.
    """
    game_board = []
    game_board = Extract_GameBoard(game_board)
    game_board = Format_GameBoard(game_board)

    return game_board

def Extract_GameBoard(game_board: list):
    """
    Extrae el tablero de juego desde un archivo de configuración y lo guarda en una lista de listas.

    Args:
        game_board (list): Lista vacía donde se guardará el tablero de juego.

    Returns:
        list: Tablero de juego almacenado en una lista de listas.
    """
    with open('./Config/game_board.conf', 'r') as file:
        for line in file:
            row = [c.strip() for c in line.split(',')]
            game_board.append(row)
    return game_board


def Format_GameBoard(game_board: list):
    """
    Formatea el tablero de juego reemplazando las celdas vacías con espacios en blanco.

    Args:
        game_board (list): Tablero de juego en forma de lista de listas.

    Returns:
        list: Tablero de juego formateado.
    """
    for row in range(len(game_board)):
        for column in range(len(game_board[row])):
            if game_board[row][column] == '':
                game_board[row][column] = ' '
    return game_board

def Update_GameBoard(game_board: list):
    with open('./Config/game_board.conf', 'w') as file:
        for row in range(len(game_board)):
            for column in range(len(game_board[row])):
                if column == len(game_board[row]) - 1:  # Evitar poner coma al final de la fila
                    file.write(game_board[row][column])
                else:
                    file.write(game_board[row][column] + ',')
            file.write('\n')
