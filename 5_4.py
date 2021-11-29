from translate import Translator
translator = Translator(to_lang='russian')
with open('text5_4.txt', 'r', encoding='utf-8') as numbers:
    result = open('text5_4output.txt', 'w', encoding='utf-8')
    for line in numbers:
        result.write(f'{translator.translate(line[0:-4])} {line[-4:]}')
    result.close()