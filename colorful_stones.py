
def get_stone_pos(s, t):
    
    index = 0
    pos = 1
    for i in range(len(t)):
        if t[i] == s[index]:
            pos += 1
            index += 1
    
    return pos

if __name__ == '__main__':

    # get the stones list
    stones = input()
    instructions = input()

    print(get_stone_pos(stones, instructions))