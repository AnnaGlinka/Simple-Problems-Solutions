from typing import Optional, List
from queue import Queue

"""
https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
O(N) 
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        n = len(nums)
        middle = len(nums) // 2
        root = TreeNode(nums[middle])
        q = Queue()
        q.put((root, (0, middle-1)))
        q.put((root, (middle+1, n-1)))
        
        while not q.empty():
            current = q.get()
            parent = current[0]
            left = current[1][0]
            right = current[1][1]

            if left <= right and parent is not None:
                middle = (right + left) // 2
                child = TreeNode(nums[middle])

                print("L=",left,"R=",right, "parent->child=",parent.val,"->",child.val)

                if nums[middle] < parent.val:
                    parent.left = child
                else:
                    parent.right = child

                q.put((child, (left, middle-1)))
                q.put((child, (middle+1, right)))
 
        
        return root


s = Solution()
print(s.sortedArrayToBST([-10,-3,0,5,9,10,20,40,50]).right.right.val)