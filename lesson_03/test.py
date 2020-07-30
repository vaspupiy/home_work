class Iter:
    def __init__(self, start=0):
        self.i = start - 1

    # Метод __iter__ должен возвращать объект-итератор
    def __iter__(self):
        return self

    def __next__(self):
        self.i += 1
        if self.i <= 5:
            return self.i
        else:
            raise StopIteration

    def obj_it(self):
        for el in self.i:
           return  el


obj = Iter(start=2)
print(obj.obj_it)
