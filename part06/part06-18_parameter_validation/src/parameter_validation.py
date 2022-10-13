# Write your solution here
def new_person(name: str, age: int):
    if len(name) == 0 or len(name) > 40 or len(name) < 2 or age < 0 or age >150:
        raise ValueError
    part = name.strip().split(" ")
    if len(part) < 2:
        raise ValueError
    return name,age