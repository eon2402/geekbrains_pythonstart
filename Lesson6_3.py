class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'Wage': wage, 'Bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_full_income(self):
        return self._income['Wage'] + self._income['Bonus']


My_worker = Position('Александр', 'Соколов', 'Руководитель департамента', 200000, 110000)
print(My_worker.get_full_name(), 'получает доход в размере', My_worker.get_full_income(), 'руб. на позиции', My_worker.position)