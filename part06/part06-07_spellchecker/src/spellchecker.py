# write your solution here
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

for i in parts:
    if i.lower() not in dic:
        result += "*" + i + "* "
    else:
        result += i + " "


print(result)

        
    