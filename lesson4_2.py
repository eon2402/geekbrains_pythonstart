def list_gen ():
    my_list = [200, 99, 44, 41, 467, 3, 32, 55, 333, 56]
    print('исходный список:', my_list)

    new_list = [my_list[i] for i in range (1, len(my_list)) if my_list[i] > my_list[i -1]]
    print('новый список:', new_list)
list_gen()