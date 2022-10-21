# Write your solution here
from string import ascii_letters, ascii_lowercase, ascii_uppercase


def change_case(orig_string: str):
    new_str =''
    for i in orig_string:
        if i in ascii_lowercase:
            new_str += i.upper()
        elif i in ascii_uppercase:
            new_str += i.lower()
        else:
            new_str += i
    return new_str

def split_in_half(orig_string: str):
    temp = len(orig_string)
    new_str1 = orig_string[:len(orig_string)//2]
    new_str2 = orig_string[len(orig_string)//2:]
    return new_str1,new_str2

def remove_special_characters(orig_string: str):
    new_str = ''
    allow_char = ascii_letters + ' 0123456789'
    for i in orig_string:
        if i in allow_char:
            new_str += i
    return new_str