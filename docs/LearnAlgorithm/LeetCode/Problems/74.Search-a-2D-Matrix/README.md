# 74. Search a 2D Matrix

https://leetcode.com/problems/search-a-2d-matrix/

Level: Medium (I believe it's an Easy)

## Solution 1

The algorithm is super easy, go through every row, for each row check the first and last number.
If target is in range of current row, then break and search this row only.

Time and Space Complexity are O(n) and O(1) (ignoring input variables)

```python
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            if matrix[i][0] <= target <= matrix[i][-1]:
                break
        return target in matrix[i]

```

## Solution 2

Time Complexity: O(log2(n))

The matrix is sorted both within row and among rows.

Use binary search to find the target row. This should be faster when there are many rows.

```python
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # use binary search to find the first row whose first number < target
        # and last number > target
        s, e = 0, len(matrix) - 1
        m = (s + e) // 2
        while s <= e:
            if matrix[m][-1] < target:
                # Search forward
                s = m + 1
            elif matrix[m][0] > target:
                # Search backward
                e = m - 1
            else:
                break
            m = (s + e) // 2
        return target in matrix[m]
```


## Test Cases

```
[[1,3,5,7],[10,11,16,20],[23,30,34,60]]
3
[[1],[3]]
3
[[1,3,5,7],[10,11,16,20],[23,30,34,50]]
30
[[1]]
2
[[1],[3]]
4
```