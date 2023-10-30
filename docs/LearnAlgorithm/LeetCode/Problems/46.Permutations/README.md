# 46. Permutations

## Approach Recursion

```python
class Solution:
    """
    Runtime: 40 ms, faster than 80.46% of Python3 online submissions for Permutations.
    Memory Usage: 13.9 MB, less than 78.61% of Python3 online submissions for Permutations.
    """
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return []
        elif len(nums) == 1:
            return [nums]
        result = []
        for i in range(len(nums)):
            sub_perms = self.permute(nums[:i] + nums[i + 1:])
            for perm in sub_perms:
                result.append([nums[i]] + perm)
        return result
```

By definition of **permutation**, every number can be placed at every position.

So we use a `for loop` to give every number in the list a chance to be the first number.

After fixing a number in the first position, pass the rest of the list to `permute` (recursion) to get a list of permutations and concatenate each of them to the first position.
Then we get the permutations starting with this number. 
