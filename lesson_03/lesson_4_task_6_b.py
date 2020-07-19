from itertools import count, cycle
from sys import argv

lesson_4_task_6_b, start_count, step_count, stop_count, repetitions = argv

iter_count = count(int(start_count), int(step_count))
count_lst = []
while not count_lst or count_lst[-1] <= int(stop_count):  # если stop_count включительно
    count_lst.append(next(iter_count))

iter_cycle = cycle(count_lst)
for item in range(int(repetitions)):
    print(next(iter_cycle))
