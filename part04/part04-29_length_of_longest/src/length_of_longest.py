# Write your solution here
def length_of_longest(ls):
    longest = 0
    for i in ls:
        if len(i) > longest:
            longest = len(i)
    return longest