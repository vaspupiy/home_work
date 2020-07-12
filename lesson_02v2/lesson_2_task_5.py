my_list = [7, 5, 3, 3, 2]
user_n = float(input())
ins = 0
for i in range(len(my_list)):
    if user_n > my_list[i]:
        break
    ins += 1
my_list.insert(ins, user_n)
print(my_list)

