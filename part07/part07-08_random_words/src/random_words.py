# Write your solution here
from random import randint


def words(n: int, beginning: str):
    with open("words.txt") as f:
        words = f.read()
        words = words.strip().split("\n")
        s= []
        result = []
        for i in words:
            if i.startswith(beginning):
                s.append(i)
        for i in range(n):
            result.append(s.pop(randint(0,len(s)-1)))

        return result
