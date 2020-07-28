"""
6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий. Сформировать словарь,
содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
"""

with open('text_6.txt', 'r', encoding='utf-8') as f:
    total_classes = {}
    for line in f.readlines():
        classes, other = line.split(':')
        other = other.split('(')
        total_classes[classes] = sum([int(''.join(i for i in j if i.isdigit())) for j in other[:-1]])
print(total_classes)
