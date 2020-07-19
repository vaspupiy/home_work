from functools import reduce


print(f'Произведение всех элементов списка:  {reduce(lambda x, y: x * y, [i for i in range(100, 1001, 2)])}')

print(f'Произведение всех элементов списка(тест):  {reduce(lambda x, y: x * y, [i for i in range(10, 15, 2)])}')
