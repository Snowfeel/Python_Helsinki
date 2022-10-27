# Write your solution here
# Remember the import statement
from datetime import date

def list_years(dates: list):
    result = []
    for i in dates:
        result.append(i.year)
    return sorted(result)