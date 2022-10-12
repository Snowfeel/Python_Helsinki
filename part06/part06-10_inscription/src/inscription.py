# Write your solution here
s = input("Whom should I sign this to: ")
file = input("Where shall I save it: ")

with open(file,"w") as f:
    f.write(f"Hi {s}, we hope you enjoy learning Python with us! Best, Mooc.fi Team")