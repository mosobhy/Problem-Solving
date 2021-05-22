def get_num(h, m):

    for i in m:
        x = i[0]
        y = i[1]
        if x != 1:
            h[x-1] += y - 1
        if x != len(h):
            h[x+1] += h[x] - y
        h[x] = 0
        
    # count the birds on each line
    return h

if __name__ == '__main__':
    n = int(input())                            # num of wires
    birds = list(map(int, input().split()))     # birds on each wire

    # compsing a dictionary of line: num_of_birds
    h = {}  # to pass the function
    for i in range(1, n+1):
        h[i] = birds[i-1]

    shots = int(input())

    lines_birds = []                            # [line_index , bird_index]
    for i in range(shots):
        lines_birds.append(list(map(int, input().split())))

    new_h = get_num(h, lines_birds)     # here the function call
    for value in new_h.values():
        print(value)
