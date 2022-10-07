# Write your solution here
import string


def histogram(s: string):
    word = {}
    for i in s:
        if i not in word:
            word[i] = 0
        
        word[i] += 1
    for key,value in word.items():
        print(key,'*' * value)