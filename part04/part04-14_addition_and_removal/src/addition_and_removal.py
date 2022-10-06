# Write your solution here
res = []
i = 1
while True:
    print(f'The list is now {res}')
    inp = input('a(d)d, (r)emove or e(x)it: ')
    if inp == 'x':
        break
    if inp =='d':
        res.append(i)
        i+=1
    elif inp == 'r':
        res.pop()
        i-=1

print('Bye!')