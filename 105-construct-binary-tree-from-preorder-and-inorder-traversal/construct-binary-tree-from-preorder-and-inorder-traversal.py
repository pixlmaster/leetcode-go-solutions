# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        curr = preorder[0]
        # print(preorder,inorder)
        # print(curr)
        inIdx = inorder.index(curr)

        root = TreeNode(curr)
        root.left = self.buildTree(preorder[1:(inIdx+1)],inorder[:inIdx])
        root.right = self.buildTree(preorder[(inIdx+1):],inorder[inIdx+1:])
        return root