n = int(input("Введите целое положительное число: "))
max_item = 0
while n > 0:
    if n % 10 == 9:
        max_item = 9
        break
    if n % 10 > max_item:
        max_item = n % 10
    n //= 10
print(max_item)
