def my_func(a, b, c):
    my_list = [a, b, c]
    my_list.remove(min(my_list))
    return sum(my_list)
print('Сумма двух мешьших чисел равна', my_func(int(input('Введите первое число ')), 
              int(input('Введите второе число ')), 
              int(input('Введите третье число '))))