# Write your solution here
def older_people(people: list, year: int):
    older = []
    for i in people:
        if i[1] < year:
            older.append(i[0])
    return older