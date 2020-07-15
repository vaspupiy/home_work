# def int_func(text):
#     lst = list(text)
#     lst[0] = (chr(ord(lst[0]) - 32))
#     return "".join(lst)


def int_func(text):
    return (chr(ord(text[0]) - 32)) + text[1:]


def test_inp(text):
    for i in text:
        if not 97 <= ord(i) <= 122:
            return False
    return True


def app_func():
    mass = "Ведите строку из слов, разделенных пробелом.\n" \
           "Каждое слово должно состоять из латинских букв в нижнем регистре: \n"
    us_inp = input(mass).split()
    for i, word in enumerate(us_inp):
        if not test_inp(word):
            print("Ошибка ввода")
            return app_func()
        us_inp[i] = int_func(us_inp[i])
    return us_inp


print(*app_func())
