import numpy as np
from lib.sudoku import Sudoku

if __name__ == "__main__":
    # load example sudoku from file as a numpy array
    input = np.loadtxt("examples/example1.txt")
    # create sudoku from array and set box size to 3
    sudoku = Sudoku(input, 3)

    # solve sudoku and print it, as well as original and time taken
    print(sudoku.solve(extend=["original", "timer"])[0])
