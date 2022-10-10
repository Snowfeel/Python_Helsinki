# write your solution here
from unittest import result


def read_matrix():
    with open('matrix.txt') as f:
        s = f.read()
        s = s.strip().split("\n")
        matrix = []
        for i in s:
            matrix.append(i.split(','))
        return matrix

def matrix_sum():
    matrix = read_matrix()
    result = 0
    for i in matrix:
        for j in i :
            result += int(j)
    return result

def matrix_max():
    matrix = read_matrix()
    result = 0
    for i in matrix:
        for j in i :
            if int(j) > result:
                result = int(j)
    return result

def row_sums():
    matrix = read_matrix()
    result = []
    for i in matrix:
        temp = 0
        for j in i :
            temp += int(j)
        result.append(temp)
    return result

