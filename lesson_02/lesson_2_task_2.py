user_lst = input("Введите элементы через пробел: ").split()
for i in range(1, len(user_lst), 2):
    user_lst[i - 1], user_lst[i] = user_lst[i], user_lst[i - 1]
print(user_lst)
