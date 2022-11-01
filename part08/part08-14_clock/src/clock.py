# Write your solution here:
class Clock:
    def __init__(self,hours:int,min:int,sec:int):
        self.seconds = sec
        self.minutes = min
        self.hours = hours
    
    def tick(self):
        self.seconds += 1
        if self.seconds == 60:
            self.seconds = 0
            self.minutes += 1
            if self.minutes == 60:
                self.minutes = 0
                self.hours += 1
                if self.hours == 24:
                    self.hours = 0

    def __str__(self):
        return f'{self.hours:02}:{self.minutes:02}:{self.seconds:02}'

    def set(self,hour,min):
        self.hours = hour
        self.minutes = min
        self.seconds = 0