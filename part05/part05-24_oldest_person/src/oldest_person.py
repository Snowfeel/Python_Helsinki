# Write your solution here
def oldest_person(people: list):
    min = 9999
    index = 0
    for i in range(len(people)):
        if people[i][1] < min:
            min = people[i][1]
            index = i
    return people[index][0]