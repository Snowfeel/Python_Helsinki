# Write your solution here
def filter_incorrect():
    a = open('correct_numbers.csv' , 'w')
    a.close()

    with open("lottery_numbers.csv") as f:
        data = f.read()
        data = data.strip().split('\n')
        
        for i in data:
            part = i.strip().split(";")
            try:
                temp = part[0].split(' ')
                temp1 = int(temp[1])
                correct = True
                temp = part[1].strip().split(',')
                count = 0
                temp_set = []
                for j in temp:
                    if int(j) < 1 or int(j) >=39 or j in temp_set:
                        correct = False
                    temp_set.append(j)
                    count += 1
                    

                if correct and count == 7:
                    write_file(i)
            except ValueError:
                pass

def write_file(s):
    with open('correct_numbers.csv' , 'a') as w:
        w.write(s+'\n')