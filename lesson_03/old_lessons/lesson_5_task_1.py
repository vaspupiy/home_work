"""
1. Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.

"""
try:
    with open('lesson_5_task_1.txt', 'w', encoding='utf-8') as my_file:
        while True:
            user_string = input("Введите данные, для окончания ввода нажмите enter не вводя данные: ")
            if user_string:
                my_file.write(user_string + '\n')
            else:
                break
except IOError:
    print("Произошла ошибка ввода-вывода!")
