import doctest
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        >>> sol = Solution()
        >>> sol.removeElement([3,2,2,3], 3)
        2
        >>> sol.removeElement([0,1,2,2,3,0,4,2], 2)
        5
        """
        left = len(nums)
        while val in nums:
            left -= 1
            nums.remove(val)
        return left


if __name__ == '__main__':
    doctest.testmod(verbose=True)
