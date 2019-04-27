# Sudoku-Solver

## How to solve a sudoku

Just instantiate a new sudoku by passing the Sudoku's constructor a 2D numpy
array and the size of the boxes.

Most sudokus are 9x9 and each box contains 9 values, so the boxes have a size of
3 (3x3 = 9 values).

Empty values (which should later be solved by the solve() method) should be
zeros, as shown in the example files.

## How it works

The empty values of the sudoku get replaced with possible values step-by-step.

At first, it replaces the first occurring zero with a value still missing in the
box, then the sudoku checks if its state is still valid, meaning there are
no duplicate values in all the rows and columns.

If the current state is valid, replace the next occurring zero with a possible value. This is continued until the sudoku's either solved or there is not
solution.
