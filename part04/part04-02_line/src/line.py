# Write your solution here
def line(n,s):
    if s == "":
        print('*' * n)
    else:
        print(s[0] * n)
# You can test your function by calling it within the following block
if __name__ == "__main__":
    line(5, "")