name_bot = "Вася"
name_user = input("Укажите, как я могу к Вам обращаться: ")
print()
massage = f"""Очень притятно, {name_user}. 
Меня зовут Робот - {name_bot}
Я хотел бы предложить Вам отгадать несколько загадок, 
Но сперва докажите, что вы не робот :).
"""
print(massage)
while True:
    user_ans = input("Сколько будет: дважды два - четыре?: ")
    if user_ans == "True" or user_ans == "1":
        print("Ура, я общаюсь с человеком!\n")
        break
    print(f"Сожалею, {name_user}, Вы все еще не доказали, что Вы не робот")
    print("Подсказка : 2 * 2 == 5 # Вывод: False")
max_cont = 2
count = 0
print("Попробуте отгадать первую загадку: \n")
massage = f"""Ночью он совсем не спит,
Дом от мышек сторожит,
Молоко из миски пьёт,
Ну конечно это -  """
user_ans = input(massage)
if user_ans == "Кот" or user_ans == "кот" or user_ans == "КОТ":
    print(f"Правильно - это {user_ans}: \n")
    count += 1
else:
    print(f"Вы не угадали, правильный ответ - кот: \n")
print("Попробуте отгадать вторую загадку: : \n")
massage = f"""Он зимой в берлоге спит,
Потихонечку храпит,
А проснётся, ну реветь,
Как зовут его -  """
user_ans = input(massage)
if user_ans == "Медведь" or user_ans == "медведь" or user_ans == "МЕДВЕДЬ":
    print(f"Правильно - это {user_ans}: \n")
    count += 1
else:
    print(f"Вы не угадали, правильный ответ - медведь: \n")
massage = f"""{name_user}, спасбо за внимание
Вы пытались отгадать {max_cont} загадки и отгадали из них {count}
C Вами был робот {name_bot}, всего доброго!
"""
print(massage)
