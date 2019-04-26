class Box:
    def __init__(self, values):
        self.values = values

    @property
    def size(self):
        return len(self.values)

    @property
    def missing_values(self):
        all_values = list(range(1, self.size**2+1))
        return [val for val in all_values if val not in self.values and val != 0]

    @staticmethod
    def from_index(sudoku, row, col):
        size = sudoku.box_size
        irow, icol = row//size, col//size
        row_start, col_start = irow*size, icol*size
        row_end, col_end = irow*size+size, icol*size+size

        return Box(sudoku.values[row_start:row_end, col_start:col_end])
