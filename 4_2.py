first_list = [20, 74, 56, 0, 3, 345, 45, 33]
second_list = [x for x in first_list if x > first_list[first_list.index(x)-1] and first_list.index(x) > 0]
print(second_list)