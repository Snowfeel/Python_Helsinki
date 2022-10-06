# Write your solution here
res = []
while True:
    s = input('Word: ')
    if s in res:
        break
    res.append(s)

print(f'You typed in {len(res)} different words')