class MyErr(Exception):
    def __init__(self, text):
        self.text = text
numbers = [input('Input numbers') for i in range(2)]
try:
    x, y = map(int, numbers)
    if y == 0:
        raise MyErr("Can't devide by zero")
except MyErr as err:
    print(err)
except ValueError:
    print("Only numbers")
else:
    print(x/y)