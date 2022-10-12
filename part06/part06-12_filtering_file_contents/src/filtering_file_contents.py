# Write your solution here
def write_file(file,data):
    with open(file, 'a') as f:
        f.write(data+"\n")

def filter_solutions():
    open('correct.csv', 'w').close()
    open('incorrect.csv', 'w').close()

    with open("solutions.csv") as f:
        data = f.read()
        data = data.strip().split('\n')
        solution = {}
        for i in data:
            parts = i.strip().split(';')
            if '+' in parts[1]:
                check = parts[1].strip().split("+")
                if int(check[0])+int(check[1]) == int(parts[2]):
                    write_file('correct.csv',i)
                else:
                    write_file('incorrect.csv',i)
            if '-' in parts[1]:
                check = parts[1].strip().split("-")
                if int(check[0])-int(check[1]) == int(parts[2]):
                    write_file('correct.csv',i)
                else:
                    write_file('incorrect.csv',i)
