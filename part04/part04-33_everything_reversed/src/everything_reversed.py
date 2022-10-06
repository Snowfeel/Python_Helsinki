# Write your solution here
def everything_reversed(ls):
    l = []
    for i in range(len(ls)-1,-1,-1):
        l.append(ls[i][::-1])
    return l