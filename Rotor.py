from Translator import Translator


# The rotor class.
class Rotor(Translator):
    def __init__(self, ringOffset, ringSetting, perm, notch):
        super(self.__class__, self).__init__(perm)
        self.ringOffset = ringOffset
        self.ringSetting = ringSetting
        self.notch = notch

    # If the rotor is at the end and should move.
    def IsNotch(self):
        return self.ringOffset == self.notch

    # Move the offset of the rotor.
    def advanceOffSet(self):
        self.ringOffset = self.rightShift(self.ringOffset, 1)

    # The function to encrypt each letter.
    def encryptedLetter(self, letter):
        # Right shift letter.
        rightShifted = self.rightShift(self.letToInd(letter), self.ringOffset - 1)

        # Left shift letter.
        leftShifted = self.leftShift(rightShifted, self.ringSetting - 1)

        # Translate the letter.
        translated = self.forwardTrans(chr(ord('A') + leftShifted))

        # Right shift again.
        result = self.rightShift(self.letToInd(translated), self.ringSetting - 1 - (self.ringOffset - 1))

        return result

    # The function to decrypt each letter.
    def decryptLetter(self, letter):
        # Right shift letter.
        rightShifted = self.rightShift(self.letToInd(letter), self.ringOffset - 1)

        # Left shift letter.
        leftShifted = self.leftShift(rightShifted, self.ringSetting - 1)

        # Reverse translate the letter.
        translated = self.reverseTrans(chr(ord('A') + leftShifted))

        # Right shift again.
        result = self.rightShift(self.letToInd(translated), self.ringSetting - 1 - (self.ringOffset - 1))

        return result        