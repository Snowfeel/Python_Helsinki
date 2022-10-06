# Write your solution here
def list_of_stars(ln):
    for i in ln:
        s = ''
        for j in range(i):
            s+='*'
        print(s)

if __name__ == "__main__":
    list_of_stars([3, 7, 1, 1, 2])
    