try:
    with open('lesson_5_task_1+2.txt', 'w+', encoding='utf-8') as my_file:
        while True:
            user_string = input("Введите данные, для окончания ввода нажмите enter не вводя данные: ")
            if user_string:
                my_file.write(user_string + '\n')
            else:
                break
        my_file.seek(0, 0)
        text = [line.split() for line in my_file.readlines()]
        print(f'количество строк: {len(text)}')
        for num, line in enumerate(text, 1):
            print(f'количество слов в {num} строке: {len(line)}')
except IOError:
    print("Произошла ошибка ввода-вывода!")
