#!/usr/bin/env python3

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
        return [np.random.randint(0, self.player_board.width),np.random.randint(0, self.player_board.height)]
