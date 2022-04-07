# from abc import ABCMeta, abstractmethod
from abc import ABC, abstractmethod
class shape(ABC):

    @abstractmethod
    def printarea(self):
        return 0



class square(shape):
    type = "square"
    sides = 4

    def __init__(self):
        self.length = 4


    def printarea(self):
        return self.length * self.length

rect1 = square()
print("The area of this square is " , rect1.printarea(),".")


