# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        travel =[]
        self.inorder(root,travel)
        return travel[k-1]
    
    def inorder(self, root: TreeNode, travel: [int]) -> None:
        if not root:
            return
        
        self.inorder(root.left, travel)
        travel.append(root.val)
        self.inorder(root.right, travel)