class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year
    @classmethod
    def remake_date(cls, date_string):
        day, month, year = map(int, date_string.split('-'))
        final_date = cls(day, month, year)
        return f'{final_date.day}:{final_date.month}:{final_date.year}'
    @staticmethod
    def date_validation(date_string):
        day, month, year = map(int, date_string.split('-'))
        return 1 <= day <= 31 and 1 <= month <= 12 and year <= 9999
user_date = input('Type your date like dd-mm-yyyy ')
print(Date.remake_date(user_date)) if Date.date_validation(user_date) else print('Your date is invalid')