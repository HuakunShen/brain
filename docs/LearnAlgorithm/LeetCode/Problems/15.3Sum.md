# 15. 3Sum

https://leetcode.com/problems/3sum/

Level: Medium

[Official Solution in Chinese](https://leetcode.cn/problems/3sum/solution/san-shu-zhi-he-by-leetcode-solution/)

[GIF Visualization](https://leetcode.cn/problems/3sum/solution/three-sum-giftu-jie-by-githber/)

![gif](https://pic.leetcode-cn.com/2124b524439bcf0eb159ba43be4420c76f60ff2b3b51f87de269c001a323ea1a-Video_2019-06-19_192352.gif)

## Solution

Sorting takes **O(n log(n))**

The rest of the 2 for loops takes **O(n^2)**

```python
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if n < 3:
            return []
        nums.sort()      # n log(n)
        result = []
        for p1 in range(n):
            if p1 > 0 and nums[p1] == nums[p1 - 1]:
                continue
            first = nums[p1]
            target = -first
            p3 = n - 1
            for p2 in range(p1 + 1, n):
                if p2 > p1 + 1 and nums[p2] == nums[p2 - 1]:
                    continue
                while p2 < p3 and nums[p2] + nums[p3] > target:
                    p3 -= 1
                if p2 == p3:
                    break
                if nums[p2] + nums[p3] == target:
                    result.append([nums[p1], nums[p2], nums[p3]])
        return result
```