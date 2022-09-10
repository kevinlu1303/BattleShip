#!/usr/bin/env python3
'''
Game Class - responsible for holding the player objects, and instantiating them with their board and ships
also responsible for the game loop and the turn based logic 

    +player1 - whichever player wrote their name first
    +player2 - whichever player wrote their name last or computer if singleplayer
    +attacking_player - intially player1, switches each turn
    +defending_player - initially player2, switches each turn

game_loop - generates a while loop that gets the attacking players action, checks if it was a hit, then switches players
at the end of each loop, if there was a hit, checks to see if that ship has sunk or if all ships have sunk, therefore a win
get_attacking_action - calls the take_action method of the attacking player's class. checks for a hit or miss
find_computer_attacking_action - similar to get_attacking_action. displays slightly differently
switch_players - simply switches who is attacking and who is defending
print_players_board - prints the board of both players to check for hits.

_____________
Funcs
_____________
get_dimensions - asks user if they would like to use default size map or custom
get_player_width_height - gets user input on the width and height of custom map
get_players - get number of players and their name
main - gets user input then instantiates the game class and begins the game

'''
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
            os.system('clear')
            coords = self.get_attacking_action()
            os.system('clear')
            print('\n{} has chosen to attack at {}!\n'.format(self.attacking_player.name,str(coords)))
            if self.defending_player.player_board.check_for_hit(coords):
                print('{} was a hit!\n'.format(str(coords)))
                input('Press enter to continue...')
                if self.defending_player.player_board.all_ships_sunk():
                    is_game_over ==True
            else:
                print('{} was a miss!\n'.format(str(coords)))
                input('Press enter to continue...')
            if self.defending_player.player_board.all_ships_sunk():
                return self.attacking_player
            if self.attacking_player.player_board.all_ships_sunk():
                return self.defending_player
            self.switch_players()
        return self.defending_player

    def get_attacking_action(self):
        if self.attacking_player.is_computer:
            return self.find_computer_attacking_action()
        print('{} are the coordinates you have hit with.\n'.format(self.defending_player.player_board.hit_coords))
        print('{} are the coordinates you have missed with.\n'.format(self.defending_player.player_board.missed_coords))
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
        input('Press enter to continue...')

    

        

'''
FUNCTIONS USED TO GET USER INPUT AT START UP
'''
def get_dimensions():
    '''
    Lets the user choose between the default 10 x 10 rectangular map or custom size for shorter or longer games
    '''
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
    '''
    If user chooses custom canvas size, this function will take
    their input for width and height
    '''
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
    '''
    takes user input to find no. of players, single player
    against computer or two players, also takes their names
    '''
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
Take user input and then start game loop
'''
def main():
    player_1, player_2 = get_players()
    width, height = get_dimensions()
    game = Game(player_1, player_2,width,height)
    game.print_player_boards()
    winning_player = game.game_loop()
    os.system('clear')
    print("{} is the Winning Player!".format(winning_player.name))
    print("{} is the Winning Player!".format(winning_player.name))
    print("{} is the Winning Player!".format(winning_player.name))
    print("{} is the Winning Player!".format(winning_player.name))
    print("{} is the Winning Player!".format(winning_player.name))
    continue_game = input('Continue?\n Press 0 to end.\n Press 1 to continue')
    if continue_game:
        main()
    else:
        print("Thank You For Playing")
main()
    