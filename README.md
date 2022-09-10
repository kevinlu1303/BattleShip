_______________________________
BattleShip
_______________________________

Play against a computer or against a friend from your terminal.
Takes in number of players, player names, board size, and the game 
automatically generates your ship.

Begin playing with: PY Game.py

_______________________________
SPECS
_______________________________

Game.py - 

Takes in user input to get the number of players and creates the player classes, also takes in board size and generates a board and randomly
places ships. Also has the Game class which supports the game logic with the game loop, game end, and turn based attack features.

Player.py - 

Holds the player class which has the instance variables for the players name and player board object. Responsible for calling user input for which coordinates to attack
and calling the method to create the board. This also Holds the computer player class which extends the player class, overriding the take_action function since it
does not rely on user input

Ship.py -

Holds the ship class which contains the name of the ship and the length to distinguish different types of ships (Destroyer, Submarine, etc..). Also holds the ships own 
internal coordinates and hit coordinates in order to evaluate if the ship has been sunk.  Once all ships.is_sunk are true we know the game is over for a players board.

Board.py -

Holds the Board class which is an abstract representation of the grid. Mostly contains an array of ships, coordinates occupied by ships, coordiantes with ships that have been hit,
and coordinates that have been hit without ships. These will mostly be used in the future when I can make a quick tkinter gui. Beyond that, the instance methods
of a board holds the ships and takes in coordinates to see if one of the board's ships have been hit, and update instance variables accordingly. Also has functions
to check if a coordinate has already been hit for input checking.

ShipPlacer.py -

Holds the ShipPlacer class which is responsible for the strategy in which ships are placed onto the board. Currently only supports the random strategy which 
randomly chooses starting coordinates and rotations, making sure there are no overlaps or boundary violations. Hope to extend into different ShipPlacer classes
with some using random placement, clustered placement, or user inputted placement.

Tests.py -

Unit and functional tests for each class.
