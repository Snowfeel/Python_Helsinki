# Write your solution here
import csv
from datetime import datetime, timedelta

def start_time():
    with open('start_times.csv') as f :
        start_time = {}
        for i in csv.reader(f,delimiter=(';')):
            start_time[i[0]] = datetime.strptime(i[1],'%H:%M')
    return start_time

def end_time():
    with open('submissions.csv') as sub:
        last_sub_time = {}
        for i in csv.reader(sub,delimiter=";"):
            try:
                temp = datetime.strptime(i[3],'%H:%M')
                if last_sub_time[i[0]] < temp:
                    last_sub_time[i[0]] = temp
            except:
                last_sub_time[i[0]] = datetime.strptime(i[3],'%H:%M')
    return last_sub_time

def final_points():
    with open('submissions.csv') as sub:
        all_score = {}
        start = start_time()
        for i in start:
            all_score[i] = [0]*8
        for i in csv.reader(sub,delimiter=";"):
            temp = datetime.strptime(i[3],'%H:%M')
            if temp - start[i[0]] <= timedelta(hours=3):
                if int(all_score[i[0]][int(i[1])-1]) < int(i[2]):
                     all_score[i[0]][int(i[1])-1] = i[2]
    result = {}
    for i in all_score:
        sum = 0
        for j in all_score[i]:
            sum += int(j)
        result[i] = sum
    return result            

def cheaters():
    start = start_time()
    last_sub_time = end_time()    
    cheater = []
    for i in start:
        if last_sub_time[i] - start[i] > timedelta(hours=3):
            cheater.append(i)
    return cheater