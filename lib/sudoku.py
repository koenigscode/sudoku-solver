import numpy as np


class Sudoku:

    def __init__(self, sudoku: np.array, box_size: int):
        if not self._has_valid_shape(sudoku.shape):
            raise ValueError("x size doesn't equal y size")

        if sudoku.shape[0] % box_size != 0:
            raise ValueError("invalid box size")

        self.sudoku = sudoku
        self.box_size = box_size

    @staticmethod
    def from_file(path):
        pass

    def is_valid_state(self):
        for row, col in np.ndindex(self.sudoku.shape):
            val = self.sudoku[row, col]  # current value
            # number of the value's occurences in the current row
            row_count = sum(self.sudoku[row] == val)
            # number of the value's occurences in the current column
            col_count = sum(self.sudoku[:, col] == val)

            return row_count == 1 and col_count == 1 and self._has_valid_values()

    def is_finished(self):
        return self.is_valid_state() and sum(self.sudoku.flatten() == 0) == 0

    def _has_valid_values(self):
        for val in self.sudoku.flatten():
            if val < 0 or val > self.box_size**2:  # invalid number
                return False

        return True

    def boxes(self):
        for row in range(0, self.sudoku.shape[0], self.box_size):
            for col in range(0, self.sudoku.shape[0], self.box_size):
                yield self.sudoku[row:row+self.box_size, col:col+self.box_size]

    @staticmethod
    def _has_valid_shape(shape):
        x_size, y_size = shape
        return x_size == y_size
