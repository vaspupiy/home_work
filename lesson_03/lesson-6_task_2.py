class Road:

    def __init__(self, length,  width):
        self.__length = length
        self.__width = width

    def mass_asp_calc(self, mass_of_meter=25, thick=5):
        return self.__length * self.__width * mass_of_meter * thick * 10 ** -3


r = Road(5000, 20)
print(r.mass_asp_calc())
