# Write your solution here
def invert(dictionary: dict):
    temp = {}
    for i,v in dictionary.items():
        temp[v] = i
    for v,i in temp.items():
        dictionary.pop(i)
        dictionary[v] = i
