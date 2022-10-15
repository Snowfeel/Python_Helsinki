# Write your solution here
from string import ascii_letters, punctuation

def separate_characters(my_string: str):
    letter = ''
    pun = ''
    other = ''
    for i in my_string:
        if i in ascii_letters:
            letter += i
        elif i in punctuation:
            pun += i
        else:
            other += i
    return letter,pun,other