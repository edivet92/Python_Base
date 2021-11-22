def int_func():
    for word in input().split():
        i = 0
        word = word.lower()
        for letter in word:
            if 96 < ord(letter) < 123:
                i +=1
        if len(word) == i:
            print(word.title(), end=' ')
        else:
            print(word, end = " ")
int_func()