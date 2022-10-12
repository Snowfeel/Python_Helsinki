# tee ratkaisu tänne
# tee ratkaisu tänne
# write your solution here
import math

def read_file(file :str):
    with open(file) as f:
        students = {}
        s = f.read()
        s = s.strip().split("\n")
        header = s.pop(0)
        header = header.strip().split(";")
        for i in s:
            part = i.split(";")
            temp = []
            for j in range(1,len(part)):
                temp.append(part[j])
            students[part[0]] = temp    
    return students

def summary_score(x):
    point = {}
    for i in x:
        res = 0
        for j in x[i]:
            res += int(j)
        point[i] = res
    return point


def grade(exercise_point,exam_point):
    student_grade = {}
    for i in exercise_point:
        student_grade[i] = exam_point[i] + math.floor(exercise_point[i]/4)
        if student_grade[i] < 15:
            student_grade[i] = 0
        elif student_grade[i] < 18:
            student_grade[i] = 1
        elif student_grade[i] < 21:
            student_grade[i] = 2
        elif student_grade[i] < 24:
            student_grade[i] = 3
        elif student_grade[i] < 28:
            student_grade[i] = 4
        else :
            student_grade[i] = 5
    return (student_grade)



def print_statistic(student,exam_point,exercise_point,student_grade,course):
    with open("results.txt", 'w') as f:
        with open(course) as c_data:
            data = c_data.read()
            parts = data.strip().split("\n")
            s = f"{parts[0][6:]}, {parts[1][15:]} credits"
            f.write(s+'\n')
            f.write('=' * len(s) + "\n")
            f.write(f"{'name':30}exec_nbr  exec_pts. exm_pts.  tot_pts.  grade\n")
            for i in student:
                f.write(f"{student[i][0]+' '+student[i][1]:30}{exercise_point[i]:<10}{math.floor(exercise_point[i]/4):<10}{exam_point[i]:<10}{math.floor(exercise_point[i]/4)+exam_point[i]:<10}{student_grade[i]:<10}\n")
    with open('results.csv' , "w") as f:
        for i in student:
            f.write(f'{i};{student[i][0]+" "+student[i][1]};{student_grade[i]}\n')



if True:
    # this is never executed
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
    exam_point_data = input('Exam points: ')
    course = input('Course information: ')
else:
    # hard-coded input
    student_info = "students1.csv"
    exercise_data = "exercises1.csv"
    exam_point_data = "exam_points1.csv"
    course = "course1.txt"


student = read_file(student_info)
exercise = read_file(exercise_data)
exam = read_file(exam_point_data)
exam_point = summary_score(exam)
exercise_point = summary_score(exercise)
student_grade = grade(exercise_point,exam_point)
print_statistic(student,exam_point,exercise_point,student_grade,course)



