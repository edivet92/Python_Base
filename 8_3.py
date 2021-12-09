class MyErr(Exception):
    def __init__(self, text):
        self.text = text
    
my_list = []
while True:
    number = (input('Input number, "q" for exit '))
    if number != 'q':
        try:
            if number.isdigit():
                number = int(number)
            else:
                raise MyErr('Input only numbers')
        except MyErr as err:
            print(err)
        else:
            my_list.append(number)
    else:
        break
print(my_list)
