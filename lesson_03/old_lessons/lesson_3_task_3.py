def my_func(arg1, arg2, arg3):
    """Функция принимает три аргумента, и возвращает сумму наибольших двух аргументов"""
    my_l = [arg1, arg2, arg3]
    my_l.remove(min(my_l))
    return sum(my_l)


def test():
    """Примитивный тест для my_func, выводит номер теста и результат"""
    print(f"test_1: {my_func(0, 0, 0) == 0}")
    print(f"test_2: {my_func(-1, 0, 1) == 1}")
    print(f"test_3: {my_func(1, 2, 3) == 5}")
    print(f"test_4: {my_func(-1, -2, -3) == -3}")
    print(f"test_5: {my_func(1, 1, 2) == 3}")
    print(f"test_6: {my_func(1, 2, 2) == 4}")


test()
