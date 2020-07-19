original_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result_list = [i for i in original_list if original_list.count(i) == 1]
print(result_list)
