import numpy as np
import random

class Player:
    def __init__(self, name, game) -> None:
        self.name = name
        self.game = game
    
    def move(self, board):
        #Print the board
        if self.game.verbose:
            print("Game state: ", board)

        move = self.get_move(board)
    
        if self.game.verbose:
            print(f'Player {self.name} removes {move[1]} lines from row {move[0]}')

        return move

    def get_move(self, board):
        pass

    def get_state(self):
        return self.game.get_state()

class HumanPlayer(Player):
    def __init__(self, name, game) -> None:
        super().__init__(name, game)

    def get_move(self, board):
        row = int(input("Enter row: "))
        lines = int(input("Enter number of lines to remove: "))
        return np.array([row, lines])
    

class RandomPlayer(Player):
    def __init__(self, game) -> None:
        super().__init__("Random", game)

    def get_move(self, board):
        row = random.randint(0, len(board)-1)
        lines = random.randint(1, board[row])
        return np.array([row, lines])