# Write your solution here
def read_input(s, lower_n, upper_n):
    while True:
        try:
            i=int(input(s))
            if lower_n <= i <= upper_n:
                return i
        except ValueError:
            pass
        print(f'You must type in an integer between {lower_n} and {upper_n}')

