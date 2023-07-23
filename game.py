import numpy as np
import random


class Game:
    def __init__(self) -> None:
        self.board = np.array([3,5,7])
        self.player1 = None
        self.player2 = None
        self.turn = 0
    
    def setPlayers(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def next_turn(self):
        if self.turn==0:
            move = self.player1.move(self.board)
        else:
            move= self.player2.move(self.board)
       
        self.update_board(move)
        if self.check_win():
            if self.turn==0:
                print("Player 1 wins!")
            else:
                print("Player 2 wins!")
            return True
        
        if self.check_lose():
            if self.turn==0:
                print("Player 2 wins!")
            else:
                print("Player 1 wins!")
            return True

        self.turn = 1 - self.turn
        return False

    def update_board(self, move):
        self.board[move[0]] -= move[1]
    
    def check_win(self):
        return np.sum(self.board)==1

    def check_lose(self):
        return np.sum(self.board)==0
