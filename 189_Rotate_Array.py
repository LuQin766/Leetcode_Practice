'''
---Description---
Given an array, rotate the array to the right by k steps, where k is non-negative.
'''

from bisect import bisect


class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        k %= len(nums)
        print("k:", k)
        nums[ : ] = nums[-k: ] + nums[ :-k]
        
        ## check 
        return nums

## test code
test_nums = [1,2]
test_k = 3
test = Solution
outPut = test.rotate(test,test_nums,test_k)
print("Output: ", outPut)  
