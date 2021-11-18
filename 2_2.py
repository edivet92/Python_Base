my_list = []
count = int(input('Ввести количество элементов в списке '))
for i in range(count):
    my_list.append(input('Ввести элемент списка '))
print(my_list)
if count%2 != 0:
    count -= 1
for n in range(count):
    if (n+1)%2 != 0:
        my_list[n], my_list[n+1] = my_list[n+1], my_list[n]
print(my_list)