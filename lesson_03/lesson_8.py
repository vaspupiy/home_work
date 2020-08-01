class MyClass:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    @classmethod
    def set_fio(cls, data):
        name, surname = data
        return cls(name, surname)

    @staticmethod
    def get_fio(self):
        return f'{self.name} {self.surname}'


my_list = ["N", "Hu"]

my_1 = MyClass.set_fio(my_list)
print(my_1.name, my_1.surname)
print(my_1.get_fio(my_1))
