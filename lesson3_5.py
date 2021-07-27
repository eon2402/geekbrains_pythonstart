def summa():
    total_result = 0
    stop = False
    try:
        while stop == False:
            numbers = input('Введите числа, сумму которых хотите узнать через пробел, для выхода введите S').split()
            result = 0
            for digit in range(len(numbers)):
                if numbers[digit] == 's' or numbers[digit] == 'S':
                    stop = True
                    break
                else:
                    result = result + int(numbers[digit])
            total_result = total_result + result
            print('Промежуточная сумма введенных чисел = ', total_result)
        print('Итоговая сумма = ', total_result)
    except ValueError:
        print('Ошибка ввода')


summa()