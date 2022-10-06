# Write your solution here
def shortest(ls):
    s = '                                                           '
    for i in ls:
        if len(i) < len(s):
            s = i
    return s 