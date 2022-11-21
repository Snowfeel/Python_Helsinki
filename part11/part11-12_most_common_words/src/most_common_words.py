# WRITE YOUR SOLUTION HERE:
import string

def most_common_words(filename: str, lower_limit: int):
    with open(filename) as f:
       content = f.read()
       content = content.translate(str.maketrans('', '', string.punctuation)).split()
       return {n : content.count(n) for n in content if content.count(n) >= lower_limit}