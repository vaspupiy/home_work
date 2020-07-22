"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""
with open('text_3.txt', 'r', encoding='utf-8') as file:
    score = 0
    workers = file.readlines()
    print("Список зарабатывающих менее 20000 $: ")
    for line in workers:
        name, salary = line.split()
        salary = float(salary)
        if salary < 20000:
            print(name)
        score += salary
    print(f'средняя величина дохода сотрудников: {score / len(workers)} $')

print("\n Вариант 2.\n")
with open('text_3.txt', 'r', encoding='utf-8') as file:
    workers = [line.split() for line in file.readlines()]
    print("Список нищебродов, зарабатывающих менее 20000 $: ")
    for name in (workers):
        name[1] = float(name[1])
        print(name[0]) if name[1] < 20000 else print(end='')
    print(f'средняя величина дохода сотрудников: {sum([name[1] for name in workers]) / len(workers)} $')
