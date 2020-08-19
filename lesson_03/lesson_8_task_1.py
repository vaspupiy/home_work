import datetime


class Date:

    def __init__(self, user_sting):
        if Date.valid(self.ex_conv(user_sting)):
            self.day, self.month, self.year = self.ex_conv(user_sting)
        else:
            self.day, self.month, self.year = "__",  "__", "____"

    @classmethod
    def ex_conv(cls, user_sting):
        return map(int, user_sting.split('-'))

    @staticmethod
    def valid(_):
        d, m, y = _
        try:
            datetime.date(y, m, d)
            return True
        except ValueError:
            print(f'Вы указали неправильное значение даты: {d, m, y}')
            return False

    @property
    def show(self):
        month_t = ["Январяб", "Февраля", "Марта", "Апреля", "Мая", "Июня",
                   "Июля", "Авгута", "Сентября", "Октября", "Ноября", "Декабря"]
        if isinstance(self.day, int):
            return f"{self.day:02d} {month_t[self.month - 1]} {self.year:04d}"
        else:
            return f"{self.day} {self.month} {self.year} (Не корректно указаны данные)"


user_d1 = Date("06-08-1979")
user_d2 = Date("29-02-2021")
print()
print(user_d1.show)
print(user_d2.show)

