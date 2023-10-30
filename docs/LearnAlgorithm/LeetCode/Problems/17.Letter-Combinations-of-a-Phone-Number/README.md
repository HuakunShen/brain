# 17. Letter Combinations of a Phone Number

## Tags
- String
- Backtracking
- Depth-first Search
- Recursion

Every case must be gone through, so there is not really a method to save time.

The problem can be divided into sub-problems recursively, remove 1 digit, compute the solution on the rest of the digits.

Then do a cross join between the letters corresponding to the removed digit and the solution of the sub-problem. 

## Recursion

Runtime: 24 ms, faster than 95.02% of Python3 online submissions for Letter Combinations of a Phone Number.

Memory Usage: 14.3 MB, less than 64.14% of Python3 online submissions for Letter Combinations of a Phone Number.

```python
from typing import List

key2letters = ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]


def get_letters(c):
    return key2letters[int(c) - 2]


class Solution:
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
```


## Iteration

Runtime: 28 ms, faster than 81.61% of Python3 online submissions for Letter Combinations of a Phone Number.

Memory Usage: 14.2 MB, less than 86.17% of Python3 online submissions for Letter Combinations of a Phone Number.

```python
from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        key2letters = ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        ans = [c for c in key2letters[int(digits[0]) - 2]]
        for c in digits[1:]:
            ans = [s + x for x in key2letters[int(c) - 2] for s in ans]
        return ans
```






