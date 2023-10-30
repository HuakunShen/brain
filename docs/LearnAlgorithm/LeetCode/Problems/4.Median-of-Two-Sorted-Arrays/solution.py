from typing import List


class Solution0:
    """
    Runtime: 104 ms, faster than 56.39% of Python3 online submissions for Median of Two Sorted Arrays.
    Memory Usage: 14.1 MB, less than 33.79% of Python3 online submissions for Median of Two Sorted Arrays.
    >>> sol = Solution0()
    >>> sol.findMedianSortedArrays([1, 3, 5, 7, 9], [2, 4, 6, 8, 10])
    5.5
    >>> sol.findMedianSortedArrays([1, 3], [2])
    2.0
    >>> sol.findMedianSortedArrays([1, 3, 5], [])
    3.0
    """

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr, i, j = [], 0, 0
        # merge
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                arr.append(nums1[i])
                i += 1
            else:
                arr.append(nums2[j])
                j += 1
        if i < len(nums1):
            arr.extend(nums1[i:])
        elif j < len(nums2):
            arr.extend(nums2[j:])
        total_len = len(arr)
        mid = total_len // 2
        if total_len % 2 == 1:
            return arr[mid]
        else:
            return (arr[mid - 1] + arr[mid]) / 2

    def findMedianSortedArrays1(self, nums1: List[int], nums2: List[int]) -> float:
        nums1_len, nums2_len = len(nums1), len(nums2)
        if nums1_len > nums2_len:
            return self.findMedianSortedArrays1(nums2, nums1)
        low, high = 0, nums1_len
        while low <= high:
            # select a partition in nums1
            p1 = (low + high) // 2
            # select a partition in nums2 based on the previous partition
            p2 = (nums1_len + nums2_len + 1) // 2 - p1
            max1 = -float("inf") if p1 == 0 else nums1[p1 - 1]
            max2 = -float("inf") if p2 == 0 else nums2[p2 - 1]
            min1 = float("inf") if p1 == nums1_len else nums1[p1]
            min2 = float("inf") if p2 == nums2_len else nums2[p2]
            if max1 <= min2 and max2 <= min1:  # partition satisfied
                if (nums1_len + nums2_len) % 2 == 1:
                    return max(max1, max2)
                else:
                    return (max(max1, max2) + min(min1, min2)) / 2
            elif max1 > min2:  # binary search left
                high = p1 - 1
            else:
                low = p1 + 1


if __name__ == "__main__":
    # import doctest
    #
    # doctest.testmod(verbose=True)
    sol = Solution0()
    print(sol.findMedianSortedArrays1([1, 3], [2]))
