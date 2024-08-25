class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        visit left
        visit right
        visit root
        """
        ans = []
        self.traverse(root, ans)
        return ans

    def traverse(self, root: TreeNode, ans: list[int]) -> None:
        if not root:
            return
        self.traverse(root.left, ans)
        self.traverse(root.right, ans)
        ans.append(root.val)
        return 