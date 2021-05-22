'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.



Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]


Constraints:

2 <= nums.length <= 105
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
'''

# the first approach to solve this problem is to use the brute force algorithm which means to iterate over
# every single element in the list with two iterators and check whether its sum equal the target or not
#DISADVANTAGE: this solution is too slow, since the time complexty is O(n^2)
def BruteForceTwoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]



# the second appraoch is to use the a hash table, where we're gonna store the complement of target - currentNum
# and keep iterating till we hit an element with the same complement
# this solution is faster than the brute force one, the time complexty is O(n)
def TwoSum(nums, target):
    compelementDict = {}
    ''' iterate over the list and calculate the compelement '''
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement not in compelementDict:
            compelementDict[nums[i]] = i
        else:
            return [compelementDict[complement], i]
