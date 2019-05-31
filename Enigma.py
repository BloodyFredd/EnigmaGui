from Substitutor import Substitutor


# The enigma class.
class Enigma(Substitutor):

    def __init__(self, rotors, reflector, plugBoard):
        self.rotors = rotors
        self.reflector = reflector
        self.plugBoard = plugBoard

    # This is the function that moves the rotors for each iteration.
    def moveRotors(self):

    # The function that makes the decryption or the encryption.
    def encryptDecrypt(self, word):
        encrypted = ""
        for letter in word:

            self.moveRotors()

        return encrypted

    # This function makes a number to char.
    def toChar(self, number):
        return chr(ord('A')+number)

    def forwardTrans(self, permutation):
        pass

    def reverseTrans(self, permutation):
        pass
