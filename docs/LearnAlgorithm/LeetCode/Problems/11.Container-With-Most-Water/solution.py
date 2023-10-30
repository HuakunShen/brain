class Solutio0:
    def maxArea(self, height: List[int]) -> int:
        m = 0
        for i in range(len(height)):
            for j in range(len(height)):
                if j > i:
                    l = j - i
                    h = min(height[i], height[j])
                    area = l * h
                    if area > m: m = area
        return m
            

class Solution:
    """
    Runtime: 128 ms, faster than 86.21% of Python3 online submissions for Container With Most Water.
    Memory Usage: 15.4 MB, less than 35.33% of Python3 online submissions for Container With Most Water.
    """
    def maxArea(self, height: List[int]) -> int:
        m, s, e = 0, 0, len(height) - 1
        while s != e:
            area = (e - s) * min(height[s], height[e])
            if area > m: m = area
            if height[s] < height[e]: 
                s += 1
            else:
                e -= 1
        return m