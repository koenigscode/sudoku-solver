import numpy as np
import time
from copy import deepcopy
import colorama
from lib.box import Box

colorama.init()


class Sudoku:

    def __init__(self, values: np.array, box_size: int):
        """Create a new Sudoku object.

        Args:
            values (numpy.array): array to create the sudoku from
                empty fields should be set to 0
            box_size (int): box size (length) of the sudoku
                most sudokus are 9x9 and therefore have a boxsize of 3

        """

        if not self._is_valid_shape(values.shape):
            raise ValueError("x size doesn't equal y size")

        if not self._is_valid_box_size(values.shape, box_size):
            raise ValueError("invalid box size")

        self.values = values.astype("int")  # convert into int array
        self.box_size = box_size

    def first_empty(self):
        """Get the position of the first empty value (first zero) in the sudoku

        Returns:
            tuple containing index of row and index of column
            or None if there is no empty value

        """

        for irow, row in enumerate(self.values):
            col_pos = np.where(row == 0)[0]
            if len(col_pos) > 0:
                return irow, np.where(row == 0)[0][0]

    def is_finished(self):
        """Check if the sudoku is finished and valid

        Returns:
            true if sudoku has valid state and there are no empty values
                (zeros) left

        """

        return self.has_valid_state() and sum(self.values.flatten() == 0) == 0

    def has_valid_state(self):
        """Check if the sudoku has a valid state, so every value only occurs
            once in a row and column
            empty values (zeros) are allowed

        Returns:
            True if all values occur in their row and column only once,
            otherwise False

        """

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
        """Check if all of the sudoku's values are valid
            zero is counted as a valid value

        Returns:
            True if all values are within the sudoku's range, otherwise False

        """

        for val in self.values.flatten():
            if val < 0 or val > self.box_size**2:  # invalid number
                return False

        return True

    def solve(self, extend=None):
        """Solve the sudoku
        Args:
            extended (list): return the sudoku as well as a formatted string
                contains different options in form of a string within the list:
                "original": show the original and solved sudoku;
                    also label the original and saved one
                "timer": show the time taken to solve the sudoku

        Returns:
            Not using "extend" option:
                solved sudoku 
            Using "extend" option:
                visual representation and solved sudoku 

        """

        if type(extend) != list:
            return self._solve()

        res = ""
        start = time.time()
        solved = self.solve()
        end = time.time()

        if solved is None:
            return "Could not be solved", None

        if "original" in extend:
            res += f"Original:\n{self}\nSolved:\n{solved}\n"
        else:
            res += solved.__repr__()

        if "timer" in extend:
            res += f"Took {end-start}ms"

        return res, solved

    def _solve(self):
        """Internal solve method to find the solution using recursion

        Returns:
            Sudoku if it could be solved
            otherwise None

        """

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
        """Check for a valid shape (width equals length)

        Args:
            shape (tuple): x and y size

        Returns:
            True if width equals length
            otherwise false

        """

        x_size, y_size = shape
        return x_size == y_size

    def _is_valid_box_size(self, shape, box_size):
        """Check if box size is valid

        Returns:
            True if box size is valid
            otherwise False

        """

        return shape[0] % box_size == 0

    def __repr__(self, highlight=None):
        """Visual representation of the sudoku

        Args:
            highlight (tuple): row index and column index indicating the value
                to be highlighted
                useful for debugging

        Returns:
            visual representation of the sudoku

        """

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
                    col.append(
                        f"{colorama.Fore.RED}{val}{colorama.Style.RESET_ALL}")
                else:
                    col.append(str(val))
            s += f"{' '.join(col)} |\n"
        return s + row_delimiter
