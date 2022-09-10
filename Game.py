#!/usr/bin/env python3

from operator import is_
import os

from Board import Board
from Player import Player, ComputerPlayer

class Game:
    def __init__(self, player1, player2 = 'Computer', width = 10, height = 10):
        self.player1 = Player(player1)
        if player2 == 'Computer':
            self.player2 = ComputerPlayer(player2)
        else:
            self.player2 = Player(player2)
        self.player1.add_board(width, height)
        self.player2.add_board(width, height)
        self.player1.player_board.place_ships()
        self.player2.player_board.place_ships()
        self.attacking_player = self.player1
        self.defending_player = self.player2
    def game_loop(self):
        is_game_over = False
        while (is_game_over == False):
            coords = self.get_attacking_action()
            print('{} has chosen to attack at {}!\n'.format(self.attacking_player.name,str(coords)))
            if self.defending_player.player_board.check_for_hit(coords):
                print('{} was a hit!\n'.format(str(coords)))
                if self.defending_player.player_board.all_ships_sunk():
                    is_game_over ==True
            else:
                print('{} was a miss!\n'.format(str(coords)))
            self.switch_players()
        return self.defending_player

    def get_attacking_action(self):
        if self.attacking_player.is_computer:
            return self.find_computer_attacking_action()
        print('{} are the coordinates you have hit with'.format(self.defending_player.player_board.hit_coords))
        print('{} are the coordinates you have missed with'.format(self.defending_player.player_board.missed_coords))
        attack_coords = self.attacking_player.take_action() 
        if self.defending_player.player_board.has_been_hit(attack_coords):
            print("You have already hit this area.\n")
            return self.get_attacking_action()
        return attack_coords
        
        
    
    def find_computer_attacking_action(self):
        attack_coords = self.attacking_player.take_action() 
        while self.defending_player.player_board.has_been_hit(self.attacking_player.take_action()):
            attack_coords = self.attacking_player.take_action() 
       
        return attack_coords
    
    def switch_players(self):
        self.attacking_player,self.defending_player = self.defending_player, self.attacking_player

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
       width, height = get_players_width_height()
    os.system('clear')
    print('Board Created\n')

    return width, height
def get_players_width_height():
    width = input("Width (8-40):\n")
    if not width.isdigit():
        print("Please input an integer.\n")
        return get_players_width_height()
    width = int(width)
    if width < 8 or width > 40:
        print("Please keep width between 8 and 40.\n")
        return get_players_width_height()
    height = input("Height (8-40):\n")
    if not height.isdigit():
        print("Please input an integer.\n")
        return get_players_width_height()
    height = int(height)
    if height < 8 or height > 40:
        print("Please keep height between 8 and 40.\n")
        return get_players_width_height()
    return width, height
def get_players():
    player_count = input('How many people are playing, 1 or 2:\n')
    if not player_count.isdigit():
        print("Please input an integer\n")
        return get_players()
  
    player_count = int(player_count) 
    if player_count != 1 and player_count != 2:
        print("Please put 1 or two players.\n")
        return get_players()
    if player_count == 1:
        player_1_name = input('What is the name for the first player:\n')
        player_2_name = 'Computer'
        os.system('clear')
        print('Welcome {}\n'.format(player_1_name))
    else:
        player_1_name = input('What is the name for the first player:\n')
        player_2_name = input('What is the name for the second player:\n')
        os.system('clear')
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
    return game.game_loop()
main()
    