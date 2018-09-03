import numpy


class Square:
    def __init__(self, number):
        middle_column_index = number // 2

        def initial_matrix():
            matrix = numpy.zeros((number, number), dtype=numpy.int_)
            matrix[0, middle_column_index] = 1
            return matrix

        self.matrix = initial_matrix()
        self.current_row = 0
        self.current_column = middle_column_index

    def step_once(self):
        (next_row, next_column) = self._next_cell_()
        self.matrix[next_row, next_column] = self.matrix[self.current_row, self.current_column] + 1
        (self.current_row, self.current_column) = (next_row, next_column)

    def step_to_finish(self):
        while 0 in self.matrix:
            self.step_once()

    def is_magic_square(self):
        row_sums = self.matrix.sum(axis=1)
        column_sums = self.matrix.sum(axis=0)
        diagonal_sum = self.matrix.trace()
        return self._is_array_of_identical_values_(row_sums) and \
               self._is_array_of_identical_values_(column_sums) and \
               row_sums[0] == diagonal_sum and \
               column_sums[0] == diagonal_sum

    def to_string(self):
        return '\n'.join('\t'.join('%d' % column for column in row) for row in self.matrix)

    def _is_array_of_identical_values_(self, array):
        return array.min() == array.max()

    def _move_up_row_(self, row):
        has_gone_off_top = row - 1 < 0
        last_column_index = self.matrix.shape[0] - 1

        if has_gone_off_top:
            return last_column_index
        else:
            return row - 1

    def _move_right_column_(self, column):
        has_gone_off_right = column + 1 > self.matrix.shape[1] - 1

        if has_gone_off_right:
            return 0
        else:
            return column + 1

    def _move_down_row_(self, row):
        has_gone_off_bottom = row + 1 > self.matrix.shape[0] - 1

        if has_gone_off_bottom:
            return 0
        else:
            return row + 1

    def _move_diagonally_(self):
        next_row = self._move_up_row_(self.current_row)
        next_column = self._move_right_column_(self.current_column)
        return next_row, next_column

    def _move_down_(self):
        next_row = self._move_down_row_(self.current_row)
        next_column = self.current_column
        return next_row, next_column

    def _next_cell_(self):
        (next_row, next_column) = self._move_diagonally_()
        cell_is_occupied = self.matrix[next_row, next_column] != 0
        if cell_is_occupied:
            (next_row, next_column) = self._move_down_()
        return next_row, next_column
