"""
3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список.
Класс-исключение должен контролировать типы данных элементов списка.

Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно,
пока пользователь сам не остановит работу скрипта, введя, например, команду “stop”.
При этом скрипт завершается, сформированный список выводится на экран.

Подсказка: для данного задания примем, что пользователь может вводить только числа и строки.
При вводе пользователем очередного элемента необходимо реализовать проверку типа элемента и вносить его в список,
только если введено число. Класс-исключение должен не позволить пользователю ввести текст (не число)
и отобразить соответствующее сообщение. При этом работа скрипта не должна завершаться.
"""


class NotNumError(Exception):
    def __init__(self, text):
        self.text = text


def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


def check_list(user_list):
    try:
        for el in user_list:
            if not isfloat(el):
                raise NotNumError("Было введено не число! ")
    except NotNumError as err:
        print(err)
    else:
        return True


res_list = []
while True:
    user_inp = input("Введите список чисел через пробел, для завершения введите 'stop':\n").lower().split()
    if len(user_inp) == 1 and "stop" in user_inp:
        break
    if check_list(user_inp):
        print(user_inp)
        res_list += user_inp

print(res_list)
