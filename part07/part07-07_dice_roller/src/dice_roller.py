# Write your solution here
from random import randint


def roll(die: str):
    a = [3,3,3,3,3,6]
    b = [2,2,2,5,5,5]
    c = [1,4,4,4,4,4]
    if die == 'A':
        return a[randint(0,5)] 
    elif die == 'B':
        return b[randint(0,5)] 
    elif die == 'C':
        return c[randint(0,5)] 

def play(die1: str, die2: str, times: int):
    first_won = 0
    second_won = 0
    tie = 0
    for i in range(times):
        first = roll(die1)
        second = roll(die2)
        if first > second:
            first_won += 1
        elif first < second:
            second_won += 1
        else:
            tie += 1

    return first_won,second_won,tie 
