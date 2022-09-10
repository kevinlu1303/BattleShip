#!/usr/bin/env python3
'''
Player Class - mostly responsible for holding board and name for display/storage purposes and takes
the user input for next attack
    + name - name of player for display purposes
    + player_board - board of the player which holds all of their ships
add_board - creates board for player once we've recieve size and strategy
get_board - recieve player_board
take_action - takes in user input for next attack coordinates, calls error if they are outside of board
or already hit

ComputerPlayer Class - extends player class, overrides the take_action class

    overrides take_action - randomly generates attack coordiantes, checks if computer has already hit them
'''
from Board import Board
import numpy as np

class Player:
    is_computer = False
    def __init__(self,name):
        self.name = name
        self.player_board = None
    
    def add_board(self, width, height, board_strategy = 'random'):
        self.player_board = Board(width, height, board_strategy)
    
    def get_board(self):
        if self.player_board:
            self.player_board.print_board()
    
    def take_action(self):
        x_coordinate = input('{} please choose a x coordinate to attack:\n'.format(self.name))
        y_coordinate = input('{} please choose a y coordinate to attack:\n'.format(self.name))
        if not x_coordinate.isdigit() or not y_coordinate.isdigit():
            print('Please put integer coordinates.\n')
            return self.take_action()
        coordinates = [int(x_coordinate), int(y_coordinate)]
        if not self.player_board.check_boundaries(coordinates):
            print('Coordinates: {}, do not fit in the board width of {} or board height of {}.\n'.format(coordinates,self.player_board.width,self.player_board.height))
            return self.take_action()
        return coordinates
        

class ComputerPlayer(Player):
    is_computer = True
    def take_action(self):
        return [np.random.randint(1, self.player_board.width + 1),np.random.randint(1, self.player_board.height + 1)]
