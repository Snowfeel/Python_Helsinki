# Write your solution here
def find_words(search_term: str):
    with open('words.txt') as f:
        data = f.read()
        words = data.strip().split('\n')
    result = []
    if "." in search_term:
        for i in words:
            if len(i) != len(search_term):
                continue
            count = len(search_term)
            for j in range(len(search_term)):
                if search_term[j] == '.' or search_term[j] == i[j] :
                    count -= 1
            if count == 0:
                result.append(i)
    elif "*" in search_term:
        for i in words:
            if search_term[0] == '*':
                if i.endswith(search_term[1:]):
                    result.append(i)
            elif search_term[-1] == '*':
                if i.startswith(search_term[:-1]):
                    result.append(i)
    else:
        for i in words:
            if i == search_term:
                result.append(i)
    return result




                    
    