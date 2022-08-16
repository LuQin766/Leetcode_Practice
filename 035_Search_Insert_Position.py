'''
---Description---
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.
'''

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        left, right = 0, len(nums)
        
        while left < right:
          mid = (left + right) // 2
          if nums[mid] < target:
            left = mid + 1
          elif nums[mid] > target:
            right = mid
          elif nums[mid] == target:
            return mid
        
        return left