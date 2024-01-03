# Import your Game class
from phrasehunter.game import Game
# Create your Dunder Main statement.
if __name__ == '__main__':
    game = Game()
    game.start()
    input("Press enter to continue...")
    play_again = input("Do you want to continue? Y/N")
    if play_again.lower() == 'y':
        game.start()
    else:
        print("Thank you for playing the game. Hope you enjoyed it!!!")
# Inside Dunder Main:
## Create an instance of your Game class
## Start your game by calling the instance method that starts the game loop
