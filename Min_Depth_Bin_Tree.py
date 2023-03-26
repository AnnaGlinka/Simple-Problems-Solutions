from typing import Optional

"""
https://leetcode.com/problems/minimum-depth-of-binary-tree/
While doing traversal, returns depth of the first encountered leaf node
O(n)
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        queue = []
        queue.append({'node': root, 'depth': 1})

        while len(queue)>0:
            current = queue.pop(0)
            current_node = current['node']
            current_depth = current['depth']

            if current_node.left is None and current_node.right is None:
                return current_depth

            if current_node.left is not None:
                queue.append({'node': current_node.left, 'depth': current_depth+1})

            if current_node.right is not None:
                queue.append({'node': current_node.right, 'depth': current_depth+1})


        
    


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(20)
root.right.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

root2 = TreeNode(3)
root2.right = TreeNode(20)
root2.right.right = TreeNode(7)
root2.right.right.right = TreeNode(3)

s = Solution()
print(s.minDepth(root))
print(s.minDepth(root2))
