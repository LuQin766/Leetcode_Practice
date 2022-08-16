'''
---Description---
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.
'''


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        left, right = 0, len(nums)
        while(left <= right):
            mid = int((left + right) / 2)
            print("Mid: ", mid)
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid
            elif nums[mid] == target:
                # print nums[left]
                return mid
            
        return -1

## test code
test_nums = [-1,0,3,5,9,12]
test_target = 9
test = Solution
outPut = test.search(test,test_nums, test_target)
print("Output: ", outPut)  

