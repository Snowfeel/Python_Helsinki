# Copy here code of line function from previous exercise and use it in your solution
def line(n,s):
    if s == "":
        print('*' * n)
    else:
        print(s[0] * n)

def triangle(size,character):
    i = 1
    while i <= size:
        line(i, character)
        i +=1

def square( width,height, character):
    # You should call function line here with proper parameters
    i = 0
    while i < height:
        line(width, character)
        i += 1

def shape(nt,st ,ns,ss):
    triangle(nt,st)
    square(nt,ns,ss)


# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 2, "o")