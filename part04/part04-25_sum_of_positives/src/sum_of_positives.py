# Write your solution here
def sum_of_positives(ln):
    res = 0
    for i in ln:
        if i > 0:
            res += i
    return res

