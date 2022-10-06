# Write your solution here
def distinct_numbers(ln):
    l = []
    for i in ln:
        if i not in l:
            l.append(i)
    x = sorted(l)
    return x
            