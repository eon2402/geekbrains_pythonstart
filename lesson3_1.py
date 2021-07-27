try:
    a = int(input('Введите числитель'))
    b = int(input('Введите знаменатель'))

    if b != 0:
        def my_func(a, b):
            return a / b


        print('результат деления:', my_func(a, b))
    else:
        print('Ошибка! На ноль делить нельзя!')

except ValueError:
    print('Неверный ввод')
