# Write your solution here
def block_correct(sudoku: list, row_no: int, column_no: int):
    for i in range(row_no,row_no+3):
        for j in range(column_no,column_no+3):
            if sudoku[i][j] != 0:
                for k in range(row_no,row_no+3):
                    for l in range(column_no,column_no+3):
                        if sudoku[k][l] != 0:
                            if not(i == k and j == l):
                                if sudoku[i][j] == sudoku[k][l]:
                                    return False
                    
    return True

def row_correct(sudoku: list, row_no: int):
    for i in range(len(sudoku[row_no])):
        if sudoku[row_no][i] != 0:
            for j in range(len(sudoku[row_no])):
                if i != j:
                    if sudoku[row_no][i] == sudoku[row_no][j]:
                        return False

    return True

def column_correct(sudoku: list, column_no: int):
    for i in range(len(sudoku[column_no])):
        if sudoku[i][column_no] != 0:
            for j in range(len(sudoku[column_no])):
                if i != j:
                    if sudoku[i][column_no] == sudoku[j][column_no]:
                        return False

    return True

def sudoku_grid_correct(sudoku: list):
    for i in range(9):
        if not row_correct(sudoku,i):
            return False
        if not column_correct(sudoku,i):
            return False
    
    loop = [0,3,6]
    for i in loop:
        for j in loop:
            if not block_correct(sudoku,i,j):
                return False
    
    return True

