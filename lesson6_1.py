from itertools import cycle
from time import sleep


class TrafficLight:
    all_colors = ('Красный', 'Желтый', 'Зеленый')
    time = (7, 2, 5)

    def __init__(self, color):
        self.__color = color

    def running(self):
        my_cycle = cycle(self.all_colors)
        for each_color in my_cycle:
            if self.__color == each_color:
                print(f'Загорелся {self.__color} свет!')
                sleep(self.time[self.all_colors.index(self.__color)])
                self.__color = next(my_cycle)


my_light = TrafficLight('Красный')
my_light.running()

