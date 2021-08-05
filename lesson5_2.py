with open ('Text', 'r') as Text:
    content = Text.readlines()
    print('Содержимое файла:', content)
    print(f'В файле {len(content)} строк(и)')
    for i in range(0,len(content)):
        content[i].split()
        print(f'В {i+1} строке {len(content[i].split())} слов(а)')


