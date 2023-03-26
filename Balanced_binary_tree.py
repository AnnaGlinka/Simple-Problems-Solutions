from typing import Optional

"""
https://leetcode.com/problems/balanced-binary-tree/
The height of a node is the number of edges present in the 
longest path connecting that node to a leaf node.

https://www.youtube.com/watch?v=Yt50Jfbd8Po&t=1s
O(N)

"""


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def height(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
      
        left_height = self.height(root.left)
        if left_height == -1:
            return -1
        right_height = self.height(root.right)
        if right_height == -1:
            return -1
        if abs(left_height - right_height) > 1:
            return -1
            
        return max(left_height, right_height) + 1

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        return self.height(root) != -1


#root = [3,9,20,null,null,15,7]
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(20)
root.right.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

root2 = TreeNode(3)
root2.left = TreeNode(9)
root2.right = TreeNode(20)
root2.right.left = TreeNode(15)
root2.right.right = TreeNode(7)
root2.right.right.right = TreeNode(3)

s = Solution()
#print(s.isBalanced(root))
print(s.isBalanced(root2))
