def my_func(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        return 'Нельзя делить на ноль'
print(my_func(int(input('Введите "a" ')), int(input('Введите "b" '))))