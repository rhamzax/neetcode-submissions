# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float('-inf')
        def dsf(root) -> int:
            nonlocal res
            if not root:
                return 0
            
            #Split Compute
            left = dsf(root.left)
            right = dsf(root.right)

            calculatedMax = left + right + root.val
            if root.val > calculatedMax:
                calculatedMax = root.val
            elif left <= 0 and right > 0:
                calculatedMax = right + root.val
            elif right <= 0 and left > 0:
                calculatedMax = left + root.val
            res = max(calculatedMax, res)

            #Return Max Compute
            return max(left, right, 0) + root.val
        dsf(root)
        return res