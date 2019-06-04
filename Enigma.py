from Substitutor import Substitutor


# The enigma class.
class Enigma(Substitutor):

    def __init__(self, rotors, reflector, plugBoard):
        self.rotors = rotors
        self.reflector = reflector
        self.plugBoard = plugBoard

    # This is the function that moves the rotors for each iteration.
    def moveRotors(self):
        if self.rotors[2].IsNotch() or self.rotors[1].IsNotch():
            if self.rotors[1].IsNotch():
                self.rotors[0].advanceOffSet()
            self.rotors[1].advanceOffSet()
        self.rotors[2].advanceOffSet()

    # The function that makes the decryption or the encryption.
    def encryptDecrypt(self, word):
        encrypted = ""
        for letter in word:

            self.moveRotors()

            translatedLetter = self.plugBoard.forwardTrans(letter.upper())

            first = self.rotors[2].encryptedLetter(translatedLetter)
            second = self.rotors[1].encryptedLetter(self.toChar(first))
            third = self.rotors[0].encryptedLetter(self.toChar(second))

            reflected = self.reflector.forwardTrans(self.toChar(third))

            first = self.rotors[0].decryptLetter(reflected)
            second = self.rotors[1].decryptLetter(self.toChar(first))
            third = self.rotors[2].decryptLetter(self.toChar(second))

            translatedLetter = self.plugBoard.forwardTrans(self.toChar(third))

            encrypted += translatedLetter

        return encrypted

    # This function makes a number to char.
    def toChar(self, number):
        return chr(ord('A')+number)

    def forwardTrans(self, permutation):
        pass

    def reverseTrans(self, permutation):
        pass
