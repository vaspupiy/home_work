while True:
    result = float(input("Укажите результат первого дня в километрах: "))  # не факт, что int()(мараф. дист. = 42.195)
    if result > 0:
        break
    print("Результат первого дня должен быть больше 0")
required_result = float(input("Укажите результат который необходимо достичь (либо превзойти): "))
day = 1
while result < required_result:
    day += 1
    result = result + result / 10
print(f"Ответ: на {day}-й день спортсмен достиг результата — не менее {required_result} км.")
