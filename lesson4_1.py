from sys import argv

script_name, hours, wages, bonus = argv

salary_calc = (int(hours) * int(wages) + int(bonus))

print('Название скрипта:', script_name)
print('Введите количество рабочих часов:', hours)
print('Введите стоимость часа:', wages)
print('Размер премии:', bonus)
print('Размер выплаты составит:', salary_calc)