# Write your solution here
def column_correct(sudoku: list, column_no: int):
    for i in range(len(sudoku[column_no])):
        if sudoku[i][column_no] != 0:
            for j in range(len(sudoku[column_no])):
                if i != j:
                    if sudoku[i][column_no] == sudoku[j][column_no]:
                        return False

    return True
