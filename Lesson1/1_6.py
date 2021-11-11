start = int(input())
stop = int(input())
day_count = 1
while stop >= start:
    start = 1.1*start
    day_count += 1
print(day_count)