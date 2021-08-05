import json

my_list = []
dict_profitable = {}
dict_damaged = {}
with open('file7') as file:
    average_profit = []
    for line in file.readlines():
        name, form, gain, damage = line.split()
        profit = int(gain) - int(damage)
        if profit > 0:
            average_profit.append(profit)
            dict_profitable.update({name: profit})
        else:
            dict_damaged.update({name: profit})
    print(dict_profitable)
    print(dict_damaged)

    my_list.append(dict_profitable)
    my_list.append(dict_damaged)
    my_list.append({"average profit": '{:.2f}'.format(sum(average_profit)/len(average_profit))})

with open('file7.json','w') as file:
    json.dump(my_list, file)