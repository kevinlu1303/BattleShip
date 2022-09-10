#!/usr/bin/env python3

from Board import Board

class Player:
    def __init__(self,name):
        self.name = name
        self.player_board = None
    
    def add_board(self, width, height, board_strategy = 'random'):
        self.player_board = Board(width, height, board_strategy)
    
    def get_board(self):
        if self.player_board:
            self.player_board.print_board()

class ComputerPlayer(Player):
    def take_action(self):
        pass
