def my_div(dividend, divider):
    """
    функция выполняет деление двух чисел и возвращает результат деления.
    В функции предусмотрена обработка ситуации деления на ноль.
    """
    try:
        result = dividend / divider
        return result
    except ZeroDivisionError:
        return "В этой стране на ноль делить нельзя"


def my_int(string):
    try:
        string = int(string)
        return string
    except ValueError:
        print("Ошибка ввода. Ожидается ввод целого числа. Повторите ввод: ")
        return my_int(input())


d_nd = my_int(input("Ведите делимое: "))
d_er = my_int(input("Ведите делитель: "))

print(my_div(d_nd, d_er))

