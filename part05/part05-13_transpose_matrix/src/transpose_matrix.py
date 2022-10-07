# Write your solution here
def transpose(matrix: list):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i != j and i < j:
                temp = matrix[j][i]
                matrix[j][i] = matrix[i][j]
                matrix[i][j] = temp


