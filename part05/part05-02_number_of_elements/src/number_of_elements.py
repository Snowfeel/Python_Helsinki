# Write your solution here
def count_matching_elements(my_matrix: list, element: int):
    count = 0
    for i in my_matrix:
        for j in i:
            if element == j:
                count +=1
    return count