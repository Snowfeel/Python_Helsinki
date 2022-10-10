# write your solution here
def read_fruits():
    with open('fruits.csv') as f:
        s = f.read()
        parts = s.strip().split("\n")
        dic = {}
        for i in parts:
            temp = i.split(";")
            dic[temp[0]] = float(temp[1])
        return dic
