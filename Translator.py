from Substitutor import Substitutor


# The translator class.
class Translator(Substitutor):

    def __init__(self, permutation):
        self.permutation = list(permutation.upper())

    # The translation of each letter
    def forwardTrans(self, letter):
        return self.permutation[self.letToInd(letter)]

    # The reverse translation of each letter.
    def reverseTrans(self, letter):
        return chr(ord('A') + self.permutation.index(letter.upper()))
