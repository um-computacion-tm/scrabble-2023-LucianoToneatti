# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.2.8] - 2023-10-19

### Added

Added a new method for the "Board" class called "presentation_board" which will show the board to the player and "generate_row_string" which helps him.
New methods for the "Several" class.

## [0.2.7] - 2023-10-18

### Added

A new file and its class called "Several" has been added. In this class, everything that is not highly complementary to your previous classes is included.

### Change

Move 8 methods from the "board" class to the "Several" class and its tests.

## [0.2.6] - 2023-10-17

### Added

I moved the 'def string_to_tiles' from scrabble.py to board.py (along with its test) because I believe it's more organized this way. I also created a set of letters, 'letter_set,' to improve letter lookup instead of iterating through all the tiles in the bag.
I will soon add more tests for these new functions.

## [0.2.5] - 2023-10-11

### Fixed

All I did was fix a duplication issue in the board tests.

## [0.2.4] - 2023-10-10

### Added

A new method called "insert" was implemented in the Board class, which takes three arguments, 'word', 'location' and 'orientation' and allows you to place a word on the game board.

## [0.2.3] - 2023-10-08

### Added

In this commit, a new method called scrabble_word_calculate_score has been added to the Scrabble class. This method allows you to calculate the score of a word in the Scrabble game, considering the values ​​of the letters and the multipliers of the squares on the board. (X3 multipliers do not work yet).

I'm trying to create a test to cover "def scrabble string_to_table" but I still can't get it to cover it correctly.

## [0.2.2] - 2023-10-07

### Added

In this commit, a new method has been added to convert a text string into a Scrabble tile list. This method has the ability to handle special letters such as 'CH,' 'LL,' and 'Ñ,' assigning them their corresponding values according to the game rules.This simplifies the conversion of words containing these special letters into playable Scrabble tiles.

## [0.2.1] - 2023-10-04

### Added

Added two methods to the Scrabble class:
Scrabble_validate_word – This method validates whether a word can be placed on the board in a specific location and orientation.
Scrabble_string_to_tiles - This method takes an input string and converts it to a list of Scrabble tiles, using a set of tiles available in the game's tile pool.

And create the tests for both methods.

## [0.2.0] - 2023-10-03

### Added

Added a method named "contains" to the "Player" class to check if a player has the necessary tiles to form a set of tiles.
It also verifies whether the player has access to the tile bag and whether the tiles are available.
This version provides a crucial functionality for verifying tile availability and is essential for the game.

###Change

When adding this new method, I decided to comment out these "get_tiles" and "exchange_tiles" methods for the time being.

## [0.1.9] - 2023-10-02

###  Added

Added a new method for the "Board" class called "put_multipliers".
And also the board itself with its cell multipliers in their corresponding places.

## [0.1.8] - 2023-09-27

###  Added

Two new methods have been implemented in the "Dictionary" class, which are "accents" which is used to remove accents from words and "verify_word" which checks if a word is in the "dictionary.txt" file and checks if it exists.

## [0.1.7] - 2023-09-26

###  Added

Add a new method in the "Board" class called "check_contions" and it is used to resolve errors in the duplication of some code.

### Change

Edit the "word_in_the_center" method.
I eliminated a couple of methods because more than helping, they got in the way and caused problems.
Fix code duplication issues, one in the "validate_word_horizontal" and "validate_word_vertical" method and the other in "word_in_the_center".

## [0.1.6] - 2023-09-25

###  Added

In the 'Board' class, I added several new methods: "word_in_the_center_horizontal," "word_in_the_center_vertical," "compare_tiles_and_letters," and "check_right_letters," each with its own tests. 
These are used for refactoring purposes and will be used for other things in the near future. 

###Change

Additionally, I reduced the complexity of some methods and eliminated duplications.

## [0.1.5] - 2023-09-24

###  Added

Finish the "validate_word_place_board" method.
Create new methods for the class "Board", "word_in_the_center", "validate_word_horizontal" and "validate_word_vertical".
"word_in_the_center" will check if the player's word will be in the center.
"validate_word_horizontal" will check if the player's word will use the other player's tile horizontally.
"validate_word_vertical" will check if the player's word will use the other player's word vertically.

## [0.1.4] - 2023-09-22

###  Added
In the "Board" file.
I implemented a new method called 'validate_word_place_board' in the 'Board' class. The idea behind this method is to check if it is possible to place a tile on the board. Additionally, new tests for this method will be added in the future.

###Change

Fixing bugs and problems.
I was fighting with the code and its test of several files to increase coverage.

## [0.1.3] - 2023-09-20

###  Added

Create a new method for the "Board" class called "is_empty", what it does is see if the board is empty.
I also created this method "validate_word_inside_board" which helps determine if a word fits properly inside the board without going out of bounds based on its location and orientation.

### Change

I changed the board tests because their level of complexity was very high and difficult to understand.

## [0.1.2] - 2023-09-12

###  Added

Work on 'main' and 'test_main' file.
The is_valid_player_count function has been replaced by the valid_player_count method to check the validity of the number of players. Logic and error handling were simplified.
Changed the entry prompt message from "Number of players:" to "Number of participants is:".
Removed unnecessary while True loop in get_player_count.
These changes improve the clarity and structure of the code compared to the previous version.

## [0.1.1] - 2023-09-11

###  Added

Work on 'models' and 'test_models' file.
Fixed a bug in the 'put' method that caused duplicate tokens to be added to the bag.
Adjusted the expected value in the 'test_put' test to reflect the fix of the 'put' method.

### Modification

Rearrange the code in the '__init__' method of the 'BigTiles' class to avoid duplicate calls to 'random.shuffle'.

## [0.1.0] - 2023-09-10

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





 
