class ClimbingRoute:
    def __init__(self, name: str, length: int, grade: str):
        self.name = name
        self.length = length
        self.grade = grade

    def __str__(self):
        return f"{self.name}, length {self.length} metres, grade {self.grade}"

def sort_by_length(routes: list):
    def order_by_length (route:tuple):
        return route.length
    return sorted(routes,key=order_by_length,reverse=True)

def sort_by_difficulty(routes: list):
    def order_by_diff(route:tuple):
        return route.grade,route.length,
    return sorted(routes,key=(order_by_diff),reverse=True)

# Write your solution herer:
