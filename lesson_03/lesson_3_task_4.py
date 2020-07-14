def my_func(x, y):
    if y < 0:
        return 1 / my_func(x, -y)
    p = 1
    for i in range(y):
        p *= x
    return p


def my_test():
    print(f"test_1: {my_func(2.43, -1) == pow(2.43, -1)}")
    print(f"test_2: {my_func(2.43, -76) == pow(2.43, -76)}")
    print(f"test_3: {my_func(2.43, -5) == pow(2.43, -5)}")
    print(f"test_4: {my_func(2.43, -2) == pow(2.43, -2)}")
    print(f"test_5: {my_func(2.43, 13) == pow(2.43, 13)}")
    print(f"test_5_1: {round(my_func(2.43, 13), 10) == round(pow(2.43, 13), 10)}")
    print(f"test_6: {my_func(0, 2) == pow(0, 2)}")
    print(f"test_7: {my_func(2.43, -7) == pow(2.43, -7)}")
    print(f"test_7_1: {round(my_func(2.43, -7), 17) == round(pow(2.43, -7), 17)}")
    print(f"test_8: {my_func(2.43, -11) == pow(2.43, -11)}")
    print(f"test_8_1: {round(my_func(2.43, -11), 17) == round(pow(2.43, -11), 17)}")
    print(f"test_9: {my_func(1.43, -6) == pow(1.43, -6)}")
    print(f"test_9_1: {round(my_func(1.43, -6), 16) == round(pow(1.43, -6), 16)}")


my_test()

print()
print("test_5")
print(my_func(2.43, 13))
print(pow(2.43, 13))
print()
print("test_7")
print(my_func(2.43, -11))
print(pow(2.43, -11))
print()
print("test_9")
print(1.43**(-6))
print(1 / (1.43 * 1.43 * 1.43 * 1.43 * 1.43 * 1.43))
print(my_func(1.43, -6))
