# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if not root:
            return 0
        if root.val > R:
            return self.rangeSumBST(root.left, L, R)
        if root.val < L:
            return self.rangeSumBST(root.right, L, R)
        return self.rangeSumBST(root.left, L, R) + root.val + self.rangeSumBST(root.right, L, R)