input_text = input('Введите строку:')
with open ('Textfile', 'w') as text:
    while input_text:
        text.write(input_text+'\n')
        input_text = input('Введите еще строку:')
        if not input_text:
            break