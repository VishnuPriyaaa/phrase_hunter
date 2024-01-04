# Create your Game class logic in here.
import random
from phrasehunter.phrase import Phrase

"""
class which contains the methods used to start and stop the game
"""


class Game:
    phrases = ['Learning Python', 'Date and Time', 'Instance attributes', 'Class Attributes', 'Init Method']

    """
    Init method to initialize all the attributes of Game class using it's object
    """
    def __init__(self):
        self.missed = 0
        self.phrases = Game.phrases
        self.active_phrase = None
        self.guesses = []

    """
    Start method which contains all the logic to proceed with the game
    """

    def start(self):
        self.welcome()
        self.active_phrase = self.random_phrase()
        self.guesses = []
        ph = Phrase(self.active_phrase)
        while (not ph.check_complete(self.guesses)) or self.missed > 6:
            ph.display(self.guesses)
            try:
                guess = input('Guess a letter: ')
                if not guess.isalpha():
                    raise ValueError('Please enter only alphabets as input')
                if len(guess) > 1:
                    raise ValueError('Please enter only one character at a time')
                if guess in self.guesses:
                    print('This letter is already taken. Please try with another letter')
                    continue
                else:
                    self.guesses.append(guess)
                    if not ph.check_letter(guess):
                        self.missed += 1
                        if self.missed != 5:
                            print(f'You have {5 - self.missed} out of 5 lives remaining')
                        else:
                            break
            except ValueError as e:
                print("Invalid Input:", e)

        if ph.check_complete(self.guesses):
            print(f"You guessed it right and the phrase is {self.active_phrase}")
        elif self.missed < 6:
            print("Sorry you are out of lives. Please try again!!!")

    """
    random_phrase method generates a random phrase from given list of phrases for each new game
    """

    def random_phrase(self):
        return random.choice(self.phrases)

    """
    welcome method displays the welcome message to start the game
    """

    def welcome(self):
        print("Welcome to Phrase Hunter.Your game will be starting now")

    """
    get_guess method is used to add all the characters user have guessed into a list
    """
    def get_guess(self, guess):
        self.guesses.append(guess)

    """
    game_over is called at the end of the game to determine that the current game is complete
    """
    def game_over(self):
        print("Thank you for playing the game. Hope you enjoyed it!!!")


