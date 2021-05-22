
'''
The Problem link on codeforces
http://codeforces.com/contest/731/problem/A
'''

def getTheLeasteMovements(word):
    movements = 0
    index = 0
    for i in range(len(word)):       # map
        # check for both clockwise and counterclockwise to decide
        # which way is shorter
        char_index = abs(ord(word[i]) - 97)   # 12
        distance = abs(index - char_index)         # 0 - 12 = 12
        if distance < 13:
            # go backword
            movements += distance
        else:
            movements += 26 - distance
        # update the basepointer
        index = char_index

    return movements

if __name__ == '__main__':
    word = input()
    print(getTheLeasteMovements(word))