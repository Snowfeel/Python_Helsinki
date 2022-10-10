# Write your solution here
def create_tuple(x: int, y: int, z: int):
    s = [x,y,z]
    s.sort()
    su = s[0]+s[1]+s[2]
    t = (s[0],s[2],su)
    return t
