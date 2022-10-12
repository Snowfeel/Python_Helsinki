# tee ratkaisu tänne
# Write your solution here
def get_station_data(filename: str):
    with open(filename) as f:
        data = f.read()
        data = data.strip().split('\n')
        header = data.pop(0)
        station = {}
        for i in data:
            part = i.strip().split(";")
            station[part[3]] = (float(part[0]),float(part[1]))
        return station

def distance(stations: dict, station1: str, station2: str):
    import math

    x_km = (stations[station1][0] - stations[station2][0]) * 55.26
    y_km = (stations[station1][1] - stations[station2][1]) * 111.2
    distance_km = math.sqrt(x_km**2 + y_km**2)

    return distance_km

def greatest_distance(stations: dict):
    greatest = 0
    for i in stations:
        for j in stations:
            distan = distance(stations,i,j)
            if distan > greatest:
                greatest = distan
                station1 = i
                station2 = j
            
    return station1,station2,greatest
