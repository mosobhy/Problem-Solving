
def sol(nums):
    '''
    This function should return the lenght of the longest 
    consecutive sequence of numbers

    '''
    if len(nums) == 0:
        return 0

    if len(nums) == 1:
        return 1
        
    counter = 0
    idx = 1
    nums.sort()

    while idx < len(nums):
        difference = nums[idx] - nums[idx-1]
        if difference == 1:
            counter += 1
        idx += 1
            
    return 0 if counter == 0 else counter + 1

if __name__ == '__main__':
    # get the input
    nums = list(map(int, input().split()))

    output = sol(nums)
    print(output)