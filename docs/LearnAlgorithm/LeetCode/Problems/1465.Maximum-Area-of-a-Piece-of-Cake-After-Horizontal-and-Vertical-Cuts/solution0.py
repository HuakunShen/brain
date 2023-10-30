class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        hcuts = [0] + sorted(horizontalCuts) + [h]
        vcuts = [0] + sorted(verticalCuts) + [w]
        max_area = 0
        for i in range(len(hcuts) - 1):
            for j in range(len(vcuts) - 1):
                area = (hcuts[i + 1] - hcuts[i]) * (vcuts[j + 1] - vcuts[j])
                max_area = max(area, max_area)
        return max_area % (10**9 + 7)