# Write your solution here:
class SuperHero:
    def __init__(self, name: str, superpowers: str):
        self.name = name
        self.superpowers = superpowers

    def __str__(self):
        return f'{self.name}, superpowers: {self.superpowers}'

class SuperGroup:
    def __init__(self,name:str,location:str):
        self._name = name
        self._location = location
        self._members = []
    
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,new_name:str):
        self._name = new_name
    @property
    def location(self):
        return self._location
    @location.setter
    def location(self,new_location):
        self._location = new_location

    def add_member(self,hero: SuperHero):
        self._members.append(hero)
    
    def print_group(self):
        print(self._name + ', ' + self._location)
        print('Members:')
        for i in self._members:
            print(i)