from abc import ABCMeta, abstractmethod


# Abstract class Substitutor.
class Substitutor:
    __metaclass__ = ABCMeta

    num_of_letters = 26

    @abstractmethod
    def forwardTrans(self, perm):
        pass

    @abstractmethod
    def reverseTrans(self, perm):
        pass

    # Turn letter to index function.
    def letToInd(self, letter):
        return ord(letter.upper()) - ord('A')

    # The iteration to the left.
    def leftShift(self, letter, numOfShifts):
        return self.rightShift(letter, 26 - numOfShifts)

    # The iteration to the right.
    def rightShift(self, letter, numOfShifts):
        if (numOfShifts < 0):
            return (letter + 26 + numOfShifts) % 26
        return (letter + numOfShifts) % 26
