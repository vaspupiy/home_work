def int_func(s=0):
    user_inp = input("Ведите строку чисел, разделенных пробелом."
                     "\nДля завершения,  вместо числа введите- q ").lower().split()
    if "q" in user_inp:
        user_inp = list(map(int, user_inp[:user_inp.index("q")]))
        print(s + sum(user_inp))
        return
    else:
        user_inp = list(map(int, user_inp))
        s += sum(user_inp)
        print(s)
        int_func(s)


int_func()
