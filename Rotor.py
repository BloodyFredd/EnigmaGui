from Translator import Translator


# The rotor class.
class Rotor(Translator):
    def __init__(self, ringOffset, ringSetting, permutation, notch):
        super(self.__class__, self).__init__(permutation)
        self.ringOffset = ringOffset
        self.ringSetting = ringSetting
        self.notch = notch

    # The function to encrypt each letter.
    def encryptedLetter(self, letter):
        return result

    # The function to decrypt each letter.
    def decryptLetter(self, letter):
        return result

    # If the rotor is at the end and should move.
    def IsNotch(self):
        return self.ringOffset == self.notch

    # Move the offset of the rotor.
    def advanceOffSet(self):
        self.ringOffset = self.rightShift(self.ringOffset, 1)

