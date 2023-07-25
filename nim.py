import game
import players

# Create a game
g = game.Game()

# Create two players
p1 = players.HumanPlayer("Sid")
p2 = players.RandomPlayer()

# Assign the players to the game
g.setPlayers(p1, p2)

# Play the game
while True:
    board = g.next_turn()
    if board==True:
        break
