# WRITE YOUR SOLUTION HERE:
class LotteryNumbers:
    def __init__(self,week:int,numbers:list):
        self.week = week
        self.numbers = numbers

    def number_of_hits(self,numbers: list):
        return len([s for s in numbers if s in self.numbers])

    def hits_in_place(self,numbers: list):
        return [s if s in self.numbers else -1 for s in numbers]