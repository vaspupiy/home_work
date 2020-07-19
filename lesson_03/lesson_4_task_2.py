while True:
    try:
        user_input = list(map(int, input("Введите список чисел через пробел: ").split()))
        break
    except ValueError:
        print("Ошибка ввода")
print(f'Результат: {[user_input[i] for i in range(1, len(user_input)) if user_input[i] > user_input[i - 1]]}')

# test: 300 2 12 44 1 1 4 10 7 1 78 123 55  / Результат: [12, 44, 4, 10, 78, 123]
