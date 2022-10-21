# write your solution here
from difflib import get_close_matches


if True:
    s = input("Write text: ")
else:
    s = "We use ptython to make a spell checker"

parts = s.strip().split(" ")
dic = []
with open("wordlist.txt") as f:
    data = f.read()
    word = data.strip().split("\n")
    for i in word:
        dic.append(i)

result = ''
suggestion = {}

for i in parts:
    if i.lower() not in dic:
        result += "*" + i + "* "
        suggestion[i.lower()] = get_close_matches(i.lower(),dic)
    else:
        result += i + " "
print(result)
print('suggestions:')
for i in suggestion:
    s = f'{i}:' 
    for j in suggestion[i]:
        s += ' ' + j 
        if j != suggestion[i][-1]:
            s += ','
    print(s)

        



