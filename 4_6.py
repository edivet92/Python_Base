from itertools import count, cycle
number = int(input('Укажите число '))
break_point = number + 15
for i in count(number):
    if i > break_point:
        break
    else:
        print(i)


my_list = ['GHJ', 123, 12.3, [12, 13, 14], {1: "book", 2: 'pencil'}]
counter = 1
for m in cycle(my_list):
    if counter <= 10:
        print(m)
        counter += 1
    else:
        break