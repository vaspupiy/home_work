from abc import ABC, abstractmethod


class Clothes(ABC):

    @abstractmethod
    def fabric_consumption(self):
        """Определение расхода ткани"""


class Coat(Clothes):

    def __init__(self, v):
        self.v = v

    @property
    def fabric_consumption(self):
        return round(self.v / 6.5 + 0.5, 1)


class Suit(Clothes):

    def __init__(self, h):
        self.h = h

    @property
    def fabric_consumption(self):
        return self.h * 2 + 0.3


cl1 = Coat(25)
cl2 = Suit(3)
cl3 = Suit(8)
cl4 = Coat(30)
print(cl1.v, cl1.fabric_consumption)
print(cl2.h, cl2.fabric_consumption)
print(cl3.h, cl3.fabric_consumption)
print(cl4.v, cl4.fabric_consumption)
print(cl1.fabric_consumption + cl2.fabric_consumption + cl3.fabric_consumption + cl4.fabric_consumption)
