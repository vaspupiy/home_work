class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'Запуск отрисовки, инструмент: {self.title}'


class Pen(Stationery):
    def draw(self):
        if self.title.lower() == "ручка":  # Ни чего умней не придумал для title
            return f'Запуск отрисовки Ручкой'
        else:
            return 'Ошибка ввода значения для title. class "Pen" подразумевает отрисовку инструментом: "Ручка"'


class Pencil(Stationery):
    def draw(self):
        if self.title.lower() == "карандаш":
            return 'Запуск отрисовки Карандашом'
        else:
            return 'Ошибка ввода значения для title. class "Pen" подразумевает отрисовку инструментом: "Карандаш"'


class Handle(Stationery):
    def draw(self):
        if self.title.lower() == "маркер":
            print(self.title.lower())
            return 'Запуск отрисовки Маркером'
        else:
            return 'Ошибка ввода значения для title. class "Pen" подразумевает отрисовку инструментом: "Маркер"'


st = Stationery("Кисть")
print(st.title, st.draw(), sep='\n')

pen1 = Pen("Ручка")
pencil1 = Pencil("Карандаш")
handle1 = Handle("Маркер")
pen2 = Pen("Кисть")

print(pen1.title, pen1.draw(), sep='\n')
print(pencil1.title, pencil1.draw(), sep='\n')
print(handle1.title, handle1.draw(), sep='\n')
print(pen2.title, pen2.draw(), sep='\n')
