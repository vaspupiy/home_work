def my_func(x, y):
    """
    Функция принимает действительное положительное число x и целое число y (возможно отрицательное).
    Выводит результат возведения числа x в степень y.

    """
    if y < 0:
        return 1 / my_func(x, -y)
    p = 1
    for i in range(y):
        p *= x
    return p


def my_func_r(x, y):
    """
    Функция принимает действительное положительное число x и целое число y (возможно отрицательное).
    Выводит результат возведения числа x в степень y. Без цикла, только рекурсия.

    """
    if y < 0:
        return 1 / my_f_pow(x, -y)
    if y == 0:
        return 1
    return my_f_pow(x, y - 1) * x


def my_f_pow(x, y):
    """
    Функция принимает действительное положительное число x и целое число y (возможно отрицательное).
    Выводит результат возведения числа x в степень y.
    Учтен алгоритм быстрого возведения в степень для четной стпенеи

    """
    if y < 0:
        return 1 / my_f_pow(x, -y)
    if y == 0:
        return 1
    if y % 2 == 0:
        return my_f_pow(x * x, y / 2)  # return my_f_pow(x, y / 2) * my_f_pow(x, y / 2)
    return my_f_pow(x, y - 1) * x


def my_test():
    """
    Функция сравнивает результаты работы моей функции с результатами функции pow()
    При совпадении результатов выводит True.
    Если результаты не совпали, выводит входные данные и результаты сравниваемых функций

    """
    x_l = [i * i / 100 for i in range(1, 30, 9)]
    y_l = [i for i in range(-13, 13)]
    for x in x_l:
        for y in y_l:
            if my_func(x, y) == pow(x, y):
                print("True")
            else:
                print(f'x = {x}, y = {y}, my_func {my_func(x, y)} :pow {pow(x, y)}')


def my_test_r():
    """
    Функция сравнивает результаты работы моей функции с результатами функции pow()
    При совпадении результатов выводит True.
    Если результаты не совпали, выводит входные данные и результаты сравниваемых функций

    """
    x_l = [i * i / 100 for i in range(1, 30, 9)]
    y_l = [i for i in range(-13, 13)]
    for x in x_l:
        for y in y_l:
            if my_func_r(x, y) == pow(x, y):
                print("True")
            else:
                print(f'x = {x}, y = {y}, my_func {my_func_r(x, y)} :pow {pow(x, y)}')


def my_test2():
    """
    Функция сравнивает результаты работы моей функции с результатами функции pow()
    При совпадении результатов выводит True.
    Если результаты не совпали, выводит входные данные и результаты сравниваемых функций

    """
    x_l = [i * i / 100 for i in range(1, 30, 9)]
    y_l = [i for i in range(-13, 13)]
    for x in x_l:
        for y in y_l:
            if my_f_pow(x, y) == pow(x, y):
                print("True")
            else:
                print(f'x = {x}, y = {y}, my_func {my_f_pow(x, y)} :pow {pow(x, y)}')


my_test()
print("\n\ntest_r")
my_test_r()
print("\n\ntest_2")
my_test2()
# Видимо что-то с окурлением... При ошибке  - разница была бы огромной.(Наверное, скорее всего)
