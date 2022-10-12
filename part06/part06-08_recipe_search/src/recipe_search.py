# Write your solution here
from copy import copy


def read_file(filename: str):
    with open(filename) as f:
        recipe = f.read()
        menu = recipe.strip().split("\n\n")
        recipes = {}
        book = []
        for i in menu:
            part = i.strip().split("\n")
            name = part[0]
            time = part[1]
            recipes['name'] = name
            recipes['time'] = int(time)
            ingredients = []
            for j in range(2,len(part)):
                ingredients.append(part[j])
            recipes['ingredients'] = ingredients
            cop = recipes.copy()
            book.append(cop)
        return book

def search_by_name(filename: str, word: str):
    book = read_file(filename)
    result = []
    for i in book:
        if word.lower() in i['name'].lower():
            result.append(i['name'])
    return result

def search_by_time(filename: str, prep_time: int):
    book = read_file(filename)
    result = []
    for i in book:
        if prep_time >= i['time']:
            result.append(i['name'] + ', preparation time ' + str(i['time']) + ' min')
    return result

def search_by_ingredient(filename: str, ingredient: str):
    book = read_file(filename)
    result = []
    for i in book:
        if ingredient in i['ingredients']:
            result.append(i['name'] + ', preparation time ' + str(i['time']) + ' min')
    return result
