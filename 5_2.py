with open('text5_2.txt', 'r', encoding="utf-8") as poem:
    line_counter = 0
    for line in poem:
        line_counter += 1
        word_counter = line.count(" ") - line.count(" —") + line.count("\n") #можно заменить на len(line.split()), но тире мешают
        print(f'В {line_counter} строчке {word_counter} слов')
    print(f'Всего строчек {line_counter}')