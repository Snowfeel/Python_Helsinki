# Write your solution here

def find_movies(database: list, search_term: str):
    movies = []
    for i in database:
        if  search_term.upper() in i['name'].upper():
            movies.append(i)
    return movies