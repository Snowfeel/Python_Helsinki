# Write your solution here
def all_the_longest(ls):
    longest = 0
    for i in ls:
        if len(i) > longest:
            longest = len(i)
    l = []
    for i in ls:
        if len(i) == longest:
            l.append(i)
    return l 