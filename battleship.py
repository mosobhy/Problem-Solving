'''
N * N grid represents the placement of the ships on the sea shore

x => alive ship ( this what i want to keep track of it and count it )
@ => hit ship
. => empty cell

make an effecient algorithm to print out the number of still alive ships in the grid

so.. all i have to do is an array travesal algorithm..dfs or bfs
but here i am going to solve it using brute force since i didn't study the
dfs yet

'''

def solution(grid):

    # brute force
    ships_counter = 0
    for ships in grid:          # O(N) since it iterates over the whole grid
        for char in ships:      # O(N)
            if char == 'x':
                ships_counter += 1
    return ships_counter        # the over all runtime complexity is O(N^2)

if __name__ == '__main__':
    sol = []

    # test cases
    t = int(input())
    for i in range(t):    
        n = int(input())
        grid = []

        # read the input
        for i in range(n):
            grid.append(input())
        
        # pass to the function
        sol.append(solution(grid))

    # print out the solution
    for i in range(t):
        print(f"Case {i+1}: {sol[i]}")