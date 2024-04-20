# Import the Game class from the game module
from game import Game

# Check if this module is being run directly (not imported as a module in another script)
if __name__ == "__main__":
    # Create an instance of the Game class
    game = Game()
    game.run()