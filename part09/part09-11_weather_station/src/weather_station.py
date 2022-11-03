# WRITE YOUR SOLUTION HERE:
class WeatherStation:
    def __init__(self,name:str):
        self.__name = name
        self.__observate = []

    def add_observation(self,observation: str):
        self.__observate.append(observation)

    def latest_observation(self):
        if len(self.__observate) != 0:
            return self.__observate[-1]
        return ''

    def number_of_observations(self):
        return len(self.__observate)
    
    def __str__(self):
        return f'{self.__name}, {len(self.__observate)} observations'
