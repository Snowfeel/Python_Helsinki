# Write your solution here
def row_sums(my_matrix: list):
    for i in my_matrix:
        temp = 0
        for j in i:
            temp += j
        i.append(temp)