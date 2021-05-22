
def getNumOfPeopleToHelp(arr):
    if len(arr) <= 2:
        return 0
    else:
        return len(arr) - 2

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    print(getNumOfPeopleToHelp(arr))
    