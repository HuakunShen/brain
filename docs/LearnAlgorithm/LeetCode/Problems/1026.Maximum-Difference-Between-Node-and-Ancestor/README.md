# 1026. Maximum Difference Between Node and Ancestor

Difficulty: Medium

Topic: Tree

Time: Beats: 90.66%


Single Word Hint: **highest**

The commented out part is a brute force solution with O(n^2) time complexity.

The non-commented out part has a O(n) time complexity.

The idea is, the descendent with max diff with current node has to be either lowest or highest seen so far. 

So we use a recursion function with 3 outputs: `lowest`, `highest`, `max_so_far`.


```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:

        def lowest_highest_max_so_far(root: Optional[TreeNode]) -> Tuple[int, int, int]:
            l_low, l_high, l_max = lowest_highest_max_so_far(root.left) if root.left else (root.val, root.val, 0)
            r_low, r_high, r_max = lowest_highest_max_so_far(root.right) if root.right else (root.val, root.val, 0)
            lowest, highest = min(l_low, r_low, root.val), max(l_high, r_high, root.val)
            _max = max(l_max, r_max)
            return lowest, highest, max(abs(root.val - lowest), abs(root.val - highest), _max)
        lowest, highest, max_ = lowest_highest_max_so_far(root)
        return max_
        # def helper(root: Optional[TreeNode]) -> Tuple[List[TreeNode], int]:
        #     if root is None:
        #         return [], 0
        #     descendents_left, max_left = helper(root.left)
        #     descendents_right, max_right = helper(root.right)
        #     descendents = descendents_left + descendents_right
        #     diffs = [abs(root.val - x) for x in descendents]
        #     return descendents + [root.val], max(max_left, max_right, max(diffs) if len(diffs) > 0 else 0)
    
        # return helper(root)[1]
```