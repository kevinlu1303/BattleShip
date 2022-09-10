#!/usr/bin/env python
from Ship import Ship
from Board import Board 
from ShipPlacer import ShipPlacer
def test_ship():
    smallship = Ship('skooner',4,2,3, 1)
    print(smallship.coordinates)
    assert smallship.coordinates == [[2,3],[3,3],[4,3],[5,3]], "does not match, got: {}".format(smallship.coordinates)
    print('passed')

def test_ship_placer():
    board = Board(10,10)
    board.place_ships()
    print([ship.get_coordinates() for ship in board.ships])
test_ship()
test_ship_placer()