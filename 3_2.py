def my_func(name, surname, birthday, city, email, number):
    return f'Name - {name}, Surname - {surname}, Birthday - {birthday}, '\
           f'City - {city}, E-mail - {email}, Phonenumber - {number}'
print(my_func(name=input('Введите имя '), surname=input('Введите фамилию '), 
             birthday=input('дата рождения '), city=input('ваш город '), 
             email=input('почта '), number=input('номер телефона ')))