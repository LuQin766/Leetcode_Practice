'''
---Description---
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
'''

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
      
        return len(set(nums)) != len(nums)


## test code
test_nums = [-2,1,-3,-4,-1,0,-5]
test_null_nums = []
test = Solution
outPut = test.containsDuplicate(test,test_nums)
print("Output: ", outPut)   
