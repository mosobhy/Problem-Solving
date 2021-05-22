
def getTheGoodNumbersCount(n, k, nums):
    ''' a good number is the number that contain all the digits for 0 to k '''

    counter = 0

    for num in nums:
        range_list = list(range(k+1))
        for digit in num:
            if int(digit) in range_list:
                range_list.remove(int(digit))
            else:
                continue
        if len(range_list) ==  0:
            counter += 1

    return counter

if __name__ == '__main__':

    n, k = input().split()
    n = int(n)
    k = int(k)

    numbers = [None] * n
    for i in range(n):
        numbers[i] = input()

    print(getTheGoodNumbersCount(n, k, numbers))