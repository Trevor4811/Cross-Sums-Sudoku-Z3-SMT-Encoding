from z3 import *
import time

# Returns the solution to the given cross sums puzzle, or that no solution exists
def CrossSumSudoku(Horizontal, Vertical):
    
    # 9x9 matrix of integer variables
    X = [ [ Int("x_%s_%s" % (i, j)) for j in range(9) ]
         for i in range(9) ]
    print("\nSudoku board matrix")
    for i in range(9):
        print(X[:][i])

    # each cell contains a value in the range [1, 9]
    cellValue = [ And(1 <= X[i][j], X[i][j] <= 9)
                 for i in range(9) for j in range(9) ]
    print("\nPossible cell values condition")
    print(cellValue)
    
    # each row contains a digit at most once
    rows = [ Distinct(X[i]) for i in range(9) ]
    print("\nDistinct value rule for each row")
    print(rows[0])
    print('...')
    print(rows[8])

    # each column contains a digit at most once
    cols = [ Distinct([ X[i][j] for i in range(9) ])
            for j in range(9) ]
    print("\nDistinct value rule for each column")
    print(cols[0])
    print('...')
    print(cols[8])
    
    # each 3x3 square contains a digit at most once
    square = [ Distinct([ X[3*i0 + i][3*j0 + j]
                         for i in range(3) for j in range(3) ])
                         for i0 in range(3) for j0 in range(3) ]
    print("\nDistinct value rule for each 3x3 square")
    print(square[0])
    print('...')
    print(square[8])
    
    # The horizontal cross sum is equal to the sum of the specific 3x1 column
    horizSum = [ Horizontal[i][j] == X[i+(2*i)][j] + X[i+1+(2*i)][j] + X[i+2+(2*i)][j] 
                for i in range(3) for j in range (9)]
    print("\nHorizontal cross sum conditions")
    print (horizSum)
    
    # The Vertical cross sum is equal to the sum of the specific 1x3 row
    vertSum = [ Vertical[i][j] == X[i][j+(2*j)] + X[i][j+1+(2*j)] + X[i][j+2+(2*j)] 
               for i in range(9) for j in range (3) ]
    print("\nVertical cross sum conditions")
    print (vertSum)
    
    # Combining standard sudoku conditions
    sudoku = cellValue + rows + cols + square
    # print (sudoku)
    
    # Combining cross sum sudoku conditions
    crossSumValues = horizSum + vertSum
    # print (crossSumValues)
    
    # Starting the timer for solve time
    start = time.time();
    
    # Creating SMT solver and adding conditions
    s = Solver()
    s.add(sudoku)
    s.push()
    s.add(crossSumValues)
    
    # is the puzzle satisfiable
    print ("\nPuzzle Satisfiability: " + str(s.check()))
    
    # If satisfiable, model, evaluate, and print solution
    if s.check() == sat:
        m = s.model()
        print("\nValues found for every cell")
        print(m)
        r = [ [ m.evaluate(X[i][j]) for j in range(9) ]
              for i in range(9) ]
        print("\nCross Sum Sudoku solution found")
        pp(r)
        
        # End time to solve with solution
        end = time.time();
        print("\nSolving time: " + str(round(end-start, 2)) + " seconds")
        return r
    else:
        print("\nNo solution found")
        
        # End time to solve when no solution
        end = time.time();
        print("\nRuntime: " + str(round(end-start, 2)) + " seconds")
        return "No solution found"
    
