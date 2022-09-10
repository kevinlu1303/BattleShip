#!/usr/bin/env python3
'''
ShipPlacer Class - takes in board and strategy and places default ships onto board

    +strategy - string which lets the class know which placer func to use (only supports random atm)
    +board - the board class that the ships will be placed on
    +ships - list of ships
    +occupied coords - list of coords that are already occupied by a ship

place_ships- Takes the board and calls a placer function to get coordinates and rotations
for a ship to fit so that they dont overlap or break the boundary.

check_if_overlap - takes in a coordinate and rotations for a prospective ship and checks if
these are already occupied on the board

random_placer - takes in the width and height of the board and the length of the ship
and looks for randomly generated coordinates and rotations

get_ships - returns list of ships

get_occupied_cords - returns occupied coords
'''
from Board import Board
from Ship import Ship
import numpy as np

class ShipPlacer:
    names = ['Destroyer', 'Submarine','Cruiser','Battleship', 'Carrier']
    lengths = [2,3,4,4,5]
    def __init__(self, strategy, board, user_input = []):
        self.strategy = strategy
        self.board = board
        self.ships = []
        self.occupied_coords = []

    def place_ships(self):
        width = self.board.width
        height = self.board.height

        for i in range(len(self.lengths)):
            if self.strategy == 'random':
                x,y,rotation = self.random_placer(width, height,self.lengths[i])
                new_ship = Ship(self.names[i],self.lengths[i],x,y,rotation)
                self.ships.append(new_ship)
                self.occupied_coords = self.occupied_coords + new_ship.get_coordinates()

    def check_if_overlap(self, x,y, length, rotation):
        for i in range(1,length):
            if rotation == 1:
                if [x+i,y] in self.occupied_coords:
                    return True
                pass
            if rotation == 3:
                if [x-i,y] in self.occupied_coords:
                    return True
                pass
            if rotation == 0:
                if [x,y+i] in self.occupied_coords:
                    return True
            if rotation == 2:
                if [x,y-i] in self.occupied_coords:
                    return True
        return False
    
    def random_placer(self,width, height, length):
        """ rand_rotation:
                0-up
                1-right
                2-bottom
                3-left
        """
        rand_x = np.random.randint(1,width+1)
        rand_y = np.random.randint(1,height+1)
        while [rand_x, rand_y] in self.occupied_coords:
            rand_x = np.random.randint(1,width + 1)
            rand_y = np.random.randint(1,height + 1)
        rand_rotation = np.random.randint(0,4)
        through_bottom = rand_y - length < 0
        through_top = rand_y + length > height
        through_left = rand_x - length < 0
        through_right = rand_x + length > width
        while True:
            if self.check_if_overlap(rand_x,rand_y, length, rand_rotation):
                        return self.random_placer(width,height,length)
            if rand_rotation == 0:
                if not through_top:
                    return [rand_x, rand_y, rand_rotation]
            if rand_rotation == 1:
                if not through_right:
                    return [rand_x, rand_y, rand_rotation]
            if rand_rotation == 2:
                if not through_bottom:
                    return [rand_x, rand_y, rand_rotation]
            if rand_rotation == 3:
                if not through_left:
                    return [rand_x, rand_y, rand_rotation]
            rand_rotation = np.random.randint(0,4)

    def get_ships(self):
        return self.ships
    
    def get_occupied_coords(self):
        return self.occupied_coords




