class Solution1:
    def climbStairs(self, n: int) -> int:
        M = {1: 1, 2: 2}
        for i in range(3, n + 1):
            M[i] = M[i - 1] + M[i - 2]
        return M[n]

class Solution2:
    def climbStairs(self, n: int) -> int:
        if n <= 2: return n
        m = [-1 for _ in range(n + 1)]
        m[1] = 1
        m[2] = 2
        for i in range(3, n + 1):
            m[i] = m[i - 1] + m[i - 2]
        return m[n]

class Solution3:
    """Solution reduces space complexity of O(1)
    """
    def climbStairs(self, n: int) -> int:
        m = [1, 2, -1]
        for i in range(3, n + 1):
            m[(i + 2) % 3] = m[(i + 1) % 3] + m[i % 3]
        return m[(n + 2) % 3]