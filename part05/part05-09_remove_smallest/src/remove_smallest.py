# Write your solution here
def remove_smallest(numbers: list):
    s = numbers[:]
    s.sort()
    numbers.remove(s[0])