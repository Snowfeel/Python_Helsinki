# Write your solution here
import json

def print_persons(filename: str):
    with open(filename) as f:
        data = f.read()
    person = json.loads(data)
    for i in person:
        s =  i['name'] + ' ' + str(i['age']) + ' years ('
        for j in i['hobbies']:
            s +=  j
            if j != i['hobbies'][-1]:
                s+= ', '
        s+= ')'    
        print(s)