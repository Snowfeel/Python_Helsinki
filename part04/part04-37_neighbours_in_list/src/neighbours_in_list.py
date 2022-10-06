# Write your solution here
def longest_series_of_neighbours(ln):
    x = 9999
    count = 1
    ma = 0
    for i in ln:
        if abs(i-x) == 1:
            count+=1
            if count > ma:
                ma = count
        else :
            count = 1
        x = i
    return ma