# Create your Game class logic in here.
import random
from phrasehunter.phrase import Phrase


class Game:
    # phrases = ['Learning Python', 'Date and Time', 'Instance attributes', 'Class Attributes', 'Init Method']
    phrases = ['app', 'dom']

    def __init__(self):
        self.missed = 0
        self.phrases = Game.phrases
        self.active_phrase = None
        self.guesses = []

    def start(self):
        self.welcome()
        self.active_phrase = self.random_phrase()
        ph = Phrase(self.active_phrase)
        wno_of_attempts = 0
        while (not ph.check_complete(self.guesses)) or wno_of_attempts > 6:
            print('-----------------------------------')
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
                    if ph.check_letter(guess):
                        ph.display(self.guesses)
                    else:
                        wno_of_attempts += 1
                        if wno_of_attempts != 5:
                            print(f'You have {wno_of_attempts} out of 5 lives remaining')
            except ValueError as e:
                print("Invalid Input:", e)

        if ph.check_complete(self.guesses):
            print(f"You guessed it right and the phrase is{self.active_phrase}")
        elif wno_of_attempts < 6:
            print("Sorry you are out of lives. Please try again!!!")
        self.game_over()

    def random_phrase(self):
        return random.choice(self.phrases)

    def welcome(self):
        print("Welcome to Phrase Hunter.Your game will be starting now")

    def get_guess(self, guess):
        self.guesses.append(guess)

    def game_over(self):
        print("Game is over now")


