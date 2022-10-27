# Write your solution here
from string import ascii_letters, ascii_uppercase, digits


def run(command :list):
    vari = {}
    result = []
    jump_location = {}
    for i in ascii_uppercase:
        vari[i] = 0

    for i in range(len(command)):
        jump_location[command[i][:-1]] = i

    i = 0
    while i < len(command):
        part = command[i].strip().split(' ')
        if part[0] == 'PRINT':
            if part[1] in digits:
                result.append(int(part[1]))
            else :
                result.append(vari[part[1]])

        elif part[0] == 'MOV':
            if part[2] in ascii_letters:
                temp = vari[part[2]]
                vari[part[1]] = temp
            else:
                vari[part[1]] = int(part[2])

        elif part[0] == 'ADD':
            if vari_or_digit(part[2]):
                vari[part[1]] += vari[part[2]]
            else :
                vari[part[1]] += int(part[2])

        elif part[0] == 'SUB':
            if vari_or_digit(part[2]):
                vari[part[1]] -= vari[part[2]]
            else :
                vari[part[1]] -= int(part[2])

        elif part[0] == 'MUL':
            if vari_or_digit(part[2]):
                vari[part[1]] *= vari[part[2]]
            else :
                vari[part[1]] *= int(part[2])

        elif part[0] == 'JUMP':
            i = jump_location[part[1]]

        elif part[0] == 'IF':
            if vari_or_digit(part[3]):
                if part[2] == '<':
                    if vari[part[1]] < vari[part[3]]:
                        i = jump_location[part[5]]
                elif part[2] == '>':
                    if vari[part[1]] > vari[part[3]]:
                        i = jump_location[part[5]]
                elif part[2] == '<=':
                    if vari[part[1]] <= vari[part[3]]:
                        i = jump_location[part[5]]
                elif part[2] == '>=':
                    if vari[part[1]] >= vari[part[3]]:
                        i = jump_location[part[5]]
                elif part[2] == '==':
                    if vari[part[1]] == vari[part[3]]:
                        i = jump_location[part[5]]   
                elif part[2] == '!=':
                    if vari[part[1]] != vari[part[3]]:
                        i = jump_location[part[5]]        
            else:
                if part[2] == '<':
                    if vari[part[1]] < int(part[3]):
                        i = jump_location[part[5]]
                elif part[2] == '>':
                    if vari[part[1]] > int(part[3]):
                        i = jump_location[part[5]]
                elif part[2] == '<=':
                    if vari[part[1]] <= int(part[3]):
                        i = jump_location[part[5]]
                elif part[2] == '>=':
                    if vari[part[1]] >= int(part[3]):
                        i = jump_location[part[5]]
                elif part[2] == '==':
                    if vari[part[1]] == int(part[3]):
                        i = jump_location[part[5]]
                elif part[2] == '!=':
                    if vari[part[1]] != int(part[3]):
                        i = jump_location[part[5]]

        elif part[0] =='END':
            pass
        else: 
            jump_location[part[0][:-1]] = i
        i += 1
    return result

def vari_or_digit(s):
    if s in ascii_letters:
        return True
    else :
        return False
