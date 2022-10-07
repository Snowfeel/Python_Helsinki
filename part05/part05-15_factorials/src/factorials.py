# Write your solution here
def factorials(n: int):
    k= {}
    for i in range(1,n+1):
        if i == 1:
            k[i] =1
        else:
            k[i] = k[i-1] * i
    return k