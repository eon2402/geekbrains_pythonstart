class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('автомобиль', self.name, self.color, 'цвета начал движение со скоростью', self.speed, 'км/ч')

    def stop(self):
        print('автомобиль', self.name, self.color, 'цвета остановился')

    def turn(self, direction):
        print('автомобиль', self.name, self.color, 'цвета повернул ', direction)

    def show_speed(self):
        print('Текущая скорость атомобиля', self.name, ' - ', self.speed, 'км/ч')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print('Снизьте скорость!')
        else:
            Car.show_speed(self)


class SportCar(Car):
    def __init__(self, speed, color, name):
        Car.__init__(self, speed, color, name, is_police=False)


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print('Снизьте скорость!')
        else:
            Car.show_speed(self)


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        Car.__init__(self, speed, color, name, is_police=True)


my_town_car = TownCar(80, 'Синего', 'volvo', False)
my_town_car.go()
my_town_car.turn('направо')
my_town_car.turn('налево')
my_town_car.show_speed()
my_town_car.stop()

my_sport_car = SportCar(230, 'желтого', 'audi')
my_sport_car.go()
my_sport_car.turn('направо')
my_sport_car.turn('налево')
my_sport_car.show_speed()
my_sport_car.stop()

my_Police_car = PoliceCar(120, 'черного', 'bmw')
my_Police_car.go()
my_Police_car.turn('направо')
my_Police_car.show_speed()
my_Police_car.stop()

my_Work_car = WorkCar(40, 'белого', 'МАЗ', False)
my_Work_car.go()
my_Work_car.turn('в обратную сторону')
my_Work_car.show_speed()
