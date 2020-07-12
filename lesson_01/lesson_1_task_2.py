seconds = int(input("Введите время в секундах: "))
fix = ""
if seconds < 0:
    seconds *= -1
    fix = "-"
minutes = seconds // 60
seconds = seconds % 60
hours = minutes // 60
minutes = minutes % 60
print(f"{fix}{hours // 10}{hours % 10}:{minutes // 10}{minutes % 10}:{seconds// 10}{seconds % 10}")
print(f'{hours:02d}:{minutes:02d}:{seconds:02d}')