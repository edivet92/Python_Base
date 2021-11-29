with open("text5_1.txt", "w", encoding="utf-8" ) as f:
    while True:
        stop_point = input()
        if stop_point == "":
            break
        else:
            f.write(stop_point + '\n')