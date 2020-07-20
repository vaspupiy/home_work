from itertools import count, cycle
from sys import argv

lesson_4_task_6_b, start_count, step_count, stop_count, rep = argv
"""
start_count: число, с которого начнется генерация чисел(включительно)
step_count: шаг, для генератора чисел(целое чило != 0)
stop_count: число, на котором генерация чисел остановится(включительно)
rep: количество повторений элементов списка(целое чило > 0)
Без break :)
"""
try:
    start_count, step_count, stop_count, rep = int(start_count), int(step_count), int(stop_count), int(rep)
    if step_count == 0 or step_count < 0 and start_count < stop_count or step_count > 0 and start_count > stop_count:
        print("Ошибка ввода. Не возможно сосздать достич stop_count")
    else:
        iter_count = count(start_count, step_count)
        count_lst = []
        if step_count > 0:
            while not count_lst or count_lst[-1] <= int(stop_count):  # если stop_count включительно
                count_lst.append(next(iter_count))
            iter_cycle = cycle(count_lst)
        else:
            while not count_lst or count_lst[-1] >= int(stop_count):  # если stop_count включительно
                count_lst.append(next(iter_count))
            iter_cycle = cycle(count_lst)
        if rep <= 0:
            print("Ошибка ввода. 'rep' должно быть > 0")
        else:
            for item in range(rep):
                print(next(iter_cycle))
except ValueError:
    print("Ошибка ввода. Ожидается ввод целых чисел")

"""
test:
lesson_4_task_6_b.py -15 5 -30 15
lesson_4_task_6_b.py -15 5 20 15
lesson_4_task_6_b.py -15 0 20 15
lesson_4_task_6_b.py -15 -5 -30 15
lesson_4_task_6_b.py 5 5 20 0
lesson_4_task_6_b.py 5 5 20 -3
lesson_4_task_6_b.py 5 5 20 hgh
lesson_4_task_6_b.py 5 -5 20 2
"""
