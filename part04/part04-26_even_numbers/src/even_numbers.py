# Write your solution here
def even_numbers(ln):   
    l = []
    for i in ln:
        if i % 2 == 0:
            l.append(i)
    return l
