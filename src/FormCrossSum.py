from z3 import *

# calculates the array of Horizontal cross sums from 
# the given complete Sudoku board
def Horizontal(FilledSudoku):
    HorizontalSums = [ [ FilledSudoku[i+(2*i)][j] 
                        + FilledSudoku[i+1+(2*i)][j] 
                        + FilledSudoku[i+2+(2*i)][j] 
                        for j in range (9)]
                        for i in range(3) ]
    print("\nHorizontal Cross Sums")
    pp (HorizontalSums)
    return HorizontalSums

# calculates the array of Vertical cross sums from 
# the given complete Sudoku board
def Vertical(FilledSudoku):
    VerticalSums = [ [ FilledSudoku[i][j+(2*j)] 
                      + FilledSudoku[i][j+1+(2*j)] 
                      + FilledSudoku[i][j+2+(2*j)] 
                      for j in range (3) ] 
                      for i in range(9) ]
    print("\nVertical Cross Sums")
    pp (VerticalSums)
    return VerticalSums