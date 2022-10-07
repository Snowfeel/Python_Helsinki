# Write your solution here
def dict_of_numbers():
    numbers = {}
    numbers[0] = 'zero'
    numbers[1] = 'one'
    numbers[2] = 'two'
    numbers[3] = 'three'
    numbers[4] = 'four'
    numbers[5] = 'five'
    numbers[6] = 'six'
    numbers[7] = 'seven'
    numbers[8] = 'eight'
    numbers[9] = 'nine'
    numbers[10] = 'ten'
    numbers[11] = 'eleven'
    numbers[12] = 'twelve'
    numbers[13] = 'thirteen'
    numbers[14] = 'fourteen'
    numbers[15] = 'fifteen'
    for i in range(16,20):
        numbers[i] = numbers[i-10]+'teen'

    numbers[18] = 'eighteen'
    numbers[20] = 'twenty'
    numbers[30] = 'thirty' 
    numbers[40] = 'forty' 
    numbers[50] = 'fifty' 
    numbers[60] = 'sixty'
    numbers[70] = 'seventy'
    numbers[80] = 'eighty'
    numbers[90] = 'ninety'

    for j in range(2,10):
        for i in range(j*10+1,j*10+10):
            numbers[i] = numbers[j*10]+'-'+numbers[i-j*10]

    return numbers
