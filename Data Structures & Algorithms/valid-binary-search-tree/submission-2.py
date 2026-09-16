# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        validBST = True
        def dsf(root, left, right):
            nonlocal validBST
            if not root:
                return None
            if not (left < root.val < right):
                validBST = False
            
            dsf(root.left, left, root.val)
            dsf(root.right, root.val, right)
        dsf(root, float('-inf'), float('inf'))
        return validBST