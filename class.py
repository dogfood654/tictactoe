# learn class

import random

# structure of game
class tictactoe():
    def __init__(self, player1, player2):
        self.box = [' ', ' ', ' ', 
                    ' ', ' ', ' ', 
                    ' ', ' ', ' ',]
        self.player1 = player1
        self.player2 = player2
        self.player_turn = player1
        
    def show_board(self):
        print(self.box[0] + '|' + self.box[1] + '|' + self.box[2])
        print(self.box[3] + '|' + self.box[4] + '|' + self.box[5])
        print(self.box[6] + '|' + self.box[7] + '|' + self.box[8])

# player in general
class player():
    def __init__(self, nature, shape):
        self.shape = shape
        self.nature = nature

    def get_input(self):
        return self.nature.get_input()

# human player
class human_player():
    def __init__(self):
        self.move = self.get_input()

    def get_input():
        while True:
            try:
                move = int(input("Pick a spot from 1-9: "))
                assert(move <= 9)
                assert(move >= 1)
                break
            except:
                print("Please enter a valid spot.")
        return move

# stupid computer player
class random_ai_player():
    def __init__(self):
        self.move = self.get_input()

    def get_input():
        move = random.randint(1,9)
        return move

# smart computer player
class minimax_ai_player():
    pass

p1 = player(human_player, "X")
p2 = player(random_ai_player, "O")
newgame = tictactoe(p1, p2)
newgame.show_board()

print(newgame.player1.get_input())
print(newgame.player2.get_input())