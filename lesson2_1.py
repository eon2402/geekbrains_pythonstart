my_list = [3, 4.5, None, 'date', [2, 3], {2: 's', 3: 'f'}, (2, 5), {'d','a'}]
list2 = [2, '2']
my_list.extend(list2)
print(my_list)
for element in my_list:
    print(element, ' - ', type(element))