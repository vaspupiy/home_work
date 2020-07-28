# def int_func(text):
#     lst = list(text)
#     lst[0] = (chr(ord(lst[0]) - 32))
#     return "".join(lst)


def int_func(text):
    """ Функция принмвает слово из маленьких латинских букв и возвращающую его же, но с прописной первой буквой"""
    return (chr(ord(text[0]) - 32)) + text[1:]


def test_inp(text):
    """Функция проверяет слово и возвращет True, если слово состоит из маленьких латинских букв"""
    for i in text:
        if not 97 <= ord(i) <= 122:
            return
    return True


def app_func():
    """
    Функция запрашивает строку из слов, разделенных пробелом,
    и возвращает исходную строку, но каждое слово -  с заглавной буквы
    В случае не корректногог ввода, функция сообщает об ошибке и просит повторить ввод

    """
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
