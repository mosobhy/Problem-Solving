from random import sample   # sample is to return a random sequence of size k with out raplacements(duplications)
import string               # to use the English alphabets in lower case, better than making a constant varibale string with all 26 letters

def getChunk(length):
    # the length of password bigger than the whole population, reutnr the population
    if length > len(string.ascii_lowercase):
        return string.ascii_lowercase       # thats makes the algorithms not effictive at high lenght passwords

    return sample(string.ascii_lowercase, k=length)     # k is optional parameter to define the desired length, its default value =1

def convert_to_str(listr):
    string = ''
    for char in listr:
        string += char

    return string

def generatePass(length, letters_range):
    word = getChunk(length)
    distinict_chars = convert_to_str(word)[:letters_range]

    password = ''
    for i in range(length):
        password += distinict_chars[i%letters_range]

    return password

if __name__ == '__main__':
    n, k = map(int, input().split())

    print(generatePass(n, k))


''' 
the algorithm becomes detectable when the lenght of the password exceeds the alphabets length
and the distinct chars is to small 
i.e.
100 2
ans: ababab.....

100 1
ans: aaaaaaaaaa...to 100

200 3
ans: abcabcabc....to 200
'''
