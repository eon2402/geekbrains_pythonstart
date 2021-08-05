my_dict = {}
with open('subjects') as file:
    for line in file:
        lesson, *other = line.split()
        hours = [int(digit.rstrip('(л)(пр)(лаб),')) for digit in other if digit]
        my_dict.update({lesson: sum(hours)})
print(my_dict)