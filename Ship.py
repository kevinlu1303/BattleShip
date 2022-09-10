#!/usr/bin/env python3

class Ship:
    
    def __init__(self, name,length, x,y, rotation):
        self.name = name
        self.length = length
        self.coordinates = self.set_coordinates(x,y,length, rotation)
        self.rotation = rotation
        self.hit_coords = [0 for i in range(length)]
        self.sunk = False
    def check_coords(self,x,y):
        '''
        takes in coordinates and see if they are within the ship, if yes we can take hit
        '''
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