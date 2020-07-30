class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __add__(self, other):
        if len(self.matrix) == len(other.matrix) and len(self.matrix[0]) == len(other.matrix[0]):
            return Matrix([[self.matrix[i][j] + other.matrix[i][j] for j in range(len(self.matrix[i]))] for i in
                           range(len(self.matrix))])
        else:
            return "Ошибка операции: Сложение матриц выполнимо только для матриц одинаковой размерности"

    def __str__(self):
        try:
            self.m_str = ''
            for row in self.matrix:
                for el in row:
                    self.m_str += f'{el:4d}' + ' '
                self.m_str += '\n'
            self.m_str = self.m_str[:-2]
            return self.m_str
        except ValueError:
            print("Не выводится сообщение, не понимаю почему")
            return "Не выводится сообщение, не понимаю почему"


m1 = Matrix([[1, 2], [2, 3], [3, 4], [1, 2]])
m2 = Matrix([[1, 2], [2, 3], [3, 4]])
m3 = Matrix([[1, 2], [2, 3], [3, 4]])
m4 = m3 + m2

print('\n1)')
print(m2 + m3 + m1)
print('\n2)')
print(m1)
print('\n3)')
print(m2)
print('\n4)')
print(m3)
print('\n5)')
print(m4)
print('\n6)')
print(m4 + m3 + m2)
