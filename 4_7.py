from math import factorial
n = int(input("До скольки считать "))
def fact():
    for i in range(1, n+1):
        yield factorial(i)
i = 1
for m in fact():
    print(f"Факториал {i} равен {m}")
    i += 1