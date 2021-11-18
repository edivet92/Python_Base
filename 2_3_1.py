winter = [12, 1, 2]
spring = [3, 4, 5]
summer = [6, 7, 8]
autumn = [9, 10, 11]
month = int(input('введите месяц '))
if month in winter:
    print('Зима')
elif month in spring:
    print('Весна')
elif month in summer:
    print('Лето')
elif month in autumn:
    print('Осень')
else:
    print('Не то пальто')