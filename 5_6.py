with open('text5_6.txt', 'r', encoding="utf-8") as lesson_hours:
    vocabul = {}
    for line in lesson_hours:
        lesson_name = line[:line.find(':')]
        lesson_hours = sum(map(int, "".join(i for i in line if '0' <= i <= '9' or i == " ").split()))
        vocabul[lesson_name] = lesson_hours
    print(vocabul)