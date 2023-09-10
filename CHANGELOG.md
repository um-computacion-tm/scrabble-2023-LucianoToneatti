# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.0.10] - 2023-09-10

###  Added

Now the "calculate_word_value" function is a method for the "Board" class and your tests are now in "test_board.py".
 
Added to the 'models' file is a 'initial_tiles' function that populates the 'tiles' tile list with an initial set of letters according to the quantities specified in the 'initial_tiles' dictionary.


### Modification

Modified the 'Cell' class constructor to accept optional 'letter' and 'status' arguments, allowing 'Cell' instances to be created with specific letters and statuses.

The 'BigTiles' class was modified by adding and correctly ordering all the letters and their values.


## [0.0.9] - 2023-09-9

###  Added

Added the mechanics of the turns in the main.
Finally added tests for the main.

## [0.0.8] - 2023-09-8

###  Added

Add new function and tests for the "next_turn" method for the "Scrabble" class.
Added a new attribute for the "Scrabble" class called "current_player". This attribute will show who the player is this turn.

## [0.0.7] - 2023-09-7

### Added

Create a new attribute for the "Scrabble" class called "spin". "turn" will count the total turns of the game.
Added 2 new methods for the "Scrabble" class called "playing" and "next_turn". "playing" will only return true in order to end the game and "next turn" will increase the attribute of the turn by 1.
Add the "main" function. This will be the interface of the game and for now it doesn't do many things.


## [0.0.6] - 2023-09-5

### Added

Create a PR and see CircleCI in action.


## [0.0.6] - 2023-08-29

### Added

Create a new folder called "dictionary.py" and a folder called "test_dictionary.py".
For an upcoming commit, define all words and misswords.

## [0.0.5] - 2023-08-29

### Added

This adds new features to the "board" class, validates placed words based on outer cells, and the ability to place tiles on the board.
These additions plus their respective tests were what I did.

## [0.0.4] - 2023-08-29

### Added

I made changes to the "player" folder to improve it and redefine old functions with new ones.
Added the ability to get tiles from the bag, swap tiles, and calculate score based on placed word cells.

## [0.0.3] - 2023-08-29

### Added

Player
He starts his hand with the 7 tiles in the bag. You can also exchange shares for tokens using the exchange method.
Test Players.
When creating a player, check if he has 7 tiles in his hand.
Check that a player's chip exchange does not change their hand or the number of chips in their bag.
BagTiles now wraps all tiles with the correct value.
I also added in "models" all the tetras with their corresponding values.

## [0.0.2] - 2023-08-28

### Added
    
In a folder named "cell.py" define the class "Cell", which represents a cell on the game board. The cell can contain a letter and has attributes to store the type and value of the multiplier. Also, it has methods to add letters to the cell and calculate the total value of the cell.

I create the "board.py" folder and inside it I made the "board" class. It also creates an array to form the board (represented by instances of the "Cell" class)

Create the class and define the "Player" class in a folder named "player.py", which represents a player in the game. The class has attribute tiles that store the letters available to the player.

Define a class called "ScrabbleGame" in the "scrabble.py" folderr. This represents the game in its entirety. The class contains attributes for the board, the bag of letters, and a list of players.  

Create the correspond tests.

## [0.0.1] - 2023-08-28

### Added

Create the classes "Tile" and "BagTiles".

Inside the "Tile" class we define the variables "letter" and "value".

Inside the "BagTiles" class and give each letter a value.

Create methods "take" and "put" in the class "BagTiles" and create the correspond tests.





 
