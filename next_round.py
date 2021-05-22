
def getThePersonsForNextRound(contestants, minimum_score):
    counter = 0
    for score in contestants:
        if score > minimum_score:
            counter += 1
    return counter

if __name__ == '__main__':

    # get n, particpants
    # k, the minimum score
    inputs = list(map(int, input().split()))
    particpants = list(map(int, input().split()))
    if len(particpants) != inputs[0]:
        raise ValueError

    print(getThePersonsForNextRound(particpants, inputs[1]))
