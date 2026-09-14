# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        seen = []

        def bsf(root):
            nonlocal seen
            if root:
                seen.append(root.val)
            else:
                seen.append(None)
                return
            bsf(root.left)
            bsf(root.right)
        bsf(p)
        p = seen
        seen=[]
        bsf(q)
        return p == seen
            