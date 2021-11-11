number = int(input())
result = 0
while number>0:
    i = number%10
    if i > result:
        result = i
    number = number//10
print(result)