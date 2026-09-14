# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced = True

        def bsf(root):
            nonlocal balanced

            if not root:
                return 0
            
            left = bsf(root.left)
            right = bsf(root.right)
            balanced = balanced and abs(left - right) <= 1
            return 1 + max(left, right)
        bsf(root)
        return balanced

            