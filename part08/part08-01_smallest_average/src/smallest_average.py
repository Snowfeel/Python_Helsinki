# Write your solution here
def smallest_average(person1: dict, person2: dict, person3: dict):
    s = [person1,person2,person3]
    smol = 99
    result = ''
    for i in s:
        temp = (i['result1']+i['result2']+i['result3'])/3
        if temp < smol:
            result = i
            smol = temp
    return result