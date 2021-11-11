income = int(input('Введите доход '))
outcome = int(input('Введите расход '))
if income>outcome:
    print('Ваша прибыль составила', income-outcome)
    print('Рентабильность выручки стоставляет', (income-outcome)/income)
    employee = int(input('Сколько у вас работает сотрудников? '))
    print('Прибыль на одного работника составляет', (income-outcome)/employee)
else:
    print('Ваш убыток составил', outcome-income)