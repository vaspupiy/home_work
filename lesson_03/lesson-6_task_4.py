class Car:

    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return 'Машина поехала'

    def stop(self):
        return 'Машина остановилась'

    def turn(self, direction):
        if direction.lower() in ['право', 'лево']:
            return f'Машина повернула на {direction}'
        else:
            return 'Ошибка ввода. direction может принимать значения "право" или "лево"'

    def show_speed(self):
        return self.speed


class TownCar(Car):

    def show_speed(self):
        if self.speed <= 60:
            return self.speed
        else:
            return 'Превышение скорости'


class SportCar(Car):
    pass


class WorkCar(Car):

    def show_speed(self):
        if self.speed <= 40:
            return self.speed
        else:
            return 'Превышение скорости'


class PoliceCar(Car):
    pass


print('\ncar1:')
car1 = Car(40, 'Зеленый', 'Жигули')
print(car1.speed, car1.color, car1.name, car1.is_police)
print(car1.go())
print(car1.show_speed())
print(car1.turn('Право'))
print(car1.turn('Юго-Восток'))
print(car1.turn('Лево'))
print(car1.stop())

print('\ntown_car1:')
town_car1 = TownCar(55, 'Красный', 'Москвич')
print(town_car1.speed, town_car1.color, town_car1.name, town_car1.is_police)
print(town_car1.go(), town_car1.show_speed(), town_car1.turn('Право'), town_car1.stop())
print('\ntown_car2:')
town_car2 = TownCar(65, 'Синий', 'Москвич')
print(town_car2.speed, town_car2.color, town_car2.name, town_car2.is_police)
print(town_car2.go(), town_car2.show_speed(), town_car2.turn('Право'), town_car2.stop())

print('\nsport_car1:')
sport_car1 = SportCar(195, 'Красный', 'Ferrari')
print(sport_car1.speed, sport_car1.color, sport_car1.name, sport_car1.is_police)
print(sport_car1.go(), sport_car1.show_speed(), sport_car1.turn('Право'), sport_car1.stop())
print('\nsport_car2:')
sport_car2 = SportCar(185, 'Белый', 'McLaren')
print(sport_car2.speed, sport_car2.color, sport_car2.name, sport_car2.is_police)
print(sport_car2.go(), sport_car2.show_speed(), sport_car2.turn('Право'), sport_car2.stop())

print('\nwork_car1:')
work_car1 = WorkCar(55, 'Красный', 'Камаз')
print(work_car1.speed, work_car1.color, work_car1.name, work_car1.is_police)
print(work_car1.go(), work_car1.show_speed(), work_car1.turn('Право'), work_car1.stop())
print('\nwork_car2:')
work_car2 = WorkCar(35, 'Синий', 'Зил')
print(work_car2.speed, work_car2.color, work_car2.name, work_car2.is_police)
print(work_car2.go(), work_car2.show_speed(), work_car2.turn('Право'), work_car2.stop())

print('\npolice_car1:')
police_car1 = PoliceCar(95, 'Белый', 'Жигули', True)
print(police_car1.speed, police_car1.color, police_car1.name, police_car1.is_police)
print(police_car1.go(), police_car1.show_speed(), police_car1.turn('Право'), police_car1.stop())
print('\npolice_car2:')
police_car2 = PoliceCar(65, 'Желтый', 'Москвич', True)
print(police_car2.speed, police_car2.color, police_car2.name, police_car2.is_police)
print(police_car2.go(), police_car2.show_speed(), police_car2.turn('Право'), police_car2.stop())
