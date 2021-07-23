print('Читерский вариант:')
number = int(input('Введите натуральное число (от 1 до 9)'))
my_list = [8,5,3,2]

if number >= 1 and number <=9:
    my_list.append(number)
    my_list.sort(reverse=True)
    print(my_list)
else:
    print('Неверный ввод')

print('Нечитерский вариант:')

number = int(input('Введите натуральное число (от 1 до 9)'))
my_list = [8,5,3,2]
twins = my_list.count(number)
try:
    for el in my_list:
        if twins > 0:
            i = my_list.index(number)
            my_list.insert(i + twins, number)
            break
        else:
            if number > el:
                j = my_list.index(el)
                my_list.insert(j, number)
                break
            elif number < my_list[-1]:
                my_list.append(number)
    print(my_list)
except ValueError:
    print('Неверный ввод')


