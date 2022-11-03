# WRITE YOUR SOLUTION HERE:
class Car:
    def __init__(self):
        self.__petrol  = 0
        self.__distant = 0

    def fill_up(self):
        self.__petrol = 60

    def drive(self,km:int):
        if self.__petrol > km:
            self.__petrol -= km
            self.__distant += km
        else:
            self.__distant += self.__petrol
            self.__petrol = 0
            
    def __str__(self) -> str:
        return f'Car: odometer reading {self.__distant} km, petrol remaining {self.__petrol} litres'