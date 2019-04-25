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

    @staticmethod
    def _has_valid_shape(shape):
        x_size, y_size = shape
        return x_size == y_size
