# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        travel =[]
        self.inorder(root,travel)
        ans = float("inf")
        for i in range(1,len(travel)):
            ans = min(ans,abs(travel[i]-travel[i-1]))

        return ans
    
    def inorder(self, root: TreeNode, travel: [int]) -> None:
        if not root:
            return
        
        self.inorder(root.left, travel)
        travel.append(root.val)
        self.inorder(root.right, travel)