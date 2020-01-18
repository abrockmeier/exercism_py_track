class Matrix:
    def __init__(self, matrix_string):
        self.matrix_string = matrix_string
        self._rows =  [[int(item) for item in row.split(' ')] for row in matrix_string.split('\n')]

    def row(self, index):
        return self._rows[index - 1]

    def column(self, index):
        return [column[index - 1] for column in self._rows]
