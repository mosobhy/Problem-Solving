

# getting ints from the user
int1 = int(input())
print(f'custom int: {int1}')


# getting array of int inputs
arr = list(map(int, input().split()))
print(f'array: {arr}')

# getting array of ints of size n
arr1 = []
for _ in range(n):
    arr1.extend(map(int(input().split()))


# getting 2D array of int inputs
twoD_arr = []
for i in range(3):   # 3 stands for the nubmer of rows of any number of columns
    twoD_arr.append([int(i) for i in input().split()])
print(f'2D array: {twoD_arr}')
