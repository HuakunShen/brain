# 938. Range Sum of BST

https://leetcode.com/problems/range-sum-of-bst/description/

Difficulty: Easy

The soluton to this probelm is simply tree traversal with recursion.

O(N) time complexity to traverse the entire tree using recursion.

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if root is None:
            return 0
        return (root.val if low <= root.val <= high else 0) + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)

        # or single line
        # return 0 if root is None else (root.val if low <= root.val <= high else 0) + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)
```
