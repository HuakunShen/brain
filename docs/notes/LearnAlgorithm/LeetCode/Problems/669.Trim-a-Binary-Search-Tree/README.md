# 669. Trim a Binary Search Tree

[TOC]



https://leetcode.com/problems/trim-a-binary-search-tree/

Level: Medium 

Comment: Looks difficult at first glance, but should be Easy once you understand how to do it with Recursion

I wrote down what I was thinking in the method docstring, it should be enough to understand.

The keyword of this problem is just **Recursion**.

For recursion, always analyze the problem and come up with the base case and recursive step. 
Then it will become super simple.

## Solution

<!-- <img src="assets/image-20220416032801190.png" alt="image-20220416032801190" style="width:50%;" /> -->
![assets/image-20220416032801190.png](assets/image-20220416032801190.png)

### Python

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
	"""
	Runtime: 55 ms, faster than 80.40% of Python3 online submissions for Trim a Binary Search Tree.
	Memory Usage: 17.9 MB, less than 83.03% of Python3 online submissions for Trim a Binary Search Tree.
	"""
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        """
        Property of binary tree, elements on the left are all smaller than root, and elements on the right larger (including all descendents)
        So the first step should be finding the first node that lies in range and use it as root.
        Is it possible the other half of the tree also has nodes in range?
            No, because if current node in range and any node on ther other side is in range, current node's parent must be in range.
        After finding the root with DFS, we need to find the left and right children.
        For left children, we want to find the subtree in range (low, root.val). 
        Note: the immediate child could be smaller than low, so we can use recusion so solve this.
        Find the first node that satisfies the condition and append it to root.
        Do the same for the right child.
        Recusive step is pretty straight forward, all the cases will need to be handled by the base case.
        "root is None" is a base case. If root doesnt' for in range, then search one side of the tree recursively.
		This step is kind of base case + recursive step. I classify it as recursive step as it makes a recursive call.
        """
        # Base Case
        if root is None:
            return None  
        # Recursive Step
        elif root.val < low:
            return self.trimBST(root.right, low, high)
        elif root.val > high:
            return self.trimBST(root.left, low, high)
        else:
            # in range
            root.left = self.trimBST(root.left, low, root.val)
            root.right = self.trimBST(root.right, root.val, high)
            return root
```

## Test Cases

```
[1,0,2]
1
2
[3,0,4,null,2,null,null,1]
1
3
```

## Solution in Other Languages

```go
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func trimBST(root *TreeNode, low int, high int) *TreeNode {
    if root == nil {
        return nil
    } else if root.Val < low {
        return trimBST(root.Right, low, high)
    } else if root.Val > high {
        return trimBST(root.Left, low, high)
    } else {
        root.Left = trimBST(root.Left, low, root.Val)
        root.Right = trimBST(root.Right, root.Val, high)
        return root
    }
}
```

### Golang

```go
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func trimBST(root *TreeNode, low int, high int) *TreeNode {
    if root == nil {
        return nil
    } else if root.Val < low {
        return trimBST(root.Right, low, high)
    } else if root.Val > high {
        return trimBST(root.Left, low, high)
    } else {
        root.Left = trimBST(root.Left, low, root.Val)
        root.Right = trimBST(root.Right, root.Val, high)
        return root
    }
}
```

### Java

```java
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public TreeNode trimBST(TreeNode root, int low, int high) {
        if (root == null) {
            return null;
        } else if (root.val < low) {
            return trimBST(root.right, low, high);
        } else if (root.val > high) {
            return trimBST(root.left, low, high);
        } else {
            root.left = trimBST(root.left, low, root.val);
            root.right = trimBST(root.right, root.val, high);
            return root;
        }
    }
}
```

### C++

```cpp
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    TreeNode* trimBST(TreeNode* root, int low, int high) {
        if (root == NULL) {
            return NULL;
        } else if (root->val < low) {
            return trimBST(root->right, low, high);
        } else if (root->val > high) {
            return trimBST(root->left, low, high);
        } else {
            root->left = trimBST(root->left, low, root->val);
            root->right = trimBST(root->right, root->val, high);
            return root;
        }
    }
};
```

### JavaScript

```js
/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @param {number} low
 * @param {number} high
 * @return {TreeNode}
 */
var trimBST = function(root, low, high) {
    if (!root) {
        return null;
    } else if (root.val < low) {
        return trimBST(root.right, low, high);
    } else if (root.val > high) {
        return trimBST(root.left, low, high);
    } else {
        root.left = trimBST(root.left, low, root.val);
        root.right = trimBST(root.right, root.val, high);
        return root;
    }
};
```

### C#

```cs
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int val=0, TreeNode left=null, TreeNode right=null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
public class Solution {
    public TreeNode TrimBST(TreeNode root, int low, int high) {
        if (root == null) {
            return null;
        } else if (root.val < low) {
            return this.TrimBST(root.right, low, high);
        } else if (root.val > high) {
            return this.TrimBST(root.left, low, high);
        } else {
            root.left = this.TrimBST(root.left, low, root.val);
            root.right = this.TrimBST(root.right, root.val, high);
            return root;
        }
    }
}
```

### Swift

```swift
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public var val: Int
 *     public var left: TreeNode?
 *     public var right: TreeNode?
 *     public init() { self.val = 0; self.left = nil; self.right = nil; }
 *     public init(_ val: Int) { self.val = val; self.left = nil; self.right = nil; }
 *     public init(_ val: Int, _ left: TreeNode?, _ right: TreeNode?) {
 *         self.val = val
 *         self.left = left
 *         self.right = right
 *     }
 * }
 */
class Solution {
    func trimBST(_ root: TreeNode?, _ low: Int, _ high: Int) -> TreeNode? {
        if (root == nil) {
            return nil;
        } else if (root!.val < low) {
            return self.trimBST(root!.right, low, high);
        } else if (root!.val > high) {
            return self.trimBST(root!.left, low, high);
        } else {
            root?.left = self.trimBST(root!.left, low, root!.val);
            root?.right = self.trimBST(root!.right, root!.val, high);
            return root;
        }
    }
}
```

