"""
2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.

"""
try:
    with open('lesson_5_task_2.txt', 'r', encoding='utf-8') as file:
        text = [line.split() for line in file.readlines()]
        print(f'количество строк: {len(text)}')
        for num, line in enumerate(text, 1):
            print(f'количество слов в {num} строке: {len(line)}')
except IOError:
    print("Произошла ошибка ввода-вывода!")
