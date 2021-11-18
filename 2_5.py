my_list = [11, 9, 5, 3, 2, 2, 1]
number = int(input("Input your number "))
for i in range(len(my_list)):
    if number > my_list[i]:
        my_list.insert(i, number)
        break
else:
    my_list.append(number)
print(my_list)