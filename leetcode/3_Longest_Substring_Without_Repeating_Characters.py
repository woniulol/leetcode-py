"""
Given a string s, find the length of the longest sub-string without duplicate characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.

Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Constraints:

    0 <= s.length <= 5 * 104
    s consists of English letters, digits, symbols and spaces.
"""


class Solution:
    def lengthoflongestsubstring(self, s: str) -> int:
        if s == "":
            return 0

        res = 0
        cur_start = 0
        cur_end = 0
        # c: index
        cur_dict = {}

        for i in range(len(s)):
            if s[i] not in cur_dict:
                cur_dict[s[i]] = i
                cur_end = i

            else:
                cur_start = cur_dict[s[i]] + 1
                cur_end = i
                cur_dict = {}
                for j in range(cur_start, cur_end + 1):
                    cur_dict[s[j]] = j

            res = max(res, cur_end - cur_start)

        return res + 1
