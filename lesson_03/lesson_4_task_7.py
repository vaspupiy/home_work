import math


def fact(n):
    if isinstance(n, int) and n >= 0:
        for num in range(n + 1):
            yield math.factorial(num)
    else:
        yield "Ошибка ввода. Необходимо вводить целое не отрицательное число."


def my_fact(n):
    if isinstance(n, int) and n >= 0:
        yield 1  # количество перестановок пустого множества равно единице
        f = 1
        for num in range(1, n + 1):
            f *= num
            yield f
    else:
        yield "Ошибка ввода. Необходимо вводить целое не отрицательное число."


def test():
    test_lst = [0, -3, 3, 1.3, 2 * 3, 3 / 2, 3 // 2, "test", my_fact(4)]
    for item in test_lst:
        print(f"n = {item}")
        for i in my_fact(item):
            print(f"my_fact: {i}")
        for i in fact(item):
            print(f"fact: {i}")


test()
