from math import sqrt
 
def getMaxAndMin(cities):
    sol = []
 
    # brute force over the whole cities
    for i in range(len(cities)):
        distances = []
        for j in range(len(cities)):
            if cities[i] != cities[j]:
                x1 = cities[i]
                x2 = cities[j]
                dist = sqrt((x1 - x2)**2)
 
                distances.append(dist)
 
        # figure out what city have the max and min
        sol.append([min(distances), max(distances)])
 
    return sol
 
if __name__ == '__main__':
    n = int(input())
    cities = list(map(int, input().split()))
 
    # pass to function
    sol = getMaxAndMin(cities)
 
    for i in sol:
        print(int(i[0]), int(i[1]))