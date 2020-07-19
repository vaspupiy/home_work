from sys import argv

lesson_4_task_1, production, rate, prize = argv
print(f'Результат расчета заработной платы сотрудника: {int(production) * int(rate) + int(prize)} у.е.')
