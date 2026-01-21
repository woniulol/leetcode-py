"""
Given an integer x, return true if x is a palindrome, and false otherwise.


Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.



Constraints:

    -2 ** 31 <= x <= 2 ** 31 - 1


Follow up: Could you solve it without converting the integer to a string?

"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        if x == 0:
            return True

        digits = 1
        res = x / (10**digits)
        while res > 1:
            digits += 1
            res = x / (10**digits)

        digits_reversed = 1
        while digits_reversed <= digits:
            cur_left: int = x // (10 ** (digits - 1))
            cur_right: int = x % (10**digits_reversed)
            if not cur_left == cur_right:
                return False

            if cur_left != 0:
                x %= cur_left * (10 ** (digits - 1))

            x //= 10**digits_reversed
            digits -= 2

        return True


# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         if x < 0:
#             return False

#         if x == 0:
#             return True

#         digits = 1
#         res = x / (10**digits)
#         while res > 1:
#             digits += 1
#             res = x / (10**digits)

#         x_reversed = 0
#         prev = 0
#         for i in range(1, digits + 1):
#             div = 10 ** (i - 1)
#             x_reversed += (x % 10**i - prev) / div * (10 ** (digits - i))
#             prev = x % 10**i

#         return x_reversed == x
