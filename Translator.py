from Substitutor import Substitutor


# The translator class.
class Translator(Substitutor):

    def __init__(self, perm):
        self.perm = list(perm.upper())

    # The translation of each letter
    def forwardTrans(self, letter):
        return self.perm[self.letToInd(letter)]

    # The reverse translation of each letter.
    def reverseTrans(self, letter):
        return chr(ord('A') + self.perm.index(letter.upper()))
