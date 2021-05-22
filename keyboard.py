'''
the message is always shiffted by just one position to left or to right,
'''

def decryptMessage(direction, string):
    chars = '''qwertyuiop\nasdfghjkl;\nzxcvbnm,./'''

    # direction: letters is shiffted just by on position
    message = ''
    if direction == 'R':
        for i in range(len(string)):
            char = string[i]
            idx = chars.index(char)
            if chars[idx - 1] == '\n':
                pass
            # update the message
            message += chars[idx - 1]
    else:
        for i in range(len(string)):
            char = string[i]
            idx = chars.index(char)
            if chars[idx + 1] == '\n':
                pass
            # update the message
            message += chars[idx + 1]

    return message

if __name__ == '__main__':
    direction = input()
    string = input()

    print(decryptMessage(direction, string))

