user_lst = input("Введите строку из нескольких слов, разделённых пробелами: ").split()
for i in range(len(user_lst)):
    print(f"{i + 1}. {user_lst[i][:10]}")


print("\nТо же самое, почитав методичку:")
for i, e in enumerate(user_lst, 1):
    print(f"{i}. {e[:10]}")
