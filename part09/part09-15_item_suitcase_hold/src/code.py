# Write your solution here:
class Item:

    def __init__(self,name:str,weight:int):
        self.__name = name
        self.__weight = weight

    def name(self):
        return self.__name

    def weight(self):
        return self.__weight

    def __str__(self) -> str:
        return f'{self.__name} ({self.__weight} kg)'

class Suitcase:

    def __init__(self,max_weight: int):
        self.__max_weight = max_weight
        self.__store = []

    def add_item(self,item:Item):
        weight = self.weight()
        if item.weight() + weight <= self.__max_weight:
              self.__store.append(item)

    def __str__(self):
        weight = self.weight()
        if len(self.__store) == 1:
            return f'{len(self.__store)} item ({weight} kg)'
        return f'{len(self.__store)} items ({weight} kg)'

    def print_items(self):
        for i in self.__store:
            print(i)

    def weight(self):
        total_weight = 0
        for i in self.__store:
            total_weight += i.weight()
        return total_weight

    def heaviest_item(self):
        if len(self.__store) == 0:
            return None
        weight = 0
        for i in self.__store:
            if i.weight() > weight:
                weight = i.weight()
                result = i
        return result

class CargoHold:
    def __init__(self,max_weight: int):
        self.__max_weight = max_weight
        self.__store = []

    def add_suitcase(self,suitcase:Suitcase):
        weight = self.weight()
        if suitcase.weight() + weight <= self.__max_weight:
              self.__store.append(suitcase)

    def weight(self):
        total_weight = 0
        for i in self.__store:
            total_weight += i.weight()
        return total_weight

    def __str__(self):
        weight = self.weight()
        if len(self.__store) == 1:
            return f'{len(self.__store)} suitcase, space for {self.__max_weight - weight} kg'
        return f'{len(self.__store)} suitcases, space for {self.__max_weight - weight} kg'

    def print_items(self):
        for i in self.__store:
            i.print_items()