# Write your solution here:
class Series:
    def __init__(self,name:str,seasons:int,genres:list):
        self.title = name
        self.seasons = seasons
        self.genres = genres
        self.rating = 0
        self.count = 0

    def __str__(self):
        if self.count == 0:
            temp = 'no ratings'
        else:
            temp = f'{self.count} ratings, average {self.rating/self.count:0.1f} points'
        return f'{self.title} ({self.seasons} seasons)\ngenres: {", ".join(self.genres)}\n' + temp
    
    def rate(self,amount :int):
        self.rating += amount
        self.count += 1

    
def minimum_grade(rating: float, series_list: list):
    result = []
    for i in series_list:
        if i.rating > rating:
            result.append(i)
    return result

def includes_genre(genre: str, series_list: list):
    result = []
    for i in series_list:
        for j in i.genres:
            if j == genre:
                result.append(i)
    return result