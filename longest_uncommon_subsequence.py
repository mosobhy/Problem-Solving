def getLongest(a, b):

    if a == b:
        return -1
    elif len(a) > len(b):
        return len(a)
    else:
        return len(b)

if __name__ == '__main__':
    a = input()
    b = input()

    print(getLongest(a, b))    