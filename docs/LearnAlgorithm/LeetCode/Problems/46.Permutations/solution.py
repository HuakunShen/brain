from typing import List


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


if __name__ == '__main__':
    sol = Solution()
    print(sol.permute([]))
    print(sol.permute([1]))
    print(sol.permute([1, 2, 3]))
