from random import randint
with open('text5_5.txt', 'w') as numbers:
    #counter = 0
    for i in range(1, 150, randint(1, 10)):
        #counter += i
        numbers.write(f'{i} ')
    #print(counter)
with open('text5_5.txt', 'r') as count:
    number_list = count.readline().split()
    calculator = 0
    for i in number_list:
        calculator += int(i)
    print(calculator)