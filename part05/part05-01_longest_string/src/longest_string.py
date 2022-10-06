# Write your solution here
def longest(strings: list):
    s = ''
    for i in strings:
        if len(i) > len(s):
            s = i
    return s

if __name__ == "__main__":
    strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
    print(longest(strings))