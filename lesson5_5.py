with open('numbers', 'w') as my_file:
    input_numbers = input('Введите числа через пробел: ')
    print(input_numbers, file=my_file)

with open('numbers') as my_file:
    content = my_file.read().split()
    sum = 0
    for el in content:
        sum += int(el)
    print(sum)

