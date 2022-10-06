# Write your solution here
n = int(input('How many items: '))
res = []
i = 1
while i <= n:
    res.append(int(input(f'Item {i}: ')))
    i += 1

print(res)