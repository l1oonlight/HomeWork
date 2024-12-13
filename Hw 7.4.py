def redactor():
    file = open(f'{input('Придумай название файла : ')}.txt', 'w+', encoding='utf-8')
    text = f'Что ты хочешь написать? : '
    print(text)
    while text != '':
        text = input()
        file.write(f'{text} \n')
    file.close()
redactor()