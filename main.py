# Import the Game class from the game module
from game import Game

# Check if this module is being run directly (not imported as a module in another script)
if _name_ == "_main_":
    # Create an instance of the Game class
    game = Game()

    # Call the run method of the Game instance to start the game