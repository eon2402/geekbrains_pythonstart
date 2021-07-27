def my_func(name, surname, birth, city, email, phone):
    print(f"Данные о пользователе: {name} {surname} {birth} г.р., из города {city}, контакты: {email} {phone}")


my_func(input('Как вас зовут?'), input('Ваша фамилия?'), input('В каком году вы родились?'),
        input('В каком городе живете?'), input('Ваш email?'), input('Ваш номер телефона?'))