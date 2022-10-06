# Write your solution here
def no_shouting(s):
    l = []
    for i in s:
        if i.isupper() == False:
            l.append(i)

    return l