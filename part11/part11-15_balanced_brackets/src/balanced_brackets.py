
def balanced_brackets(my_string: str):
    print(my_string)
    if len(my_string) == 0:
        return True 
    if my_string.count('(') != my_string.count(')') or my_string.count('[') != my_string.count(']'):
        return False
    if my_string[0] != "(" and my_string[0] != "[":
        return balanced_brackets(my_string[1:])
    if my_string[-1] != ")" and my_string[-1] != "]":
        return balanced_brackets(my_string[:-1])
    if my_string[0] == "(":
        if my_string[-1] != ")":
            return False
    elif my_string[0] == "[":
        if my_string[-1] != "]":
            return False

    # remove first and last character
    return balanced_brackets(my_string[1:-1])