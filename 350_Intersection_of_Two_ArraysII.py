'''
---Description---
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.
----Source---
https://github.com/JiayangWu/LeetCode-Python/blob/master/0350.两个数组的交集II/0350-两个数组的交集II.py
'''

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        from collections import Counter
        dic1 = Counter(nums1)
        print("Dic1: ", dic1)
        dic2 = Counter(nums2)
        print("Dic2: ", dic2)
        

        res = []
        for key, val in dic1.items():
          print("dic2[key]: ", dic2[key])
          res += [key] * min(val, dic2[key]) 
          ## list can be added with a list by +=, also can be multipied by num
          print("Res: ", res)

        return res


## test code
test_nums1 = [4,9,5,9]
test_nums2 = [9,4,9,8,4]
test = Solution
outPut = test.intersect(test,test_nums1, test_nums2)
print("Output: ", outPut)  