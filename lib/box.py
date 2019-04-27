class Box:
    def __init__(self, values):
        """Create a new box

        Args:
            values (numpy.array): 2D array containing the values

        """

        self.values = values

    @property
    def size(self):
        """Get size of the box
            e.g. most sudokus are 9x9 and have a size of 3 (3**2 values in each
            box)

        Returns:
            size of the box

        """

        return len(self.values)

    @property
    def missing_values(self):
        """Get all values missing in the box

        Returns:
            array containing all missing values

        """

        all_values = list(range(1, self.size**2+1))
        return [
            val for val in all_values if val not in self.values and val != 0]

    @staticmethod
    def from_index(sudoku, row, col):
        """Create a new box using the indexes of a value of a sudoku

        Args:
            sudoku (Sudoku): the sudoku to take the box from
            row (int): the index of the row in which the value is present
            column (int): the index of the column in which the value is present

        Returns:
            new box object

        """

        size = sudoku.box_size
        irow, icol = row//size*size, col//size*size
        # get ending indexes of the box
        irow_end, icol_end = irow+size, icol+size

        return Box(sudoku.values[irow:irow_end, icol:icol_end])
