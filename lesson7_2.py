from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, args):
        self.args = args

    @abstractmethod
    def get_consumption(self):
        pass


class Coat(Clothes):
    def __init__(self, args):
        super().__init__(args)
        print(f'Плащ имеет размер: {self.args}')

    @property
    def get_consumption(self):
        return round(self.args / 6.5 + 0.5, 2)


class Suit(Clothes):
    def __init__(self, args):
        super().__init__(args)
        print(f'Костюм имеет рост: {self.args}')

    @property
    def get_consumption(self):
        return round(self.args * 2 + 0.3, 2)


my_coat = Coat(44)
my_suit = Suit(1.85)

print(f'суммарный расход ткани на производство Плаща: {my_coat.get_consumption}')
print(f'суммарный расход ткани на производство Костюма: {my_suit.get_consumption}')
print(f'суммарный общий расход ткани: {my_coat.get_consumption + my_suit.get_consumption}')