# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # Helper function to check if two subtrees are mirrors of each other
        def isMirror(t1: Optional[TreeNode], t2: Optional[TreeNode]) -> bool:
            # Base cases
            if not t1 and not t2:  # If both nodes are None, they are mirrors
                return True
            if not t1 or not t2:  # If only one is None, they are not mirrors
                return False
            if t1.val != t2.val:  # If their values are different, they are not mirrors
                return False
            
            # Recursive case: Compare left of t1 with right of t2, and right of t1 with left of t2
            return isMirror(t1.left, t2.right) and isMirror(t1.right, t2.left)
        
        # Start the recursion by comparing the left and right subtrees of the root
        return isMirror(root, root)
