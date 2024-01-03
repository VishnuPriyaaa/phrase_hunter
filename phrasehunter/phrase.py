# Create your Phrase class logic here.
class Phrase:
    def __init__(self, phrase):
        self.phrase = phrase

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

    def check_letter(self, guessed_letter):
        for char in self.phrase:
            if char.lower() == guessed_letter:
                return True
        return False

    def check_complete(self, guessed_letters):
        if len(guessed_letters) < 1:
            return False
        else:
            for char in self.phrase:
                if char.lower() not in guessed_letters:
                    return False
        return True
