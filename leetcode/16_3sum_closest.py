from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # initial value to avoid condition check.
        nums = sorted(nums)
        res: int = nums[0] + nums[1] + nums[-1]
        cur_diff: int = res - target

        for i in range(0, len(nums) - 2):
            if i != 0 and nums[i] == nums[i - 1]:
                continue

            j = i + 1
            k = len(nums) - 1

            while j < k:
                total = nums[i] + nums[j] + nums[k]
                diff = total - target
                if diff == 0:
                    return total

                if abs(diff) < abs(cur_diff):
                    res = total
                    cur_diff = diff

                if diff > 0:
                    k -= 1
                    continue

                if diff < 0:
                    j += 1
                    continue

                j += 1

        return res


print(Solution().threeSumClosest([10, 20, 30, 40, 50, 60, 70, 80, 90], 1))
