import random
print(random.seed(3))


class Assign:
    def __init__(self, value=0):
        self.__value = value


obj1 = Assign(2)
obj2 = Assign(2)
print(id(obj1) == id(obj2), end =' ')
str1 = 'Good'
str2 = 'Good'
print(id(str1) == id(str2))
