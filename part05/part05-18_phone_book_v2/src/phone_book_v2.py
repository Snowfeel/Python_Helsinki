# Write your solution here
def add_number(person):
    name = input('name: ')
    number = input('number: ')
    if name not in person:
        person[name] = []
    person[name].append(number)
    print('ok!')

def search_number(person):
    name = input('name: ')
    if name in person:
        for number in person[name]:
            print(number)
    else:
        print('no number')


person ={}
while True:
    s = input('command (1 search, 2 add, 3 quit): ')
    if s == '3':
        break
    elif s == '2':
        add_number(person)
    elif s == '1':
        search_number(person)

print('quitting...')