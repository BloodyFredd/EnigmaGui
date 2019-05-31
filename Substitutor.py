from abc import ABCMeta, abstractmethod


# Abstract class Substitutor.
class Substitutor:
    __metaclass__ = ABCMeta

    num_of_letters = 26

    @abstractmethod
    def forwardTrans(self, permutation):
        pass

    @abstractmethod
    def reverseTrans(self, permutation):
        pass
