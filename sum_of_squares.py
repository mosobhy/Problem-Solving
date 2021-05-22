def sum_squares(N, X):
    """ Do not use any for loops """

    index = 0
    sum_of_squares = 0
    while index < N:
        if X[index] > 0:
            sum_of_squares += X[index] ** 2
        index += 1

    return sum_of_squares

if __name__ == '__main__':

    T = int(input())    # nubmer of test cases

    for t in range(T):
        N = int(input())    # number of ints per one test case
        X = list(map(int, input().split()))     # list with ints to sum their squares
        print(sum_squares(N, X))
