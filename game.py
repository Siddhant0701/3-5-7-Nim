import numpy as np
import random

class Game:
    def __init__(self, verbose=True) -> None:
        self.board = np.array([3,5,7])
        self.player1 = None
        self.player2 = None
        self.turn = 0
        self.verbose = verbose
    
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
            if self.verbose:
                if self.turn==0:
                    print("Player 1 wins!")
                else:
                    print("Player 2 wins!")
            return True, 1+self.turn
        
        if self.check_lose():
            if self.verbose:
                if self.turn==0:
                    print("Player 2 wins!")
                else:
                    print("Player 1 wins!")
            return True, 2-self.turn

        self.turn = 1 - self.turn
        return False, None

    def update_board(self, move):
        self.board[move[0]] -= move[1]
    
    def check_win(self):
        return np.sum(self.board)==1

    def check_lose(self):
        return np.sum(self.board)==0
    
    def get_state(self):
        return str(self.board[0]) + str(self.board[1]) + str(self.board[2])
    
    def reset(self):
        self.board = np.array([3,5,7])
        self.turn = 0
        self.player1.state_history = []
        self.player2.state_history = []



if __name__ == "__main__":
    import players

    # Create a game
    g = Game()

    # Create two players
    p1 = players.HumanPlayer("Sid", g)
    p2 = players.RandomPlayer(g)

    # Assign the players to the game
    g.setPlayers(p1, p2)

    # Play the game
    while True:
        board = g.next_turn()
        if board==True:
            break