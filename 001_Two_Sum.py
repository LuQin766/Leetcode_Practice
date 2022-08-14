'''
---Description---
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
'''

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        dic = {}
        for i, num in enumerate(nums):
          if target - num in dic:
            return [dic[target-num], i]
          dic[num] = i 

## test code
test_nums = [-2,1,-3,4,-1,0,0,-5,0]
test_null_nums = []
test = Solution
test_target = -2
outPut = test.twoSum(test,test_nums,test_target)
print("Output: ", outPut)