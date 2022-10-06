# Write your solution here
def anagrams(s1,s2):
    count = 0
    if len(s1) == len(s2):
        l = []
        l.extend(s2)
        for i in s1:
            if i in l:
                l.remove(i)
                count+=1

    if count == len(s1):
        return True
    else : return False

if __name__ == '__main__':
    print(anagrams("tame", "meta")) # True
    print(anagrams("tame", "mate")) # True
    print(anagrams("tame", "team")) # True
    print(anagrams("tabby", "batty")) # False
    print(anagrams("python", "java")) # False   