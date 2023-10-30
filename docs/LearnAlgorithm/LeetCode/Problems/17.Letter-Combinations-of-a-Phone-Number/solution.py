from typing import List

key2letters = ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]


def get_letters(c):
    return key2letters[int(c) - 2]


class Solution0:
    """
    Runtime: 24 ms, faster than 95.02% of Python3 online submissions for Letter Combinations of a Phone Number.
    Memory Usage: 14.3 MB, less than 64.14% of Python3 online submissions for Letter Combinations of a Phone Number.
    """
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        if len(digits) == 1:
            return get_letters(digits)
        subproblem = self.letterCombinations(digits[1:])
        sol = []
        for digit in get_letters(digits[0]):
            for ele in subproblem:
                sol.append(digit + ele)
        return sol


class Solution1:
    """
    Runtime: 28 ms, faster than 81.61% of Python3 online submissions for Letter Combinations of a Phone Number.
    Memory Usage: 14.2 MB, less than 86.17% of Python3 online submissions for Letter Combinations of a Phone Number.
    """
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        key2letters = ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        ans = [c for c in key2letters[int(digits[0]) - 2]]
        for c in digits[1:]:
            ans = [s + x for x in key2letters[int(c) - 2] for s in ans]
        return ans

if __name__ == '__main__':
    digits = "23"
    sol = Solution1()
    print(sol.letterCombinations(digits))
    print(get_letters("2"))
