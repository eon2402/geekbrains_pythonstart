x = float(input('Введите действительное положительное число'))
y = int(input('Введите целое отрицательное число'))

if x > 0 and y < 0:
    print(pow(x, y))

# в виде my_func:

    def my_func(x, y):
        return x**y
    print(my_func(x, y))

# с циклом:
    def my_func2(x, y):
        i = 0
        result = 1
        while i > y:
            result /= x
            i -= 1
        print(result)
    (my_func2(x, y))


else: print('Неверный ввод')