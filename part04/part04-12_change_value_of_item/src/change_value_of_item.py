# Write your solution here
n = [1, 2, 3, 4, 5]

while True:
    index = int(input('Index: '))
    if index == -1:
        break
    inp = int(input('New value: ')) 
    n[index] = inp
    print(n)


