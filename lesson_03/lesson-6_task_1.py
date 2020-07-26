import time


class TrafficLight:
    """Класс TrafficLight (светофор)"""

    def __init__(self):
        self.__color = None

    def running(self):
        self.__color = "red"
        print(self.__color)
        time.sleep(7)
        self.__color = "yellow"
        print(self.__color)
        time.sleep(2)
        self.__color = "green"
        print(self.__color)
        time.sleep(11)


tr = TrafficLight()
tr.running()
