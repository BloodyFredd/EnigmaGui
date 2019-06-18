from Translator import Translator


# The reflector class.
class Reflector(Translator):

    def __init__(self, perm):
        self.reflector = list(perm)

    # The translation of each letter.
    def forwardTrans(self, letter):

        index = self.letToInd(letter.upper())

        return self.reflector[index]

    # The reverse translation of each letter.
    def reverseTrans(self, letter):
        return self.forwardTrans(letter)

