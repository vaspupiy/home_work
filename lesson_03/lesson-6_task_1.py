import time
import turtle


def c_color(color):
    t = turtle.Pen()
    t.color(color)
    t.begin_fill()
    t.circle(100)
    t.end_fill()


class TrafficLight:
    """Класс TrafficLight (светофор)"""

    def __init__(self):
        self.__color = None

    def running(self):
        self.__color = "red"
        print("\033[31m {}" .format(self.__color))
        c_color(self.__color)
        time.sleep(7)
        self.__color = "yellow"
        print("\033[33m {}" .format(self.__color))
        c_color(self.__color)
        time.sleep(2)
        self.__color = "green"
        print("\033[32m {}" .format(self.__color))
        c_color(self.__color)
        time.sleep(7)
        self.__color = "yellow"
        print("\033[33m {}" .format(self.__color))
        c_color(self.__color)
        time.sleep(2)


tr = TrafficLight()
tr.running()
