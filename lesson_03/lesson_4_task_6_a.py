from itertools import count, cycle
from sys import argv

lesson_4_task_6_a, start_count, step_count, repetitions_count, repetitions_cycle = argv

iter_count = count(int(start_count), int(step_count))
user_list = [next(iter_count) for i in range(int(repetitions_count))]

iter_cycle = cycle(user_list)
for i in range(int(repetitions_cycle)):
    print(next(iter_cycle))
