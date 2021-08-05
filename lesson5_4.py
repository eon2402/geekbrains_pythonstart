russian_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

with open('1234') as english, open('1234rus', 'w') as russian:
    words = english.readlines()
    for line in words:
        line = line.strip('\n')
        print(line)
        if line:
            word, digit = line.split(' — ')
            russian.write(f'{russian_dict[word]} — {digit}\n')
