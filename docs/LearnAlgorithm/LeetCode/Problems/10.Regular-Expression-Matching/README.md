# 10. Regular Expression Match

[LeetCode Official Solution](https://leetcode.com/problems/regular-expression-matching/solution/)

## Approach 1: Recursion

This approach is similar to a iterative/loop approach but using loops to solve this problem is very complicated, since there are many cases. Using Recursion and `or` operator to branch these cases makes the code simpler to implement.

```python
class SolutionRecursion:
    """
    Runtime: 1284 ms, faster than 22.72% of Python3 online submissions for Regular Expression Matching.
    Memory Usage: 13.9 MB, less than 55.53% of Python3 online submissions for Regular Expression Matching.
    """

    def isMatch(self, s: str, p: str) -> bool:
        # if no pattern, no string. No string -> a* still works
        if len(p) == 0:
            return len(s) == 0
        first_char_match = s and (s[0] == p[0] or p[0] == '.')
        # there may be more char to match in pattern or *
        # current evaluating pattern contains kleene star
        if len(p) >= 2 and p[1] == '*':
            """
            case 1: kleene star ends here
                case 1.1: first char doesn't match, skip current kleene star pattern
                case 1.2: first char matches but still want to skip current kleene start pattern, consider this case: s = "a", p = "a*a"
            case 2: continue kleene star pattern, go to next char in string "s"
            """
            return self.isMatch(s, p[2:]) or (first_char_match and self.isMatch(s[1:], p))
        else:
            # currently matching basic char (no kleene star involved), if current char matches, keep matching the rest of the string and pattern
            return first_char_match and self.isMatch(s[1:], p[1:])
```

## Approach 2: Dynamic Programming 1
Exactly the same as Approach 1 except that DP uses memoization
### Approach 2.1: Official Solution, use set for memoization
```python
class SolutionDP1:
    """
    Runtime: 36 ms, faster than 97.64% of Python3 online submissions for Regular Expression Matching.
    Memory Usage: 14.1 MB, less than 10.73% of Python3 online submissions for Regular Expression Matching.
    """
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}
        def dp(row, col):
            if not (row, col) in memo:
                if col == len(p):
                    ans = row == len(s)
                else:
                    first_match = row < len(s) and p[col] in {s[row], '.'}
                    if col + 1 < len(p) and p[col + 1] == '*':
                        ans = (first_match and dp(row + 1, col)) or dp(row, col + 2)
                    else:
                        ans = first_match and dp(row + 1, col + 1)
                memo[(row, col)] = ans
            return memo[row, col]

        return dp(0, 0)
```

#### Complexity Analysisl

let m=len(p), n=len(s)

**Time Complexity:** O(mn), go through most of the table, bounded by *m x n*

**Space Complexity:** O(mn), created a (m+1)x(n+1) memoization table.

### Approach 2.2: Use 2D Array for memoization

Use 2D array instead of set for memoization.

```python
class SolutionDP2:
    """
    Runtime: 2912 ms, faster than 5.05% of Python3 online submissions for Regular Expression Matching.
    Memory Usage: 14 MB, less than 21.16% of Python3 online submissions for Regular Expression Matching.
    """

    def isMatch(self, s: str, p: str) -> bool:
        # dimension + 1 because there could be index out of range, dealing with edge cases is complicated
        # adding 1 more row and column solve the problem easily
        memo = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]

        def dp(row, col):
            if not memo[row][col]:
                if col == len(p):
                    # pattern reaches the end, if string also reaches the end, then ans is True
                    ans = row == len(s)
                else:
                    first_match = row < len(s) and p[col] in {s[row], '.'}
                    if col + 1 < len(p) and p[col + 1] == '*':
                        """
                        case 1: kleene star ends here
                            case 1.1: first char doesn't match, skip current kleene star pattern
                            case 1.2: first char matches but still want to skip current kleene start pattern, consider this case: s = "a", p = "a*a"
                        case 2: continue kleene star pattern, go to next char in string "s"
                        """
                        ans = (first_match and dp(row + 1, col)) or dp(row, col + 2)
                    else:
                        # currently matching basic char (no kleene star involved), if current char matches, keep matching the rest of the string and pattern
                        ans = first_match and dp(row + 1, col + 1)
                memo[row][col] = ans
            return memo[row][col]

        return dp(0, 0)
```

#### Complexity Analysis

let m=len(p), n=len(s)

**Time Complexity:** O(mn), go through most of the table, bounded by *m x n*

**Space Complexity:** O(mn), created a (m+1)x(n+1) memoization table.

### Approach 2.3 Bottom Up Dynamic Programming

```python
class SolutionDPBottomUp1:
    """
    Runtime: 48 ms, faster than 82.23% of Python3 online submissions for Regular Expression Matching.
    Memory Usage: 14.1 MB, less than 16.86% of Python3 online submissions for Regular Expression Matching.
    """
    def isMatch(self, s: str, p: str) -> bool:
        memo = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        # same as step 1 of recursion approach, assuming previous all match
        # if reach the end of both pattern and string. must match overall
        memo[-1][-1] = True
        for row in range(len(s), -1, -1):
            """
            why row starts from len(s) len(s) - 1 which is the last character?
            The extra row is actually for the case of empty string, such as this example: s="", p="a*"
            If we don't start from the last row, There is no way of changing memo[0][0] to True (The True is taken from memo[-1][-1]
            See graph #.
            Consider another case: s="aa", p="a*"
            See graph #.
            memo[2][0] is the same as the previous case (empty string), must be updated to "True". This value will be used in the future steps
            When calculating memo[1][0], memo[2][0] will be looked at, and update memo[1][0] to "True"
            """
            for col in range(len(p) - 1, -1, -1):
                first_match = row < len(s) and p[col] in {s[row], '.'}
                if col + 1 < len(p) and p[col + 1] == '*':
                    memo[row][col] = (first_match and memo[row + 1][col]) or memo[row][col + 2]
                else:
                    memo[row][col] = first_match and memo[row + 1][col + 1]

        return memo[0][0]
```

#### Empty String Case

|      | a    | *    |      |
| ---- | ---- | ---- | ---- |
| ""   | T    | F    | T    |

#### `aa` and a* case

|      | a    | *    |      |
| ---- | ---- | ---- | ---- |
| a    |      |      | F    |
| a    | T    |      | F    |
|      | T    | F    | T    |

### Complexity Analysis

let m=len(p), n=len(s)

**Time Complexity:** O(mn), Iterate Through entire table.

**Space Complexity:** O(mn), created a (m+1)x(n+1) memoization table.

## Approach 3: Dynamic Programming 2

In Approach 2, Dynamic Programming has an extra row & column, which is for the special case **empty string**.

However, it doesn't look intuitive enough. Empty string case should start from the beginning, not the end of the row & column.

And both the recursion and bottom-up method in Approach 2 fill the memoization table from end to beginning. Intuitively, we compare characters from beginning to end, thus we can also fill the memo table from beginning to end like this:

|      | ""   | a    | *    |
| ---- | ---- | ---- | ---- |
| ""   | T    | F    | F    |
| a    | F    |      |      |
| a    | F    |      |      |

The table has an extra row and column from the beginning.

```python
class SolutionDPBottomUp2:
    """
    Runtime: 40 ms, faster than 94.16% of Python3 online submissions for Regular Expression Matching.
    Memory Usage: 14 MB, less than 26.04% of Python3 online submissions for Regular Expression Matching.
    """
    def isMatch(self, s: str, p: str) -> bool:
        memo = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        memo[0][0] = True
        for col in range(1, len(memo[0])):
            # init all empty string cases
            if p[col - 1] == "*":
                memo[0][col] = memo[0][col - 2]
        for row in range(1, len(memo)):
            for col in range(1, len(memo[0])):
                cur_p, cur_s = p[col - 1], s[row - 1]
                first_match = cur_p in {cur_s, '.'}
                if first_match:
                    # check previous pattern and string char
                    memo[row][col] = memo[row - 1][col - 1]
                elif cur_p == '*':
                    """
                    case 1: 0 occurrence for *, then check 2 pattern char before, col - 2
                    case 2: repeat char, then check previous string char. 
                    If current repeating pattern matches current string char.
                    """
                    memo[row][col] = memo[row][col - 2] or (p[col - 2] in {cur_s, '.'} and memo[row - 1][col])
                else:
                    # doesn't match
                    memo[row][col] = False
        return memo[len(s)][len(p)]
```

|      | ""   | a    | *    |
| ---- | ---- | ---- | ---- |
| ""   | T    | F    | T    |
| a    | F    | T    | T    |
| a    | F    | F    | T    |

### Complexity Analysis

let m=len(p), n=len(s)

**Time Complexity:** O(mn), Iterate Through entire table.

**Space Complexity:** O(mn), created a (m+1)x(n+1) memoization table.





