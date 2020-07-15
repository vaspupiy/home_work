struct_data = []

characteristics = (("название", "Укажите название товара: "),
                   ("цена", "Укажите цену товара в у.е.: "),
                   ("количество", "Укажите количество товара: "),
                   ("eд.", "Укажите единицу измерения: "))

number = 0

# struct_data = [
#     (1, {'название': 'компьютер', 'цена': 20000.0, 'количество': 5.0, 'eд.': 'шт.'}),
#     (2, {'название': 'принтер', 'цена': 6000.0, 'количество': 2.0, 'eд.': 'шт.'}),
#     (3, {'название': 'сканер', 'цена': 2000.0, 'количество': 7.0, 'eд.': 'шт.'})
# ]
# number = 3

n_inp = int(input("Укажите количество товара, для котрого будут введены параметры: "))
for i in range(n_inp):
    d_param = dict()
    s_inp = input("Введите через пробел:\n'название товара' 'цену товара' "
                  "'количество товара' 'единицу измерения':\n ").split()
    if not (''.join(s_inp[1].split('.', 1)).isdigit() and ''.join(s_inp[2].split('.', 1)).isdigit()):
        print("\nОшибка ввода данных! Данные в базу не введины!\n"
              "Значения данных 'цена' и 'количество' не могут быть отрицательными и должны указываться цыфрами.\n"
              "Пример корректного ввода:\n [мука 45.5 75.5 кг.]\n"
              f"Ваш ввод:\n {' '.join(s_inp)}\n"
              "Позже, Вы сможете ввести эти значения по отдельности.\n")
        continue
    else:
        for ind, key in enumerate(characteristics):
            d_param[key[0]] = (s_inp[ind].lower() if ind not in [1, 2] else float(s_inp[ind]))
        if input("\nПроверьте введенные вами данные: \n"
                 f"{d_param}\n"
                 " Если все правильно, введите 'да': ").lower() != "да":
            print("\nВвод отменен пользователем.\n"
                  "Позже, Вы сможете ввести эти значения по отдельности.\n")
            continue
    number += 1
    item_t = (number, d_param)
    struct_data.append(item_t)
    print()

while True:
    if input("Для начала ввода данных введите 'да'. Желаете ввести данные по отдельности?: ").lower() != "да":
        break
    d_param = dict()
    for i in characteristics:
        d_param[i[0]] = input(i[1]).lower()
    if not (''.join(d_param["цена"].split('.', 1)).isdigit() and ''.join(
            d_param["количество"].split('.', 1)).isdigit()):
        print("\nОшибка ввода данных! Данные в базу не введины!\n"
              "Значения данных 'цена' и 'количество' не могут быть отрицательными и должны указываться цыфрами.\n"
              "Пример корректного ввода:\n {'название': 'мука', 'цена': '45.5', 'количество': '75.5', 'eд': 'кг.'}\n"
              f"Ваш ввод:\n {d_param}\n")
        continue
    else:
        d_param["цена"] = float(d_param["цена"])
        d_param["количество"] = float(d_param["количество"])
        if input("\nПроверьте введенные вами данные: \n"
                 f"{d_param}\n"
                 " Если все правильно, введите 'да': ").lower() != "да":
            print("\nВвод отменен пользователем.\n")
            continue
    number += 1
    item_t = (number, d_param)
    struct_data.append(item_t)
    print()

analytic = {'название': [], 'цена': [], 'количество': [], 'eд.': []}
if struct_data:
    print(f'\nСтруктура данных «Товары»: {struct_data}')
    for key in analytic:
        for i in struct_data:
            analytic[key].append(i[1][key])
    print(f"\nАналитика структуры данных «Товары»:\n {analytic}")
else:
    print("\nНевозможно вывести аналитику.\nВ структуре данных «Товары» отсутствуют данные.")