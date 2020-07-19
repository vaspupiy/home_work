from itertools import count, cycle, islice
from sys import argv

lesson_4_task_6_a, start_count, step_count, repetitions_count, repetitions_cycle = argv
"""
start_count: число, с которого начнется генерация чисел
step_count: шаг, для генератора чисел
repetitions_count: количество чисел, которое необходимо сгенеировать
repetitions_cycle: количество повторений элементов списка
"""

try:
    user_list = [i for i in islice(count(int(start_count), int(step_count)), (int(repetitions_count)))]
    for i in islice(cycle(user_list), int(repetitions_cycle)):
        print(i)
except ValueError:
    print("Ошибка ввода. Ожидается ввод целых чисел")
