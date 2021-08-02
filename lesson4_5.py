from functools import reduce
my_list = [el for el in range(100, 1001, 2)]
print(f'Исходный список {my_list}')

result = reduce(lambda x, y: x*y, my_list)

print(result)

