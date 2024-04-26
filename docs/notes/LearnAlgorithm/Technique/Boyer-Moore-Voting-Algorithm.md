# Boyer-Moore Voting Algorithm

> Boyer–Moore majority vote algorithm

> This is a very useful algorithm for finding the majority element in an array. The majority element is the element that appears more than `n/2` times in an array of size `n`. This algorithm is also known as the **Majority Vote Algorithm**.


This leetcode problem is a good example of using this algorithm: https://leetcode.com/problems/majority-element/

```python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # n = len(nums)
        # n_2 = n // 2
        # sorted_nums = sorted(nums)
        # return sorted_nums[n_2]
        count = 0
        candidate = None
        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if candidate == num else -1
        return candidate
```

The commented out section is the naive solution. The time complexity is `O(nlogn)` because of the sorting. 

The uncommented section is the Boyer-Moore Voting Algorithm. The time complexity is `O(n)`.

The idea is pretty simple, 