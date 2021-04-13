import CrossSumSudoku
import FormCrossSum
import time

#################
### Example 1 ###
#################
print ("Example 1")

Board1  =  ((2, 4, 8, 6, 3, 9, 5, 1, 7),
            (3, 7, 9, 1, 8, 5, 2, 6, 4),
            (5, 1, 6, 4, 7, 2, 9, 8, 3),
            (8, 2, 7, 5, 4, 3, 1, 9, 6),
            (1, 9, 3, 2, 6, 8, 7, 4, 5),
            (4, 6, 5, 7, 9, 1, 8, 3, 2),
            (9, 8, 4, 3, 2, 7, 6, 5, 1),
            (6, 5, 2, 9, 1, 4, 3, 7, 8),
            (7, 3, 1, 8, 5, 6, 4, 2, 9))

# Horizontal cross sums of integer variables
Horizontal1 = FormCrossSum.Horizontal(Board1)
              
# Vertical cross sums of integer variables
Vertical1 = FormCrossSum.Vertical(Board1)

Solution1 = CrossSumSudoku.CrossSumSudoku(Horizontal1, Vertical1)

time.sleep(1)


# Example with multiple solutions, leading to the input and 
# output boards being different
#################
### Example 2 ###
#################
print ("\nExample 2 - Board has multiple solutions so output is different")

Board2  =  ((1,2,6,4,3,7,9,5,8),
            (8,9,5,6,2,1,4,7,3),
            (3,7,4,9,8,5,1,2,6),
            (4,5,7,1,9,3,8,6,2),
            (9,8,3,2,4,6,5,1,7),
            (6,1,2,5,7,8,3,9,4),
            (2,6,9,3,1,4,7,8,5),
            (5,4,8,7,6,9,2,3,1),
            (7,3,1,8,5,2,6,4,9))

# Horizontal cross sums of integer variables
Horizontal2 = FormCrossSum.Horizontal(Board2)
              
# Vertical cross sums of integer variables
Vertical2 = FormCrossSum.Vertical(Board2)

Solution2 = CrossSumSudoku.CrossSumSudoku(Horizontal2, Vertical2)


time.sleep(1)


# Example of invalid input board so no solution
#################
### Example 3 ###
#################
print ("\nExample 3 - Invalid board given")

Board3  =  ((9,2,6,4,3,7,9,5,8),
            (8,9,5,6,2,1,4,7,3),
            (3,7,4,9,8,5,1,2,6),
            (4,5,7,1,9,3,8,6,2),
            (9,8,3,2,4,6,5,1,7),
            (6,1,2,5,7,8,3,9,4),
            (2,6,9,3,1,4,7,8,5),
            (5,4,8,7,6,9,2,3,1),
            (7,3,1,8,5,2,6,4,9))

# Horizontal cross sums of integer variables
Horizontal3 = FormCrossSum.Horizontal(Board3)
              
# Vertical cross sums of integer variables
Vertical3 = FormCrossSum.Vertical(Board3)

Solution3 = CrossSumSudoku.CrossSumSudoku(Horizontal3, Vertical3)







