# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.dfs(root,p,q)[0]
    
    def dfs(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> tuple(['TreeNode', bool, bool]):
        if not root:
            return tuple([None,False,False])
        left = self.dfs(root.left, p, q)
        # both on left, ancestor found, pass it up
        if left[1] and left[2]:
            return tuple([left[0], True, True])
        # both on right, ancestor found, pass it up
        right = self.dfs(root.right, p ,q)
        if right[1] and right[2]:
            return tuple([right[0], True, True])

        # found p and q on either subtree, this si the common ancestor
        if (left[1] and right[2]) or (left[2] and right[1]):
            return tuple([root,True, True])

        left1 = left[1] or right[1] or root == p
        right1 = left[2] or right[2] or root ==q
        ans = tuple([None,left1,right1])
        # print(root.val, ans)
        if left1 and right1:
            return tuple([root,True,True])

        return ans