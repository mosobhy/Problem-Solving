def iceCream(x, arr):
    # n stands for the nubmer of people waiting
    # x number of ice cream packets available
    # arr = [['+', '5'], ['-', '10']]
    amount = x
    kids = 0
    for chunk in arr:
        if chunk[0] == '+':
            amount += int(chunk[1])
        elif chunk[0] == '-':
            if amount >= int(chunk[1]):
                amount -= int(chunk[1])
            else:
                kids += 1
    return [amount, kids]

if __name__ == '__main__':
    n, x = map(int, input().split())

    arr = []
    for i in range(n):
        arr.append(input().split())   # both will be strings

    out = iceCream(x, arr)
    for i in out:
        print(i, end=' ')
    print()
    