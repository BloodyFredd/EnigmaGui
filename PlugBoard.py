from Translator import Translator


# The plugboard class.
class PlugBoard(Translator):

    def __init__(self, config):
        self.config = config.strip().split()
        self.configDict = {}

        # Pair the plugboard letters.
        for pair in self.config:
            self.configDict[pair[0]] = pair[1]
            self.configDict[pair[1]] = pair[0]

    # The translation of the letter in the plug.
    def forwardTrans(self, letter):
        if letter in self.configDict:
                return self.configDict[letter]

        return letter.upper()

    # The reverse translation of the letter in the plug.
    def reverseTrans(self, letter):
        pass

