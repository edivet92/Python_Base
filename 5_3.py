with open('text5_3.txt', 'r', encoding='utf-8') as presidents:
    low_payment = []
    payment = 0
    worker_counter = 0
    for line in presidents:
        worker_counter += 1
        line_list = line.split()
        payment += float(line_list[-1])
        if float(line_list[-1]) < 20000.0:
            low_payment.append(line_list[0:-1])
    print(f'Эти люди получают меньше 20 тыр в месяц {low_payment}')
    print(f'Средняя зарплата по цеху состовляет {payment/worker_counter:.2f}')