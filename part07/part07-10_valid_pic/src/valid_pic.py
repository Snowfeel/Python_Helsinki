# Write your solution here
from datetime import datetime


def is_it_valid(pic: str):
    if len(pic)!= 11:
        return False
    
    #translate str to date
    day = int(pic[0]+pic[1])
    #translate str to month
    month = int(pic[2]+pic[3])
    #translate str to year
    if pic[6] == '+':
        year = int('18'+pic[4]+pic[5])
    elif pic[6] == '-':
        year = int('19'+pic[4]+pic[5])
    elif pic[6] == 'A':
        year = int('20'+pic[4]+pic[5])
    else:
        year = -1
    indentity = int(pic[0]+pic[1]+pic[2]+pic[3]+pic[4]+pic[5]+pic[7]+pic[8]+pic[9])
    control = pic[10]

    if check_date(year,month,day) and check_index(indentity,control):
        return True
    return False


def check_date(year,month,day):
    try:
        temp = datetime(year,month,day)
        return True
    except:
        return False

def check_index(indentity,control):
    #create index
    index = '0123456789ABCDEFHJKLMNPRSTUVWXY'
    indentity %= 31
    if index[indentity] == control:
        return True
    return False

        