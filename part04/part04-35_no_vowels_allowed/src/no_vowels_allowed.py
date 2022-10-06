# Write your solution here
def no_vowels(s):
    l = []
    l.extend(s)
    nl = []
    for i in range(len(l)):
        if l[i] != 'a' and l[i] != 'e' and l[i] != 'i' and l[i] != 'o' and l[i] != 'u':
            nl.append(l[i])
    s = ''
    for i in nl:
        s += i
    return s