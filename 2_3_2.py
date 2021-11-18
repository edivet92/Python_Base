my_dict = {
    'winter': [12, 1, 2],
    'spring': [3, 4, 5],
    'summer': [6, 7, 8],
    'autumn': [9, 10, 11]
}
month = int(input("Введите месяц "))
for key, value in my_dict.items():
    if month in value:
        print(key)