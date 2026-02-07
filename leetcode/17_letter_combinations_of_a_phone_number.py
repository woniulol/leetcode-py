from typing import List, Dict


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digits_to_letters_map: Dict[str, str] = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        res: List[str] = []

        for digit in digits:
            letters = digits_to_letters_map[digit]

            if len(res) == 0:
                res = list(letters)
                continue

            new_res = []
            for cur_res in res:
                for letter in letters:
                    new_res.append(cur_res + letter)

            res = new_res

        return res


print(Solution().letterCombinations(digits="23"))
print(Solution().letterCombinations(digits="2"))
