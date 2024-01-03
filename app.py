# Import your Game class
from phrasehunter.game import Game

# Create your Dunder Main statement.
# Inside Dunder Main:
# Create an instance of your Game class
# Start your game by calling the instance method that starts the game loop

if __name__ == '__main__':
    game = Game()
    game.start()
    # Taking user input to decide if game has to be continued or declared as over
    input("Press enter to continue...")
    play_again = input("Do you want to continue? Y/N")
    if play_again.lower() == 'y':
        game.start()
    else:
        game.game_over()
