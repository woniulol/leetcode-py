"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.


"""

from typing import List


# class Solution:
#     def maxArea(self, height: List[int]) -> int:
#         max_area = 0
#         for i in range(len(height)):
#             for j in range(i, len(height)):
#                 area = min((height[i], height[j])) * (j - i)
#                 if max_area < area:
#                     max_area = area
#         return max_area


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        cur_left = 0
        cur_right = len(height) - 1

        while cur_left < cur_right:
            area = min((height[cur_left], height[cur_right])) * (cur_right - cur_left)
            max_area = max((area, max_area))

            if height[cur_left] > height[cur_right]:
                cur_right -= 1
            else:
                cur_left += 1

        return max_area
