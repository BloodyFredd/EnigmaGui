from Translator import Translator


# The reflector class.
class Reflector(Translator):

    def __init__(self, permutation):
        self.reflector = list(permutation)

    # The translation of each letter.
    def forwardTrans(self, letter):
        return letter

    # The reverse translation of each letter.
    def reverseTrans(self, letter):
        return self.forwardTrans(letter)

