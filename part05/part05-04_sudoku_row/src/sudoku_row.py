# Write your solution here
def row_correct(sudoku: list, row_no: int):
    for i in range(len(sudoku[row_no])):
        if sudoku[row_no][i] != 0:
            for j in range(len(sudoku[row_no])):
                if i != j:
                    if sudoku[row_no][i] == sudoku[row_no][j]:
                        return False

    return True