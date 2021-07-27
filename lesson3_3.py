def my_func(a,b,c):
    my_list = [a, b, c]
    my_list.sort(reverse=True)
    result = my_list[0]+my_list[1]
    print(result)


my_func(10,5,50)