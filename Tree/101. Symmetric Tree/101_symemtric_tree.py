# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        """
            Iterative Approach:
            Algorithm for checking whether a binary tree is a mirror of itself using an iterative approach and a stack:

            Create a stack and push the root node onto it twice.
            While the stack is not empty, repeat the following steps:
            a. Pop two nodes from the stack, say node1 and node2.
            b. If both node1 and node2 are null, continue to the next iteration.
            c. If one of the nodes is null and the other is not, return false as it is not a mirror.
            d. If both nodes are not null, compare their values. If they are not equal, return false.
            e. Push the left child of node1 and the right child of node2 onto the stack.
            f. Push the right child of node1 and the left child of node2 onto the stack.
            If the loop completes successfully without returning false, return true as it is a mirror.
        """
        from collections import deque
        stack = deque()
        if root is None:
            return True
        stack.append(root)
        stack.append(root)
        while stack:
            # a. Pop two nodes from the stack, say node1 and node2.
            node1 = stack.pop()
            node2 = stack.pop()
            
            #  b. If both node1 and node2 are null, continue to the next iteration.
            if node1 == None and node2 == None:
                continue
            # c. If one of the nodes is null and the other is not, return false as it is not a mirror.
            if node1 == None  or node2 == None:
                return False 
            # d. If both nodes are not null, compare their values. If they are not equal, return false.
            if  node1.val != node2.val:
                return False

            # e.  Push the left child of node1 and the right child of node2 onto the stack.
            stack.append(node1.left)
            stack.append(node2.right)
            #  f. Push the right child of node1 and the left child of node2 onto the stack. 
            stack.append(node1.right)
            stack.append(node2.left)
        return True
            