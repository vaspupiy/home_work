"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
from random import randint

name_file = 'set_of_numbers.txt'
with open(name_file, 'w', encoding='utf-8') as f:
    for n in range(randint(10, 30)):
        print(randint(-300, 300), file=f, end=' ')

with open(name_file, 'r', encoding='utf-8') as f:
    print(sum(map(int, f.read().split())))
