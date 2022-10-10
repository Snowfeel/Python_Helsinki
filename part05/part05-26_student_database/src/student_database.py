# Write your solution here
from gettext import find


def add_student(students : dict, name : str):
    if name not in students:
        students[name] = []

def print_student(students : dict, name : str):
    if name not in students:
        print(f'{name}: no such person in the database')
    elif len(students[name]) > 0:
        print(f'{name}:')
        print(f' {len(students[name])} completed courses:')
        for i in students[name]:
            print(' ',i[0],i[1]) 
        print(f' average grade {avg_grade(students,name)}')
    else :
        print(name + ':')
        print(' no completed courses')

def avg_grade(students: dict, name: str):
    grade = 0
    for i in students[name]:
            grade += i[1] 
    return grade/len(students[name])

def add_course(students : dict, name : str , course : tuple):
    if course[1] > 0:
        if len(students[name]) == 0 :
            students[name].append(course)
        elif course[0] not in students[name][0]:
            students[name].append(course)
        else:
            for i in students[name]:
                if i[0] == course[0]:
                    if course[1] > i[1]:
                        students[name].remove(i)
                        students[name].append(course)
            
def summary(students : dict):
    print('students',len(students))
    most_course = 0
    most_course_name = '' 
    most_avg = 0
    most_avg_name =''
    for i in students:
        if len(students[i]) > most_course:
            most_course = len(students[i])
            most_course_name = i
        temp = avg_grade(students,i)
        if temp > most_avg:
            most_avg = temp
            most_avg_name = i
    print('most courses completed',most_course,most_course_name)
    print('best average grade',most_avg,most_avg_name)
