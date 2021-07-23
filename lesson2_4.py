string = input('Введите несколько слов через пробел')
n = 0
for word in string.split(' '):
    n += 1
    if len(word) <= 10:
        print(n, word)
    else:
       print(n, word[0:10])