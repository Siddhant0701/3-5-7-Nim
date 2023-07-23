import numpy as np
import random

class Player:
    def __init__(self, name) -> None:
        self.name = name
    
    def move(self, board):
        #Print the board
        print("Game state: ", board)

        move = self.get_move(board)
        print(f'Player {self.name} removes {move[1]} lines from row {move[0]}')

        return move

    def get_move(self, board):
        pass


class HumanPlayer(Player):
    def __init__(self, name) -> None:
        super().__init__(name)

    def get_move(self, board):
        row = int(input("Enter row: "))
        lines = int(input("Enter number of lines to remove: "))
        return np.array([row, lines])
    

class RandomPlayer(Player):
    def __init__(self) -> None:
        super().__init__("Random")

    def get_move(self, board):
        row = random.randint(0, len(board)-1)
        lines = random.randint(1, board[row])
        return np.array([row, lines])