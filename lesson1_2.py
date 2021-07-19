time = int(input('Введите количество секунд'))

hour = time // 3600
min = (time - hour * 3600) // 60
sec = time - (hour * 3600 + min * 60)
print(hour, min, sec, sep=':')
print(f"Время чч:мм:сс  {hour}:{min}:{sec}")
