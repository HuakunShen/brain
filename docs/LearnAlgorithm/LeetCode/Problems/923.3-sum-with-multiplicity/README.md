# 923. 3Sum With Multiplicity

https://leetcode.com/problems/3sum-with-multiplicity/

Level: Medium

## Solution

```python
class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        ans, mod, n = 0, 10**9 + 7, len(arr)
        arr.sort()
                
        for i in range(n):
            diff = target - arr[i]
            p1, p2 = i + 1, n - 1
            # two pointers
            while p1 < p2:
                _sum = arr[p1] + arr[p2]
                if _sum < diff:
                    p1 += 1
                elif _sum > diff:
                    p2 -= 1
                else:
                    # _sum == diff, count number of 2 sums
                    if arr[p1] != arr[p2]:
                        left, right = 1, 1
                        while p1 + 1 < n - 1 and arr[p1] == arr[p1 + 1]:
                            left += 1
                            p1 += 1
                        while p2 - 1 > p1 and arr[p2] == arr[p2 - 1]:
                            right += 1
                            p2 -= 1
                        ans += left * right
                        ans %= mod
                        p1 += 1
                        p2 -= 1
                    else:
                        # arr[p1] == arr[p2], number from p1 to p2 are all the same, then it's a combination problem
                        # (p2 - p1 + 1)C2, the formula for combination is nCr = n!/r!(n-r)!. When r is 2 this can be simplified to n(n-1)/2
                        ans += (p2 - p1 + 1) * (p2 - p1) / 2
                        ans %= mod
                        break   # all possiblities are counted
        return int(ans)
```