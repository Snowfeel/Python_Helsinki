# WRITE YOUR SOLUTION HERE:
class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def __str__(self):
        return self.name

class Room:
    def __init__(self):
        self.people = []

    def add(self,person: Person):
        self.people.append(person)
    
    def is_empty(self):
        if len(self.people) ==0:
            return True
        return False

    def print_contents(self):
        for i in self.people:
            print(i.name + f' ({i.height} cm)')

    def shortest(self):
        short = ''
        height = 999
        if len(self.people) !=0:
            for i in self.people:
                if i.height < height:
                    height = i.height
                    short = i
            return short
        return None

    def remove_shortest(self):
        if len(self.people) !=0:
            x = self.shortest()
            self.people.remove(x)
            return x
        return None