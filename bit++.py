def getVarXValue(arr):   # array of statements to be executed
    # --x , ++x, x++, x--
    # x's initial value is 0
    # ['x++', 'x++', '--x', '++x']  # should return 2
    x_value = 0
    for state in arr:
        if state in ['++X', 'X++']:
            x_value += 1
        else:
            x_value -= 1

    return x_value

if __name__ == '__main__':
    n = int(input())    # number of statements
    
    statements = []
    for i in range(n):
        statements.append(input())

    print(getVarXValue(statements))