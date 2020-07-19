from sys import argv

lesson_4_task_1, production, rate, prize = argv
try:
    print(f'Результат расчета заработной платы сотрудника:  {float(production) * float(rate) + float(prize):.2f} у.е.')
except ValueError:
    print("Ощибка ввода")