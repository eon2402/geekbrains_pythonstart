class Cell:
    def __init__(self, num):
        try:
            if num <= 0:
                raise ValueError('Введите число больше 0')
            self.num = int(num)
        except TypeError:
            print('проверьте количество ячеек')
        except ValueError:
            print('проверьте количество ячеек')

    def __add__(self, other):
        return Cell(self.num + other.num)

    def __sub__(self, other):
        if self.num - other.num > 0:
            return Cell(self.num - other.num)
        else:
            print('Вычитание невозможно')

    def __mul__(self, other):
        return Cell(self.num * other.num)

    def __truediv__(self, other):
        return Cell(self.num // other.num)

    def make_order(self, size):
        row = ''
        for i in range(self.num // size):
            row += f'{"o" * size} \n'
        row += f'{"o" * (self.num % size)}'
        return row

cell_1 = Cell(17)
cell_2 = Cell(8)
print('Изобразим структуру клеток')
print('первая клетка размером: ', cell_1.num)
print(cell_1.make_order(5))
print()
print('вторая клетка размером: ', cell_2.num)
print(cell_2.make_order(4))

cell_3 = cell_1 * cell_2
print('третья клетка - умножение первых двух: ', cell_3.num)
print(cell_3.make_order(20))

cell_4 = cell_1 / cell_2
print('четвертая клетка - деление первых двух: ', cell_4.num)
print(cell_4.make_order(2))

cell_5 = cell_1 + cell_2
print('пятая клетка - сложение первых двух: ', cell_5.num)
print(cell_5.make_order(7))

cell_6 = cell_1 - cell_2
print('шестая клетка - вычитание первых двух: ', cell_6.num)
print(cell_6.make_order(3))
