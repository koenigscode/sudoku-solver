import numpy as np
import time
from copy import deepcopy
import colorama
from colorama import Fore
from colorama import Style
from lib.box import Box

colorama.init()


class Sudoku:

    def __init__(self, values: np.array, box_size: int):
        if not self._is_valid_shape(values.shape):
            raise ValueError("x size doesn't equal y size")

        if values.shape[0] % box_size != 0:
            raise ValueError("invalid box size")

        self.values = values.astype("int")
        self.box_size = box_size

    def first_empty(self):
        for irow, row in enumerate(self.values):
            col_pos = np.where(row == 0)[0]
            if len(col_pos) > 0:
                return irow, np.where(row == 0)[0][0]

    def is_finished(self):
        return self.has_valid_state() and sum(self.values.flatten() == 0) == 0

    def has_valid_state(self):
        if not self.has_valid_values():
            return False

        for irow, row in enumerate(self.values):
            for icol in range(len(row)):
                curr_val = self.values[irow, icol]
                if curr_val != 0:
                    occurrences_in_row = sum(self.values[irow] == curr_val)
                    occurrences_in_col = sum(self.values[:, icol] == curr_val)

                    if occurrences_in_row > 1 or occurrences_in_col > 1:
                        return False
        return True

    def has_valid_values(self):
        for val in self.values.flatten():
            if val < 0 or val > self.box_size**2:  # invalid number
                return False

        return True

    def solve(self, extend=None):
        if type(extend) != list:
            return self._solve()

        res = ""
        start = time.time()
        solved = self.solve()
        end = time.time()

        if solved is None:
            return "Could not be solved"

        if "original" in extend:
        res += f"Original:\n{self}\nSolved:\n{solved}\n"
        else:
            res += solved.__repr__()

        if "timer" in extend:
            res += f"Took {end-start}ms"

        return res, solved

    def _solve(self):

        if not self.has_valid_state():
            return None
        if self.first_empty() is None:
            if self.is_finished():
                return self
            return None

        row, col = self.first_empty()
        first_empty_box = Box.from_index(self, row, col)

        for val in first_empty_box.missing_values:
            new_sudoku = deepcopy(self)
            new_sudoku.values[row][col] = val
            solved_sudoku = new_sudoku._solve()

            if solved_sudoku is not None:
                return solved_sudoku

    @staticmethod
    def _is_valid_shape(shape):
        x_size, y_size = shape
        return x_size == y_size

    def __repr__(self, highlight=None):
        s = ""
        row_delimiter = "-" * \
            ((len(self.values)+len(self.values)//self.box_size)*2 + 1) + "\n"

        for irow, row in enumerate(self.values):
            col = []
            if(irow % self.box_size == 0):
                s += row_delimiter
            for icol, val in enumerate(row):
                if(icol % self.box_size == 0):
                    col.append("|")
                if(highlight is not None and len(highlight) == 2 and irow == highlight[0] and icol == highlight[1]):
                    col.append(f"{Fore.RED}{val}{Style.RESET_ALL}")
                else:
                    col.append(str(val))
            s += f"{' '.join(col)} |\n"
        return s + row_delimiter
