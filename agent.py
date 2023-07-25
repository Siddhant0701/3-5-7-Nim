import players
import numpy as np


class RLAgent(players.Player):
    def __init__(self, name, game, exp_rate, lr, policy={}, decay_gamma=0.9, explore_decay=1, train=False):
        super().__init__(name, game)
        self.train = train

        self.state_history = []

        self.policy = {}
        self.lr = lr
        self.decay_gamma = decay_gamma
        self.exp_rate = exp_rate
        self.explore_decay = explore_decay
    
    def move(self, board):
        #Print the board
        if self.game.verbose:
            print("Game state: ", board)

        self.state_history.append(self.get_state())

        move = self.get_move(board)

        if self.game.verbose:
            print(f'Player {self.name} removes {move[1]} lines from row {move[0]}')

        return move
    
    def get_move(self, board):
        # Actual Play
        if not self.train:        
            possible_moves = self.get_possible_moves(board)

            value = 0
            best_move = possible_moves[0]

            for move in possible_moves:
                next_state = self.next_state(board, move)
                if next_state in self.policy:
                    if self.policy[next_state] > value:
                        value = self.policy[next_state]
                        best_move = move
            
            return best_move
        
        # Training
        else:
            possible_moves = self.get_possible_moves(board)
            if np.random.uniform(0,1) <= self.exp_rate:
                self.exp_rate *= self.explore_decay
                return possible_moves[np.random.choice(len(possible_moves))]
            else:
                value = 0
                best_move = possible_moves[0]
                for move in possible_moves:
                    next_state = self.next_state(board, move)
                    if next_state in self.policy:
                        if self.policy[next_state] > value:
                            value = self.policy[next_state]
                            best_move = move
                self.exp_rate *= self.explore_decay
                return best_move

    def get_possible_moves(self, board):
        possible_moves = []
        for row in range(len(board)):
            for lines in range(1, board[row]+1):
                possible_moves.append([row, lines])
        return possible_moves
    
    
    def next_state(self, board, move):
        new_board = board.copy()
        new_board[move[0]] -= move[1]
        return str(new_board[0]) + str(new_board[1]) + str(new_board[2])
    
    def update_policy(self, reward):
        for state in reversed(self.state_history):
            if state not in self.policy:
                self.policy[state] = 0
            self.policy[state] += self.lr * (self.decay_gamma * reward - self.policy[state])
            reward = self.policy[state]