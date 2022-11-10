# tee ratkaisusi tänne
class All_Course:
    def __init__(self) -> None:
        self.__course = {}
        self.__credits = 0
        self.__grade = [0]*5

    def add_course(self,course:str,grade:int,credits:int):
        if course not in self.all_course():
            self.__course[course] = Course(course,grade,credits)
            self.__credits += credits
        self.__course[course].set_grade(grade)

    def all_course(self):
        return self.__course

    def course(self,course:str):
        if course not in self.all_course():
            print("no entry for this course")
            return
        print(self.__course[course])

    def mean(self):
        grade = 0
        self.__grade = [0] * 5
        for i in self.__course:
            grade += self.__course[i].grade()
            self.__grade[self.__course[i].grade()-1] += 1
        return grade/len(self.__course)

    def statistic(self):
        print(f"{len(self.__course)} completed courses, a total of {self.__credits} credits")
        print(f"mean {self.mean():.1f}")
        print("grade distribution")
        i = 4
        while(i!=-1):
            print(f"{i+1}: {'x' * self.__grade[i]}")
            i -= 1


class Course:
    def __init__(self,course:str,grade:int,credits:int):
        self.__course = course
        self.__grade = grade
        self.__credits = credits

    def set_grade(self,grade:int):
        if grade > self.__grade:
            self.__grade = grade

    def grade(self):
        return self.__grade
    
    def credits(self):
        return self.__credits

    def __str__(self) -> str:
        return f"{self.__course} ({self.__credits} cr) grade {self.__grade}"


class Interface:
    def __init__(self) -> None:
        self.__course = All_Course()

    def run(self):
        print("1 add course")
        print("2 get course data")
        print("3 statistics")
        print("0 exit")
        while (True):
            command = input("command: ")
            if command == '0':
                break
            if command == '1':
                course = input("course: ")
                grade = int(input("grade: "))
                credit = int(input("credits: "))
                self.__course.add_course(course,grade,credit)
            elif command == '2':
                course = input("course: ")
                self.__course.course(course)
            elif command == '3':
                self.__course.statistic()



app = Interface()
app.run()