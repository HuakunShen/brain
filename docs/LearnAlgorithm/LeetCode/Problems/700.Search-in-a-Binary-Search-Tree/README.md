# 700. Search in a Binary Search Tree

https://leetcode.com/problems/search-in-a-binary-search-tree/

Level: Easy

## Solution

### Iterative Approach (while loop)

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        while root is not None:
            if root.val == val:
                return root
            root = root.left if val < root.val else root.right
        return root
```

### Recusive Approach

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
	"""
	Runtime: 79 ms, faster than 86.12% of Python3 online submissions for Search in a Binary Search Tree.
	Memory Usage: 16.4 MB, less than 74.05% of Python3 online submissions for Search in a Binary Search Tree.
	"""
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root or root.val == val:
            return root
        return self.searchBST(root.left if val < root.val else root.right, val)
```



