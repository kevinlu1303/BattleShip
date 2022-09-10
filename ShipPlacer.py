#!/usr/bin/env python3
'''
Can have a random strategy tha
'''
from Board import Board
from Ship import Ship
import numpy as np

class ShipPlacer:
    names = ['Destroyer', 'Submarine','Cruiser','Battleship', 'Carrier']
    lengths = [2,3,4,4,5]
    def __init__(self, strategy, board):
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
        rand_x = np.random.randint(0,width)
        rand_y = np.random.randint(0,height)
        while [rand_x, rand_y] in self.occupied_coords:
            rand_x = np.random.randint(0,width)
            rand_y = np.random.randint(0,height)
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




