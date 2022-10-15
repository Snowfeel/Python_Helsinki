# Write your solution here
from random import randint
from string import ascii_lowercase


def generate_password(n : int):
    result = ''
    for i in range(n):
        result += ascii_lowercase[randint(0,25)]
    return result
