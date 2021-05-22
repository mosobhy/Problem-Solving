def coins(n, c):
    
    # sort the array to make the larges coins adjecent
    # iterate over the array (with sumation) till get the middle + 1
    # count the number of coins ( array elements) 
    sum_of_total_coins = sum(c)
    sum_of_coins = 0
    counter = 0
    for ele in reversed(sorted(c)):
        if sum_of_coins > sum_of_total_coins / 2:
            break
        sum_of_coins += ele
        counter += 1

    return counter         

if __name__ == '__main__':
    n = int(input())
    c = list(map(int, input().split())) # the values of each coin space separated

    print(coins(n, c))