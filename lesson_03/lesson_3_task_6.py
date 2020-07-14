def int_func(text):
    lst = list(text)
    lst[0] = (chr(ord(lst[0]) - 32))
    return "".join(lst)


print(int_func("python"))
