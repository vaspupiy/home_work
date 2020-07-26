class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        return 'Запуск отрисовки'


class Pen(Stationery):
    def draw(self):
        return f'Запуск отрисовки Ручкой'


class Pencil(Stationery):
    def draw(self):
        return 'Запуск отрисовки Карандашом'


class Handle(Stationery):
    def draw(self):
        return 'Запуск отрисовки Маркером'


st = Stationery("Кисть")
print(st.title, st.draw(), sep='\n')

pen1 = Pen("Ручка")
pencil1 = Pencil("Карандаш")
handle1 = Handle("Маркер")

print(pen1.title, pen1.draw(), sep='\n')
print(pencil1.title, pencil1.draw(), sep='\n')
print(handle1.title, handle1.draw(), sep='\n')


