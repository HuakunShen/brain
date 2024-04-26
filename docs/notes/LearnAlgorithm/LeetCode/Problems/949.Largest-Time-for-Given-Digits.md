# 949. Largest Time for Given Digits

## Approach 1: Permutation

```python
class Solution:
    """
    Runtime: 28 ms, faster than 92.63% of Python3 online submissions for Largest Time for Given Digits.
    Memory Usage: 13.9 MB, less than 32.88% of Python3 online submissions for Largest Time for Given Digits.
    """

    def permute(self, nums: List[str]) -> List[List[str]]:
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

    def largestTimeFromDigits(self, A: List[int]) -> str:
        def valid(time_tuple):
            return 0 <= time_tuple[0] * 10 + time_tuple[1] < 24 and 0 <= time_tuple[2] * 10 + time_tuple[3] < 60

        permutes = self.permute(A)
        valid_permutes = list(filter(lambda x: valid(x), permutes)) # filter out invalid permutations
        valid_permutes.sort(key=lambda x: (x[0], x[1], x[2], x[3])) # sort permutations
        if valid_permutes:
            largest = "".join([str(num) for num in valid_permutes[-1]])
            return largest[:2] + ":" + largest[2:]
        else:
            return ""
```

Produce the permutations first, same algorithm from Problem **46. Permutations**.

Filter out invalid ones which don't comply with valid time standards.

Sort permutations from smallest to largest.

## Official Approach

```python
class SolutionOfficial:
    """
    Runtime: 28 ms, faster than 92.63% of Python3 online submissions for Largest Time for Given Digits.
    Memory Usage: 14 MB, less than 25.00% of Python3 online submissions for Largest Time for Given Digits.
    """

    def largestTimeFromDigits(self, A: List[int]) -> str:
        max_time = -1
        for a, b, c, d in itertools.permutations(A):
            hour, minute = a * 10 + b, c * 10 + d
            if hour < 24 and minute < 60:
                max_time = max(max_time, hour * 60 + minute)
        return "" if max_time == -1 else "{:02d}:{:02d}".format(max_time // 60, max_time % 60)
```

This uses pretty much the same algorithm as the previous approach, both iterates through all permutations and find the maximum one.

But this one uses a python library.


