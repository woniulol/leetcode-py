"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).



Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

"""

from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        cur1 = 0
        cur2 = 0
        all_nums = []
        while cur1 < len(nums1) and cur2 < len(nums2):
            if nums1[cur1] < nums2[cur2]:
                all_nums.append(nums1[cur1])
                cur1 += 1
            else:
                all_nums.append(nums2[cur2])
                cur2 += 1
        all_nums.extend(nums1[cur1:])
        all_nums.extend(nums2[cur2:])

        if len(all_nums) % 2 == 0:
            return (all_nums[len(all_nums) // 2] + all_nums[len(all_nums) // 2 - 1]) / 2
        else:
            return all_nums[len(all_nums) // 2]
