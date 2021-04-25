# Cross-Sums-Sudoku-Z3-SMT-Encoding

## Cross-Sum Sudoku:

Cross-Sum Sudoku is a game that combines the ruleset of Sudoku and Cross-Sum Kakuro. What this means is that numbers must fit into a 9x9 grid such that each 3x3 section contains the numbers 1-9 exactly once, each row contains numbers 1-9 exactly once, and each column must contain the numbers 1-9 exactly once. Also, each row and column of each smaller 3x3 grid has an assigned sum that the three numbers which make up that column or row must add up to. Due to the nature of this variation, there are no numbers placed in the 9x9 grid at the start as with normal Sudoku; the only clues provided are the sums of each row and column.
  
## Steps to Install:
- Install [Python](https://www.python.org/downloads/release/python-394/)
- Install [Eclipse IDE](https://www.eclipse.org/downloads/packages/)
- Install [PyDev](https://www.pydev.org/download.html) as a plugin in a new eclipse workspace
- In the PyDev workspace of Eclipse go to windows > Preferences > PyDev > Interpreters > Python Interpreters
  - Click New and add your previous Python install as an interpreter.
  - Apply
  - Then in the same window click manage with pip
  - Use pip to install the “z3-solver”

## Using CrossSumSudoku:

The CrossSumSudoku module contains one function that takes in the horizontal and vertical cross sums of a puzzle in the form of two arrays as seen in the example below, and returns an array of the Suduko answer or a string that there was "No solution found"

```Python
import CrossSumSudoku

Solution = CrossSumSudoku.CrossSumSudoku(
    [[19, 12, 14, 19, 9, 17, 17, 14, 14],
     [6, 17, 22, 13, 15, 17, 16, 16, 13],
     [20, 16, 9, 13, 21, 11, 12, 15, 18]],
    [[15, 9, 21],
     [12, 19, 14],
     [18, 17, 10],
     [13, 19, 13],
     [18, 11, 16],
     [14, 15, 16],
     [16, 14, 15],
     [10, 17, 18],
     [19, 14, 12]])
```

## Using FormCrossSum:

The FormCrossSum module contains two functions that both take in a completed standard sudoku board in the form of an array with the Horizontal function returning the horizontal cross sum array for the given board and Vertical function returning the vertical cross sum array for the given board, as seen in the examples below.

```Python
import FormCrossSum

Horizontal = FormCrossSum.Horizontal(
    [[6, 2, 7, 5, 3, 1, 9, 8, 4], 
     [8, 1, 3, 6, 4, 9, 2, 5, 7], 
     [5, 9, 4, 8, 2, 7, 6, 1, 3], 
     [1, 7, 5, 4, 9, 6, 8, 3, 2], 
     [3, 6, 9, 2, 1, 8, 7, 4, 5], 
     [2, 4, 8, 7, 5, 3, 1, 9, 6], 
     [7, 3, 6, 1, 8, 5, 4, 2, 9], 
     [4, 5, 1, 9, 6, 2, 3, 7, 8], 
     [9, 8, 2, 3, 7, 4, 5, 6, 1]])
            
Vertical = FormCrossSum.Vertical( 
    [[6, 2, 7, 5, 3, 1, 9, 8, 4], 
     [8, 1, 3, 6, 4, 9, 2, 5, 7], 
     [5, 9, 4, 8, 2, 7, 6, 1, 3], 
     [1, 7, 5, 4, 9, 6, 8, 3, 2], 
     [3, 6, 9, 2, 1, 8, 7, 4, 5], 
     [2, 4, 8, 7, 5, 3, 1, 9, 6], 
     [7, 3, 6, 1, 8, 5, 4, 2, 9], 
     [4, 5, 1, 9, 6, 2, 3, 7, 8], 
     [9, 8, 2, 3, 7, 4, 5, 6, 1]])
```

## Using FormCrossSum:

The Examples module can be run to test both the CrossSumSudoku and FormCrossSum modules. The ExamplesOutput text file is an output from running the FormCrossSum file. It is important to note that if a given set of cross sums has multiple solutions, this solver may produce different but still correct solutions.
