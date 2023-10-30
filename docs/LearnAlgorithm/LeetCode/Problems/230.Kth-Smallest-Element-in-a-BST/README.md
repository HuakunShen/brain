# 230. Kth Smallest Element in a BST

https://leetcode.com/problems/kth-smallest-element-in-a-bst/

**Level:** Medium (it's easy if you know the trick ([in-order traversal](../../../Technique/inorder-traversal.md)))


## Solution

$O(N)$ for both Time and Space Complexity.

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorder(node):
            if node:
                inorder(node.left)
                self.i += 1
                if self.i == k:
                    self.ret = node
                    return
                elif self.i > k:
                    return  # try to quit early
                inorder(node.right)
            
        self.i = 0
        self.ret = None
        inorder(root)
        return self.ret.val
```

## Official Solution

https://leetcode.com/problems/kth-smallest-element-in-a-bst/solution/

The official solution provides an iterative solution.

```python
class Solution:
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        stack = []
        
        while True:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if not k:
                return root.val
            root = root.right
```