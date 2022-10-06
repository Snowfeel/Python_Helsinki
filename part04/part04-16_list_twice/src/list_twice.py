# Write your solution here
res =[]
while True:
    s = int(input('New item: '))
    if s == 0:
        break
    res.append(s)
    print(f'The list now: {res}')
    print(f'The list in order: {sorted(res)}')

print('Bye!')
