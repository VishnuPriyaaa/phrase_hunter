# Create your Phrase class logic here.
class Phrase:

    """
    Init method to initialize all the attributes of Phrase class using object
    """
    def __init__(self, phrase):
        self.phrase = phrase

    """
    Display method is used to display the phrase in a masked form revealing the guessed letters
    """
    def display(self, guessed_letters):
        displayed_phrase = ''
        for char in self.phrase:
            if char.lower() in guessed_letters:
                displayed_phrase += char
            elif char == ' ':
                displayed_phrase += ' '
            else:
                displayed_phrase += '_'
        print(displayed_phrase)

    """
    check_letter method is used to check if the guessed letter is present in the phrase
    """
    def check_letter(self, guessed_letter):
        for char in self.phrase:
            if char.lower() == guessed_letter:
                return True
        return False

    """
    check_complete method is used to check if the user has guessed all the letters from the phrase
    """
    def check_complete(self, guessed_letters):
        if len(guessed_letters) < 1:
            return False
        else:
            for char in self.phrase:
                if char.lower() not in guessed_letters and char != ' ':
                    return False
        return True
