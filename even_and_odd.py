'''
some fucking boy was playing with the natural numbers and trying to rearrange them
so he has come up with a silly idea to to put the odd numbers first and then the even numbers
like this 1 2 3 4 5 5 6 7 8
after rearranging
1 3 5 7 2 4 6 8

'''

def nonOptimaGetPos(n, k):

    h = {}

    # check upon the number range is even or odd to be able to decide where the last index of
    # odd numbers will be
    if n % 2 == 0:
        even_idx = int(n / 2) + 1
    else:
        even_idx = int(n // 2) + 2

    # iterate over the numbers and hash each number with its pos as key
    odd_idx = 1
    for i in range(n):
        value = i + 1
        if value % 2 != 0:
            h[odd_idx] = value
            odd_idx += 1
        else:
            h[even_idx] = value
            even_idx += 1

    return h[k]


def optimaGetPos(n, k):
    
    #check if the pos in the even side or in the odd side
    if n % 2 == 0:
        mid = int(n / 2)

        # odd number
        if k <= mid:
            return int(k * 2 - 1)

        else:
            # even number in the even part
            pos = k - mid
            return int(pos * 2)
    # odd range
    else:
        mid = int(n / 2) + 1

        # odd number in odd part
        if k <= mid:
            return int(k * 2 - 1)

        else:
            # even number in the even part
            pos = k - mid
            return int(pos * 2)


if __name__ == '__main__':
    n, k = map(int, input().split())

    print(nonOptimaGetPos(n, k))
    print(optimaGetPos(n, k))