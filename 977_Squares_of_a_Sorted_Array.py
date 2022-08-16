'''
---Description---
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
'''


class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        return sorted([num ** 2 for num in nums])

## test code
test_nums = [-4,-1,0,3,10]
test = Solution
outPut = test.sortedSquares(test,test_nums)
print("Output: ", outPut)  
