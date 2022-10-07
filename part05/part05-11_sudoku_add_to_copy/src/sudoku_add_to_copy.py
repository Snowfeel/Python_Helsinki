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

def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int):
    copy_sudoku = []
    for i in sudoku:
        copy_sudoku.append(i.copy())
        
    print(copy_sudoku)
    add_number(copy_sudoku,row_no,column_no,number)
    return copy_sudoku

