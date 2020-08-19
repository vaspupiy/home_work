class ComplexTypeErr(Exception):
    def __init__(self, text):
        self.text = text


class ComplexNum:
    """Комплексные числа"""
    def __init__(self, real_n, imaginary_n):
        if ComplexNum.valid_type(real_n, imaginary_n):
            self.real_n = real_n
            self.imaginary_n = imaginary_n

    @staticmethod
    def valid_type(real_n, imaginary_n):
        if (isinstance(real_n, int) or isinstance(real_n, float)) and \
                (isinstance(imaginary_n, int) or isinstance(imaginary_n, float)):
            return True
        else:
            raise ComplexTypeErr("Значения атрибутов должны быть 'int' либо 'float'")

    def __str__(self):
        return f"({self.real_n}+{self.imaginary_n}j)"

    def __add__(self, other):
        return ComplexNum(self.real_n + other.real_n, self.imaginary_n + other.imaginary_n)

    def __mul__(self, other):
        return ComplexNum(self.real_n * other.real_n - self.imaginary_n * other.imaginary_n,
                          self.real_n * other.imaginary_n + self.imaginary_n * other.real_n)


f = ComplexNum(9.5, 6.5)
print(f)
b = ComplexNum(9, 2)
print(b)
d = b + f
print(d)
s = b * f
print(s)
print()
print((9.5 + 6.5j) * (9 + 2j))

# r = ComplexNum(9, "")


