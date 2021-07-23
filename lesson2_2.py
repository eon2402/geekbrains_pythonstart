my_list = list(input('введите список значений'))
print(my_list)
i = 0
while i * 2 < len(my_list) - 1:
    my_list[i*2],my_list[i*2+1] = my_list[i*2+1], my_list[i*2]
    i += 1

print(my_list)