# Write your solution here
from cmath import exp
from random import randint
from unittest import result


def lottery_numbers(amount: int, lower: int, upper: int):
    result = []
    for i in range(amount):
        n = randint(lower,upper)
        try:
            while n in result:
                n = randint(lower,upper)
        except:
            pass
        result.append(n)
    result.sort()
    return result