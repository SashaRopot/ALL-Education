import string


class Alphabet:
    def __init__(self, lang, letter):
        self.lang = lang
        self.letter = list(letter)

    def print(self):
        print(self.letter)

    def letters_num(self):
        len(self.letter)


class EngAlphabet(Alphabet):

    __letters_num = 26

    def __init__(self):
        super().__init__('En', string.ascii_uppercase)

    def eng_letter(self, letter):
        if letter.upper() in self.letter:
            return True
        return False

    def letters_num(self):
        return EngAlphabet.__letters_num

    @staticmethod
    def example():
        print('English text:\nI really want to study and change jobs.')


if __name__ == '__main__':
    eng_alphabet = EngAlphabet()
    eng_alphabet.print()
    print(eng_alphabet.letters_num())
    print(eng_alphabet.eng_letter('F'))
    print(eng_alphabet.eng_letter('Щ'))
    EngAlphabet.example()
