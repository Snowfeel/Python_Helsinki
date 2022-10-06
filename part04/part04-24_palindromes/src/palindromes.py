# Write your solution here
def palindromes(s):
    count = 0
    for i in range(int(len(s)/2)):
        if s[i]==s[-1-i]:
            count +=1
    if count == int(len(s)/2):
        print(f'{s} is a palindrome!')
        return True
    else : 
        print('that wasn\'t a palindrome')
        return False
# Note, that at this time the main program should not be written inside


while True:
    s = input('Please type in a palindrome: ')
    if palindromes(s):
        break
# block!
