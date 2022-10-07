# Write your solution here

phone_book ={}
while True:
    s = input('command (1 search, 2 add, 3 quit): ')
    if s == '3':
        break
    elif s == '2':
        name = input('name: ')
        number = input('number: ')
        phone_book[name] = number
        print('ok!')
    elif s == '1':
        name = input('name: ')
        if name in phone_book:
            print(phone_book[name])
        else:
            print('no number')

print('quitting...')