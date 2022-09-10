#!/usr/bin/env python3


from Board import Board
from Player import Player, ComputerPlayer

class Game:
    def __init__(self, player1, player2 = 'Computer', width = 10, height = 10):
        self.player1 = Player(player1)
        if player2 == 'Computer':
            self.player2 = ComputerPlayer(player2)
        self.player2 = Player(player2)
        self.player1.add_board(width, height)
        self.player2.add_board(width, height)
        

    def print_player_boards(self):
        print('{}\'s board\n'.format(self.player1.name))
        self.player1.get_board()
        print('{}\'s board\n'.format(self.player2.name))
        self.player2.get_board()
        

'''
FUNCTIONS USED TO GET USER INPUT AT START UP
'''
def get_dimensions():
    width = 10
    height = 10
    default_or_custom = int(input('How big should the board be:\n   (0): Default(10x10)\n   (1): Custom\n'))
    if default_or_custom != 0 and default_or_custom != 1:
        print('Please select default or custom.\n')
        get_dimensions()
    if default_or_custom:
        width = int(input("Width (8-40):\n"))
        height = int(input("Height (8-40):\n"))
    print('Board Created\n')

    return width, height

def get_players():
    player_count = input('How many people are playing, 1 or 2:\n')
    if not player_count.isdigit():
        print("Please input an integer\n")
        get_players()
  
    player_count = int(player_count) 
    if player_count != 1 and player_count != 2:
        print("Please put 1 or two players.\n")
        main()
    if player_count == 1:
        player_1_name = input('What is the name for the first player:\n')
        player_2_name = 'Computer'
        print('Welcome {}\n'.format(player_1_name))
    else:
        player_1_name = input('What is the name for the first player:\n')
        player_2_name = input('What is the name for the second player:\n')
        print('Welcome {} and {}\n'.format(player_1_name, player_2_name))
    
    return player_1_name, player_2_name

''' 
GAME LOOP
'''
def main():
    player_1, player_2 = get_players()
    width, height = get_dimensions()
    game = Game(player_1, player_2,width,height)
    game.print_player_boards()
    return 
main()
    