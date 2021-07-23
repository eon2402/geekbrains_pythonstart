number = int(input('Введите номер месяца'))
if number <= 12 and number >= 1:
    dict = {1:'Январь', 2:'Февраль', 3:'Март', 4:'Апрель', 5:'Май', 6:'Июнь', 7:'Июль', 8:'Август',
         9:'Сентябрь', 10:'Октябрь', 11:'Ноябрь', 12:'Декабрь'}
    list = list(dict.values())
    print('Через Dict:')
    print(dict.get(number))
    if number == 12 or number == 1 or number == 2:
        print('Время года - зима')
    elif number == 3 or number == 4 or number == 5:
        print('Время года - весна')
    elif number == 6 or number == 7 or number == 8:
        print('Время года - лето')
    else:
        print('Время года - лето')
    print('Через list:')
    print(list[number-1])
    if number == 12 or number == 1 or number == 2:
        print('Время года - зима')
    elif number == 3 or number == 4 or number == 5:
        print('Время года - весна')
    elif number == 6 or number == 7 or number == 8:
        print('Время года - лето')
    else:
        print('Время года - лето')
else:
    print('Неверный ввод, введите число от 1 до 12')