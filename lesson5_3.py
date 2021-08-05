with open('employees') as file:
    my_list = file.readlines()
    print(my_list)
    my_list_20 = []
    sum = 0
    for el in my_list:
        employee, salary = el.split('-')
        sum += int(salary)
        if int(salary) < 20000:
            my_list_20.append(employee)
    print('Оклад менее 20 000 руб имеют сотрудники: ', ', '.join(my_list_20))

    print(f'Средняя заработная плата в фирме: {sum/len(my_list)}')