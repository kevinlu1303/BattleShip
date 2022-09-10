#!/usr/bin/env python3
'''
Board Class -   Holds the Board class which is an abstract representation of the grid. Mostly contains an array of ships, coordinates occupied by ships, coordiantes with ships that have been hit,
and coordinates that have been hit without ships.

    +width - width of board (coordinates [1-width])
    +height - height of board (coordinates [1-height])
    +ships - list of ship objects corresponding to this players board
    +occupied_coords - coords on the board that have been filled
    +hit_coords - coords which have been hit with a ship
    +missed_coords - coords which have been hit with no ship
    +board_strategy - how to place ships on the board (only supports random atm)

    check_boundaries: checks to see a coord lies within the boundaries [[1 - width],[1 - height]]
    check_for_hit: takes in coords, see if it will strike a ship. if it does update hit_coords and the ship
    otherwise place in missed_coords. returns a bool 
    has_been_hit: checks if a coord has already been played
    all_ships_sunk: condition to see if game is over for this player, iterates through ships and sees if all have been sunk
    place_ships: instantiates the ShipPlacer class with the board specific strategy
    print_board: prints the player board
'''

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
        self.actualboard = [['.' for i in range(width)] for i in range(height)]

    def check_boundaries(self,coords):
        x,y = coords[0],coords[1]
        within_boundaries = True
        if x > self.width or x < 1:
            within_boundaries = False
        if y > self.height or y < 1:
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
                    self.actualboard[coords[1]][coords[0]] == 'X'
                    if ship.is_sunk():
                        print('{} has been sunk!\n'.format(ship.name))
                    return True
        else:
            self.missed_coords.append(coords)
            self.actualboard[coords[1]][coords[0]] == 'O'
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
            if not ship.is_sunk():
                return False
        return True
    
    def place_ships(self):
        ''' can take a user array of coordinate and rotation'''
        ship_placer = ShipPlacer(self.board_strategy, self)
        ship_placer.place_ships()
        self.ships = ship_placer.get_ships()
        self.occupied_coords = ship_placer.get_occupied_coords()

    def print_board(self):
        """
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
            """
        for y in range(len(self.actualboard)):
            print(str(self.actualboard[y]))
                

'''
Leave here due to cylical import
'''
from ShipPlacer import ShipPlacer