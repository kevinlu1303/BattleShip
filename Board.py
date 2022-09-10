#!/usr/bin/env python3
from ShipPlacer import ShipPlacer
class Board:
    width = 0
    height = 0 
    def __init__(self, width, height, board_strategy = 'random'):
        self.width = width
        self.height = height
        self.ships = []
        self.occupied_coords = []
        self.hit_coords = []

    def check_boundaries(self,x,y):
        within_boundaries = True
        if x > self.width:
            within_boundaries = False
        if y > self.height:
            within_boundaries = False
        return within_boundaries
    
    def place_ships(self):
        ''' can take a user array of coordinate and rotation'''
        ship_placer = ShipPlacer(self.board_strategy, self)
        ship_placer.place_ships()
        self.ships = ship_placer.get_ships()
        self.occupied_coords = ship_placer.get_occupied_coords()

    def print_board(self):
        row =[]
        for x in range(self.width):
            row = []
            for y in range(self.height):
                if [x,y] in self.hit_coords:
                    row.append('X')
                else:
                    row.append(str(0))
                if y == self.height - 1:
                    print(row)
                