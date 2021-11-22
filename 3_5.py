def my_f():
    total = 0
    while True:
        my_list = input('type "s" to stop').split()
        for number in my_list:
            if number == 's':
                return 'Total sum = ', total, 'bye'
                break
            else:
                try:
                    total += int(number)
                except ValueError:
                    print('Oh-way')
        print('Total sum = ', total)
print(my_f())