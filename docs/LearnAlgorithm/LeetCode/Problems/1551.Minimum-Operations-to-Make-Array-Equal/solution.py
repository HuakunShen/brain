class Solution:
    def minOperations(self, n: int) -> int:
        less_count = 0
        for i in range(n):
            num = 2*i+1
            if num > n:
                less_count += num - n
        return less_count
        