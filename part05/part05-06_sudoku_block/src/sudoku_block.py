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