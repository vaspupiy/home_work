def my_div(dividend, divider):
    """
    функция выполняет деление двух чисел и возвращает результат деления.
    В функции предусмотрена обработка ситуации деления на ноль.
    """

    try:
        dividend, divider = int(dividend), int(divider)
    except ValueError:
        return "Ошибка ввода"

    try:
        result = dividend / divider
        return result
    except ZeroDivisionError:
        return "В этой стране на ноль делить нельзя"


print(my_div(5, 0))
