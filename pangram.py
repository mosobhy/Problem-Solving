'''
pangram: the string with all the alphabets in it

'''
def isPangram(length, String):
    letters = []

    if length < 26:
        return 'NO'
    
    for i in range(length):
        char = String[i].lower()
        if char in letters:
            pass
        else:
            letters.append(char)
        
    return 'YES' if len(letters) == 26 else 'NO'
        

if __name__ == '__main__':
    n = int(input())

    string = input()

    print(isPangram(n, string))