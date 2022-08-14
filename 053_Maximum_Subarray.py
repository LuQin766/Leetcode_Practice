'''
---description---
find the contiguous subarray

---source---
From github
address: 
https://github.com/JiayangWu/LeetCode-Python/blob/master/0053.最大子序和/0053-最大子序和.py
'''

class Solution(object):

    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        ## if the nums is null, the sum is 0
        if not nums:
            ##print("The nums is NULL!")
            return 0

        ## copy the nums[] but replace each with 0
        dp = [0 for each in nums]
        ## copy the first item in nums[]
        dp[0] = nums[0]
        
        for i, x in enumerate(nums):
            if i:
                ## if the forwarding sum is greater than 0
                if dp[i - 1] > 0:
                    ## compare the add of the forwading sum and the new with 0
                    dp[i] = max(dp[i - 1] + x, dp[i]) 
                else:
                    dp[i] = x
                    
        return max(dp)


## test code
test_nums = [-2,1,-3,-4,-1,0,0,-5,0]
test_null_nums = []
test = Solution
outPut = test.maxSubArray(test,test_nums)
print("Output: ", outPut)


