# Write your solution here
def print_sudoku(sudoku: list):
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                print( '_' , end = ' ')
            else:
                print(sudoku[i][j], end = ' ')
            if (j+1)% 3 == 0:
                print('', end = ' ')
        print('')    
        if (i+1)% 3 == 0:
                print('')

def add_number(sudoku: list, row_no: int, column_no: int, number:int):
    sudoku[row_no][column_no] = number