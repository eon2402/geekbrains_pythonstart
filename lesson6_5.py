class Stationery:
    title = ['карандаш', 'ручка', 'маркер']

    def draw(self):
        print('Запуск отрисовки:')


class Pencil(Stationery):
    def draw(self):
        print(Stationery.title[0])
        print('отрисовка карандашом')


class Pen(Stationery):
    def draw(self):
        print(Stationery.title[1])
        print('отрисовка ручкой')


class Handle(Stationery):
    def draw(self):
        print(Stationery.title[2])
        print('отрисовка маркером')


stat = Stationery()
stat.draw()
pencil = Pencil()
pen = Pen()
handle = Handle()
pen.draw()
pencil.draw()
handle.draw()

