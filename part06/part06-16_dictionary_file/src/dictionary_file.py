# Write your solution here
def read_file():
    with open('dictionary.txt') as f_read:
        data = f_read.read()
        data = data.strip().split("\n")
        dictionary = {}
        if data != ['']:
            for i in data:
                part = i.strip().split(';')
                dictionary[part[0]] = part[1]
    return dictionary
        
while True:
    print('1 - Add word, 2 - Search, 3 - Quit')
    s = input('Function: ')
    if s == '3':
        print('Bye!')
        break
    elif s == '1':
        word_f = input('The word in Finnish: ')
        word_e = input('The word in English: ')
        translator = f"{word_f};{word_e}\n"
        f = open('dictionary.txt' , 'a')
        f.write(translator)
        print('Dictionary entry added')
        f.close()
    elif s == '2':
        word = input('Search term: ')
        dictionary = read_file()
        for i in dictionary:
            if word in i or word in dictionary[i]:
                print(f"{i} - {dictionary[i]}")
            