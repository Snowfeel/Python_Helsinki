# Write your solution here!
class  NumberStats:
    def __init__(self):
        self.numbers = 0
        self.sum = 0
        self.even_sum = 0
        self.odd_sum = 0

    def add_number(self, number:int):
        self.numbers += 1
        self.sum += number
        if number % 2 == 0:
            self.even_sum += number
        else:
            self.odd_sum += number

    def count_numbers(self):
        return self.numbers
    
    def get_sum (self):
        return self.sum
    
    def average(self):
        if self.numbers != 0:
            return self.sum/self.numbers
        return 0

print('Please type in integer numbers:')
data = NumberStats()
while(True):
    s = int(input())
    if s == -1:
        break
    data.add_number(s)

print('Sum of numbers:',data.get_sum())
print('Mean of numbers:',data.average())
print('Sum of even numbers:',data.even_sum)
print('Sum of odd numbers:',data.odd_sum)
    
