# Write your solution here
from decimal import ROUND_DOWN
import urllib.request
import json
import ssl # add this library to your import section
import math

def retrieve_all():
    # add the following line to the beginning of all your functions
    context = ssl._create_unverified_context()
    # the rest of your function
    request = urllib.request.urlopen('https://studies.cs.helsinki.fi/stats-mock/api/courses')
    data = json.load(request)
    result = []
    for i in data:
        if i['enabled']:
            sum = 0 
            for j in i['exercises']:
                sum += j
            result.append((i['fullName'],i['name'],i['year'],sum))
    return result

def retrieve_course(course_name: str):
    context = ssl._create_unverified_context()
    # the rest of your function
    url = f'https://studies.cs.helsinki.fi/stats-mock/api/courses/{course_name}/stats'
    request = urllib.request.urlopen(url)
    data = json.load(request)
    result = {}
    result['weeks'] = len(data)
    students = 0
    hours = 0
    exercises = 0
    for i in data:
        if data[i]['students'] > students:
            students = data[i]['students']
        hours += data[i]['hour_total']
        exercises += data[i]['exercise_total']
    result['students'] = students
    result['hours'] = hours
    result['hours_average'] = math.floor(hours/students)
    result['exercises'] =exercises
    result['exercises_average'] = math.floor(exercises/students)
    return result