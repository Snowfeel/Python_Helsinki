# Write your solution here
def read_file():
    with open("diary.txt") as f:
        s = f.read()
        print(s)

def write_file(s):
    with open('diary.txt' , 'a') as f:
        f.write(s + '\n')
    
while True:
    print('1 - add an entry, 2 - read entries, 0 - quit')
    fun = input('Function: ')
    if fun == '0':
        break
    elif fun == '1':
        s = input('Diary entry: ')
        write_file(s)
        print('Diary saved')
    elif fun == '2':
        print('Entries:')
        read_file()

print('Bye now!')

