import math


def fact(n):
    """Функция создает объект-генератор, выводит  первые n чисел, начиная с 1! и до n!"""
    if isinstance(n, int) and n > 0:
        for num in range(1, n + 1):
            yield math.factorial(num)
    else:
        yield "Ошибка ввода. Необходимо вводить целое число больще 0."


def my_fact(n):
    """Функция создает объект-генератор, выводит  первые n чисел, начиная с 1! и до n!"""
    if isinstance(n, int) and n > 0:
        f = 1
        for num in range(1, n + 1):
            f *= num
            yield f
    else:
        yield "Ошибка ввода. Необходимо вводить целое  число больще 0."


def test():
    test_lst = [0, -3, 3, 1.3, 2 * 3, 3 / 2, 3 // 2, "test", my_fact(4)]
    for item in test_lst:
        print(f"n = {item}")
        for i in my_fact(item):
            print(f"my_fact: {i}")
        for i in fact(item):
            print(f"fact: {i}")


test()
