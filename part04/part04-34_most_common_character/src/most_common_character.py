# Write your solution here
def most_common_character(s):
    n = [0] * len(s)
    for i in range (len(s)):
        for j in range (len(s)):
            if s[i] == s[j]:
                n[i] += 1    
    large = 0
    for i in range(len(n)):
        if n[i] > large:
            large = n[i]
            index = i 
        
    return s[index]