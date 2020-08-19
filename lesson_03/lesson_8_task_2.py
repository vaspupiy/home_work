"""
 Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
 вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту
 ситуацию и не завершиться с ошибкой.
"""


class MyZeroDivisionError(Exception):
    def __init__(self, txt):
        self.txt = txt


try:
    dividend, divisor = map(float, input("Введите делимое и делитель через пробел: ").split())
    if divisor == 0:
        raise MyZeroDivisionError("На ноль делить нельзя")
except ValueError:
    print("Вы ввели не числа")
except MyZeroDivisionError as err:
    print(err)
else:
    print(f"Результат деления: {dividend / divisor}")
