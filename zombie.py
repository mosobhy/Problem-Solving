# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

'''
keep track of the number of steps taken by doctor to use to locate the next zombie

repeate
. meeti_in = zombie_loc - ROOT // 2    , 4 - 0 // 2 = 2
. steps_taken = 2 * meet_in           , 2 * 2 = 4
. next_zombie_location = zombie_loc - steps_taken   , 7 - 4 = 3

'''

def solution(A, B):
    # write your code in Python 3.6
    if len(B) == 0:
        return 'Doable'
    ROOT = 0
    taken_steps = 0
    vaccinated = 0
    index = 0
    while True:
        if ROOT in B:
            return "Hopeless"
        
        meet_in = ((B[index] - taken_steps) - ROOT) // 2
        if meet_in > 0:
            vaccinated += 1
            index += 1
        else:
            return "Hopeless"

        taken_steps = 2 * meet_in

        if vaccinated == len(B):
            return "Doable"


if __name__ == "__main__":

    A = [-1, 0, 1, 2, 3]
    B = []

    state = solution(A, B)
    print(state)








