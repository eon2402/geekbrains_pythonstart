income = int(input('Введите размер выручки фирмы в рублях'))
costs = int(input('Введите размер издержек фирмы в рублях'))

if income > costs:
    profit = income - costs
    print(f"Ваша фирма получает прибыль в размере {profit} рублей")
    rent = profit / income * 100
    print(f"Рентабельность бизнеса составляет {rent:.2f} %")
    staff = int(input('Введите количество сотрудников фирмы, чтобы узнать прибыль фирмы в расчете на одного '
                             'сотрудника'))
    profit_staff = profit / staff
    print(f"Прибыль в расчете на одного сотрудника составляет {profit_staff:.2f} рублей")

else:
    loss = costs - income
    print(f"Ваша фирма работает в убыток суммой {loss} рублей")