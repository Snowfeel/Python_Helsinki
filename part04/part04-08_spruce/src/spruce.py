# Write your solution here
def line(space,dot):
    print(" " * space + '*' * dot)

def spruce(n):
    print('a spruce!')
    i= 1
    j = n-1

    while i <= n*2:
        line(j,i)
        j-=1
        i+=2

    line(n-1,1)


# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(3)