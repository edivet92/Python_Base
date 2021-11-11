time = int(input("введите время в секундах "))
hours = time//3600
minutes = time%3600//60
secundes = time%3600%60
print(f"{hours:02}:{minutes:02}:{secundes:02}")