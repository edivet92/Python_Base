from sys import argv
name, workout, rate, prize = argv
pay = int(workout)*int(rate)+int(prize)
print('Зарплата составляет', pay)