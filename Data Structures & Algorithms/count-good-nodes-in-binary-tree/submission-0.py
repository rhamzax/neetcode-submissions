# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        goodNodes = 0

        def dsf(root, maxAbove):
            nonlocal goodNodes
            if not root:
                return 0
            
            if root.val >= maxAbove:
                goodNodes += 1

            maxAbove = max(root.val, maxAbove)
            dsf(root.left, maxAbove)
            dsf(root.right, maxAbove)
        
        dsf(root, root.val - 1)
        return goodNodes
