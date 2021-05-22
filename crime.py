
def getTheUntreatedCrimes(events, ordering):
    hired_officers = []     # officers stack
    treated_crimes = 0

    for i in range(events):
        if ordering[i] > 0:
            for j in range(ordering[i]):
                # put the officers as ones
                hired_officers.append(1)
        else:   # this is a crime
            if len(hired_officers) >= 1:
                treated_crimes += 1
                hired_officers.pop()

    total_crimes = len([ crime for crime in ordering if crime == -1 ])
    return total_crimes - treated_crimes

if __name__ == '__main__':
    # events means what ever happens
    # hiring a police officer or a crime occure
    events = int(input())
    chronological_ordering = list(map(int, input().split()))
    if len(chronological_ordering) != events:
        print('error with input')
        raise ValueError

    print(getTheUntreatedCrimes(events, chronological_ordering))