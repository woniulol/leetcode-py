"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
"""

from typing import List


"""
Brut force way.
"""


# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         res: List[List[int]] = []

#         for i in range(len(nums) - 2):
#             for j in range(i + 1, len(nums) - 1):
#                 for k in range(j + 1, len(nums)):
#                     if nums[i] + nums[j] + nums[k] == 0:
#                         new_ls = [nums[i], nums[j], nums[k]]
#                         append = True
#                         for ls in res:
#                             if sorted(new_ls) == sorted(ls):
#                                 append = False
#                                 break
#                         if append:
#                             res.append(new_ls)

#         return res


"""

Sort the list first and ignore any i j k that is the same as the previous one.

"""


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)

        res: List[List[int]] = []
        for i in range(len(nums)):
            if (i != 0) and (nums[i] == nums[i - 1]):
                continue

            j: int = i + 1
            k: int = len(nums) - 1

            while j < k:
                if (j != i + 1) and nums[j] == nums[j - 1]:
                    j += 1
                    continue

                total = nums[i] + nums[j] + nums[k]
                if total == 0:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    continue
                if total < 0:
                    j += 1
                    continue
                if total > 0:
                    k -= 1
                    continue

        return res
