"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""
with open('text_3.txt', 'r', encoding='utf-8') as file:
    score = 0
    workers = file.readlines()
    print(workers)
    for line in workers:
        name, salary = line.split()
        salary = float(salary)
        if salary < 20000:
            print(name)
        score += salary
    print(score / len(workers))

with open('text_3.txt', 'r', encoding='utf-8') as file:
    workers = [line.split() for line in file.readlines()]
    print(workers)
