while True:
    revenue = float(input("Введите размер выручки в у.е.: "))
    if revenue >= 0:
        break
    print("Размер выручки не может быть отрицательным")
while True:
    costs = float(input("Введите размер издержек в у.е.: "))
    if costs >= 0:
        break
    print("Размер издержек не может быть отрицательным")
profit = revenue - costs
if profit < 0:
    print(f"Фирма понесла убытки в размере {- profit:.2f} у.е")
elif profit == 0:
    print("Нет ни прибыли не убытков")
else:
    print(f"Прибыль фирмы составила {profit:.2f} у.е")
    print(f"рентабельность выручки составила: {profit / revenue * 100:.2f} % ")
    while True:
        n_person = float(input("Введите количество сотрудников фирмы: "))  # бывает не целое число, при не полн. занят.
        if n_person > 0:
            break
        elif n_person == 0:
            print("Гугл говорит, что бывает и 0 сотрудников...Но давайте представим, что учредитель это сотрудник.")
        else:
            print("Вы, очевидно, ошиблись, введя отрицательное количество сотрудников.")
    print(f"Прибыль фирмы в расчете на одного сотрудник составила: {profit / n_person:.2f} у.е")
