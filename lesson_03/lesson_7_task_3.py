class Cell:
    def __init__(self, n_cells):
        self.n_cells = n_cells

    def __add__(self, other):
        return self.n_cells + other.n_cells

    def __sub__(self, other):
        if self.n_cells >= other.n_cells:
            return self.n_cells - other.n_cells
        return other.n_cells - self.n_cells

    def __mul__(self, other):
        return self.n_cells * other.n_cells

    def __truediv__(self, other):
        try:
            return int(round(self.n_cells / other.n_cells, 0))
        except ZeroDivisionError:
            return "Значение количества клеток делителя должнно быть больше 0"

    def make_order(self, row):
        ord_str = ''
        row_ = row
        for i in range(self.n_cells):
            if row_ > 0:
                ord_str += '*'
                row_ -= 1
            else:
                ord_str += '\n'
                ord_str += '*'
                row_ = row - 1
        return ord_str


cell_1 = Cell(14)
cell_2 = Cell(7)
print(cell_1 / cell_2)
print(cell_2 / cell_1)
print(cell_1 * cell_2)
print(cell_2 * cell_1)
print(cell_1 + cell_2)
print(cell_2 + cell_1)
print(cell_1 - cell_2)
print(cell_2 - cell_1)
print(cell_1.make_order(3))
