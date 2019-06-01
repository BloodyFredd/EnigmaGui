from Translator import Translator


# The plugboard class.
class PlugBoard(Translator):

    def __init__(self, configuration):
        self.configuration = configuration.strip().split()
        self.configurationDict = {}

        for pair in self.configuration:
            self.configurationDict[pair[0]] = pair[1]
            self.configurationDict[pair[1]] = pair[0]

    # The translation of the letter in the plug.
    def forwardTrans(self, letter):
        return letter.upper()

    def reverseTrans(self, letter):
        pass

