#!/usr/bin/env python3
''''
Ship class - represents a ship, mostly responsible for holding data and checking if this ship has been sunk

    + name - name of ship corresponding to conventional battleship
    + length - length of said ship
    + coordinates - which coordinates on the board it lies on
    + hit_coords - array that signifies which parts of the ship have been hit thus far, when its all 1's the ship is sunk
    + is_sunk - True if ship is completely sunk, can update gui once implemented

check_for_coords - checks if a coordinate overlaps with the ship
take_hit - updates the hit_coords if the coord lies within the ship
check_if_sunk - sees if all the coords of the ship have been hit, (self.hit_coords == [1,...])
set_coordinates - takes in starting coords, length, and rotation to return all of its internal coordinates
get_coordinates - returns self.coordinates
is_sunk - returns self.is_sunk
'''

class Ship:
    
    def __init__(self, name,length, x,y, rotation):
        self.name = name
        self.length = length
        self.coordinates = self.set_coordinates(x,y,length, rotation)
        self.hit_coords = [0 for i in range(length)]
        self.sunk = False
    def check_for_coords(self, coords):
        if coords in self.coordinates:
            return True
        return False
    def take_hit(self,coords):
        '''
        takes in coordinates and see if they are within the ship, if yes we can take hit
        '''
        for i in range(self.length):
            if self.coordinates[i] == coords:
                self.hit_coords[i] = 1
        if self.check_if_sunk():
            self.sunk = True
    
    def check_if_sunk(self):
        for i in self.hit_coords:
            if i == 0:
                return False
        return True


        
    def set_coordinates(self, x,y,length,rotation):
        coordinates = [[x,y]]
        for i in range(1,length):
            if rotation == 1:
                coordinates.append([x+i,y])
            if rotation == 3:
                coordinates.append([x-i,y])
            if rotation == 0:
                coordinates.append([x,y+i])
            if rotation == 2:
                coordinates.append([x,y-i])
        return coordinates
    def get_coordinates(self):
        return self.coordinates
    def is_sunk(self):
        return self.sunk