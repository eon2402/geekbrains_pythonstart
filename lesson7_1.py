class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix


    def __str__(self):
        my_str = '\n'
        for row in self.matrix:
            for el in row:
                my_str += f'{el:>5}'
            my_str += '\n'
        return my_str


    def __add__(self, other):
        add = []
        if len(self.matrix) == len(other.matrix):
            for i in range(len(self.matrix)):
                if len(self.matrix[i]) != len(other.matrix[i]):
                    print('Проверьте соразмерность матриц')
                    return None
                row = []
                for j in range(len(self.matrix[i])):
                    row.append(self.matrix[i][j]+other.matrix[i][j])
                add.append(row)
            return Matrix(add)
        else:
            print('Проверьте соразмерность матриц')
            return None


mtrx_1 = Matrix([[1, 2, 3], [3, 2, 1], [2, 1, 3]])
mtrx_2 = Matrix([[0, 2, 1], [0, 2, 2], [0, 2, 3]])
print(mtrx_1)
print(mtrx_2)
print('результат =', '\n', mtrx_1 + mtrx_2)