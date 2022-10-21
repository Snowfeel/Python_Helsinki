# Write your solution here
from traceback import print_last


def cheaters():
    with open('start_times.csv') as f :
        data = f.read()
        data = data.strip().split('\n')
        start_time = {}
        cheater =[]
        for i in data:
            part = i.strip().split(';')
            time = part[1].strip().split(':')
            start_time[part[0]] = (int(time[0]),int(time[1]))

        with open('submissions.csv') as sub:
            data = sub.read()
            data = data.strip().split('\n')
            last_sub_time = {}
            for i in data:
                part = part = i.strip().split(';')
                time = part[3].strip().split(':')
                try:
                    if last_sub_time[part[0]][0] < int(time[0]) or (int(time[0]) == last_sub_time[part[0]][0] and int(time[1]) > last_sub_time[part[0]][1]):
                        last_sub_time[part[0]] = (int(time[0]),int(time[1]))
                except:
                    last_sub_time[part[0]] = (int(time[0]),int(time[1]))
            print(last_sub_time)
        for i in start_time:
            start = start_time[i][0] * 60 + start_time[i][1]
            end = last_sub_time[i][0] * 60 + last_sub_time[i][1]
            print(i,start,end)
            if end - start > 180:
                cheater.append(i)
    return cheater