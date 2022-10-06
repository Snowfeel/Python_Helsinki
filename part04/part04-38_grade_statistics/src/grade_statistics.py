# Write your solution here
def cal_point(s):
    return int(s[1]/10) + s[0]

def grade(point,student_grade):
    i = cal_point(point)
    if point[0] < 10:
        student_grade[0] += 1
    elif 0 <= i <= 14:
        student_grade[0] += 1
    elif 15 <= i <= 17:
        student_grade[1] += 1
    elif 18 <= i <= 20:
        student_grade[2] += 1    
    elif 21 <= i <= 23:
        student_grade[3] += 1
    elif 24 <= i <= 27:
        student_grade[4] += 1
    elif 28 <= i <= 30:
        student_grade[5] += 1
    return student_grade

def percent(student_grade):
    pas = 0
    for i in range(1,6):
        pas += student_grade[i]
    return pas/(student_grade[0]+pas)*100

def print_grade(student_grade):
    for i in range(5,-1,-1):
        print(f'{i}:', end =' ')
        s = ''
        for j in range(student_grade[i]):
            s += '*'
        print(s)


all_score = 0
count = 0
student_grade = [0] * 6
while True:
    s = input('Exam points and exercises completed: ')
    if s =='':
        break
    point = s.strip().split(' ')
    point[0] = int(point[0])
    point[1] = int(point[1])
    student_grade = grade(point,student_grade)
    all_score += cal_point(point)
    count += 1
    
print('Statistics:')
print(f'Points average: {all_score/count:0.1f}')
print(f'Pass percentage: {percent(student_grade):0.1f}')
print('Grade distribution:')
print_grade(student_grade)