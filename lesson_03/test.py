class Iterator:
    """
    Объект-итератор
    """
    def __init__(self, start=0):
        self.i = start
    # У итератора есть метод __next__

    def __next__(self):
        self.i += 1
        if self.i <= 5:
            return self.i
        else:
            raise StopIteration


class IterObj:
    """
    Объект, поддерживающий интерфейс итерации (итерируемый объект)
    """
    def __init__(self, start=0):
        self.start = start - 1

    def __iter__(self):
        # Метод __iter__ должен возвращать объект-итератор
        return Iterator(self.start)


obj = IterObj(start=2)
for el in obj:
    print(el)


print("Еще раз ...")
for el in obj:
    print(el)

