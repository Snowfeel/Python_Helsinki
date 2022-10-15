# Write your solution here
from operator import contains
from random import randint
from string import ascii_lowercase, punctuation
from tokenize import Special


def generate_strong_password(n : int,contain_number :bool, contain_special :bool):
    random = []
    random.extend(ascii_lowercase)
    number = ['0','1','2','3','4','5','6','7','8','9']
    special_char = ['!','?','=','+','-','(',')','#']
    if contain_number:
        random.extend(number)
    if contain_special:
        random.extend(special_char)
    result = []
    for i in range(n):
        s = randint(0,len(random)-1)
        result.append(random[s])
    special = True
    num = True
    alpha = True
    for i in result:
        if i not in special_char and contain_special:
            special = False
        if i not in number and contain_number:
            num =False
        if len(result) > 2 and i not in ascii_lowercase:
            alpha = False
            
    
    if not special:
        result[0] = special_char[randint(0,len(special_char)-1)]
    if not num:
        result[1] = number[randint(0,9)]    
    if not alpha:
        result[2] = ascii_lowercase[randint(0,25)]
        
    results = ''
    for i in result:
        results += i

    return results
