#!/usr/bin/env python3

from turtle import Turtle


class Board:
    width = 0
    height = 0 
    def __init__(self, width, height, board_strategy = 'random'):
        self.width = width
        self.height = height
        self.ships = []
        self.occupied_coords = []
        self.hit_coords = []
        self.missed_coords = []
        self.board_strategy = board_strategy

    def check_boundaries(self,coords):
        x,y = coords[0],coords[1]
        within_boundaries = True
        if x > self.width:
            within_boundaries = False
        if y > self.height:
            within_boundaries = False
        return within_boundaries

    def check_for_hit(self, coords):
        '''
        returns true if a ship took a hit, false if not
        updates the hit_coords, occupied_coords, and updates ships
        '''
        if coords in self.occupied_coords:
            self.hit_coords.append(coords)
            for ship in self.ships:
                if ship.check_for_coords(coords):
                    ship.take_hit(coords)
                    if ship.is_sunk():
                        print('{} has been sunk!\n'.format(ship.name))
                    return True
        else:
            self.missed_coords.append(coords)
            return False
    def has_been_hit(self, coords):
        '''
        checks if the attacking player has already hit these coords
        called by game_loop of Game class in game.py
        '''
        if coords in self.hit_coords or coords in self.missed_coords:
            return True
        return False
    def all_ships_sunk(self):
        for ship in self.ships:
            if not ship.is_sunk:
                return False
        return True
    
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
                
from ShipPlacer import ShipPlacer