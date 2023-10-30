# 97. Interleaving String

[LeetCode URL](https://leetcode.com/problems/interleaving-string)

## Solution 0: Pure Recursion (Brute Force)

- [Python Solution](./solution0.py)

  ```python
  class Solution0:
      def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
          sum_all = len(s1) + len(s2) + len(s3)
          if sum_all == 0:
              return True
          elif len(s3) == 0 and sum_all != 0:
              return False
          else:
              first_match, second_match = len(s1) and s1[0] == s3[0], len(s2) and s2[0] == s3[0]
              first_success = self.isInterleave(s1[1:], s2[0:], s3[1:]) if first_match else False
              second_success = self.isInterleave(s1[0:], s2[1:], s3[1:]) if second_match else False
              return first_success or second_success
  ```

- [CPP Solution](./solution0.cpp)

Solution Timeout

**Time Complexity:** O(2^(m+n))

**Space Complexity:** O(m+n)
  - The size of stack for recursive calls can go upto m+nm+n

## Solution 1: Recursion with Memoization

[Python Solution](./solution1.py)

**Time Complexity:** O(m x n)
  - each cell of the memoization table will be calculated at most once, if a value is present then return it takes constant time
**Space Complexity:** O(m x n)
  - memoization table size

```python
class Solution1:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        memo = [[-1] * (len(s2) + 1) for _ in range(len(s1) + 1)]
        # in memoization table, -1 means not visited, 0 means fail, 1 means success
        def helper(i: int, j: int, k: int) -> int:
            sum_remain = len(s1) + len(s2) + len(s3) - i - j - k
            if memo[i][j] != -1:
                pass
            elif sum_remain == 0 or len(s1) - i == 0 and s2[j:] == s3[k:] or len(s2) - j == 0 and s1[i:] == s3[k:]:
                memo[i][j] = 1
            elif k == len(s3) and sum_remain != 0:
                memo[i][j] = 0
            else:
                first_match, second_match = len(s1) - i and s1[i] == s3[k], len(s2) - j and s2[j] == s3[k]
                first_success = helper(i + 1, j, k + 1) if first_match else False
                second_success = helper(i, j + 1, k + 1) if second_match else False
                memo[i][j] = first_success or second_success
            return memo[i][j]

        return bool(helper(0, 0, 0))
```

## Solution 2: 2D Dynamic Programming

[Golang Solution](./solution2.go)

**Time Complexity:** O(m x n)
  - each cell of the memoization table will be calculated exactly once

**Space Complexity:** O(m x n)
  - memoization table size

Runtime: 4 ms, faster than 50.00% of Go online submissions for Interleaving String.

Memory Usage: 2.3 MB, less than 18.29% of Go online submissions for Interleaving String.

```go
func isInterleave(s1 string, s2 string, s3 string) bool {
    l1, l2, l3 := len(s1), len(s2), len(s3)
    if (l3 != l1 + l2) {
        return false;
    }
    dp := make([][]bool, l1 + 1)
    for i := range dp {
        dp[i] = make([]bool, l2 + 1)
    }
    for i := 0; i <= l1; i++ {
        for j := 0; j <= l2; j++ {
            if i == 0 && j == 0 {
                dp[i][j] = true
            } else if i == 0 {
                dp[i][j] = dp[i][j - 1] && s2[j - 1] == s3[i + j - 1]
            } else if j == 0 {
                dp[i][j] = dp[i - 1][j] && s1[i - 1] == s3[i + j - 1]
            } else {
                dp[i][j] = (dp[i - 1][j] && s1[i - 1] == s3[i + j - 1]) || (dp[i][j - 1] && s2[j - 1] == s3[i + j - 1])
            }
        }
	}
    return dp[l1][l2]
}
```

## Solution 3: 1D Dynamic Programming

Same algorithm as previous solution. Only the previous row in the DP table is used when iterating through the DP table,
we can keep only one row (1D DP table).

**Time Complexity:** O(m x n)
  - each cell of the memoization table will be calculated exactly once

**Space Complexity:** O(n)
  - size of s2, only one row of memoization table is kept

**Runtime:** 0 ms, faster than 100.00% of Go online submissions for Interleaving String.

**Memory Usage:** 2.3 MB, less than 24.39% of Go online submissions for Interleaving String.

```go
func isInterleave(s1 string, s2 string, s3 string) bool {
    l1, l2, l3 := len(s1), len(s2), len(s3)
    if (l3 != l1 + l2) {
        return false;
    }
    dp := make([]bool, l2 + 1)
    for i := 0; i <= l1; i++ {
        for j := 0; j <= l2; j++ {
            if i == 0 && j == 0 {
                dp[j] = true
            } else if i == 0 {
                dp[j] = dp[j - 1] && s2[j - 1] == s3[i + j - 1]
            } else if j == 0 {
                dp[j] = dp[j] && s1[i - 1] == s3[i + j - 1]
            } else {
                dp[j] = dp[j] && s1[i - 1] == s3[i + j - 1] || dp[j - 1] && s2[j - 1] == s3[i + j - 1]
            }
        }
	}
    return dp[l2]
}
```


## Comments

For cpp solutions, test cases were implemented using `assert`, use the following command to run.

```bash
g++ solution0.cpp && ./a.out && rm ./a.out
```