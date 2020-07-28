class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def get_full_name(self):
        return f'Полное имя сотрудника: {self.name} {self.surname}'

    def get_total_income(self):
        return f'Доход с учетом премии: {self._income["wage"] + self._income["bonus"]} $'


employee = Position("Zigizmund", "Mucusev", "Killer", 25, 27)
employee1 = Position("Avtandill", "Pertahiya", "Dealer", 253, 27)
print()
print(employee.get_full_name())
print(employee.get_total_income())
print()
print(employee1.get_full_name())
print(employee1.get_total_income())

