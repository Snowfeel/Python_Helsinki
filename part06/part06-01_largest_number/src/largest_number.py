# write your solution here
def largest():
    with open("numbers.txt") as f:
        s = f.read()
        largest = 0
        s1 = s.strip().split("\n")
        for i in s1:
            if int(i) > largest:
                largest = int(i)
        return(largest)

if __name__ == "__main__":
    largest()
