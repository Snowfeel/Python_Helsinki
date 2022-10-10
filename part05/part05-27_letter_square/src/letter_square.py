# Write your solution here
def draw(alpha :tuple, n :int):
    result = []
    for i in range(n):
        for j, s in enumerate(result):
            result[j] = alpha[i] + s + alpha[i]
        result.append((2*i+1)*alpha[i])

        if i != 0:
            result.insert(0, (2*i+1)*alpha[i])
        
    for line in result:
        print(line)

n = int(input("Layers: "))
alpha = ('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')
draw(alpha,n)
