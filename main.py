import numpy as np
from lib.sudoku import Sudoku

input = np.loadtxt("examples/example2.txt")
sudoku = Sudoku(input, 3)

print(sudoku.solve(extend=["original", "timer"])[0])
