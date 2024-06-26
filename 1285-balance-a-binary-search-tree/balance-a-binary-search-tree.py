class Solution:
    order = []
    
    def balanceBST(self, root: TreeNode) -> TreeNode:
        self.order = []
        self.inorder(root)
        return self.contruct(0,len(self.order)-1)

    def contruct(self, start: int, end: int) -> TreeNode:
        if end < 0 or start >= len(self.order) or start>end:
            return None
        mid = start + (end - start) // 2
        # print(start,end, mid)
        midNode = self.order[mid]
        midNode.left = self.contruct(start, mid-1)
        midNode.right = self.contruct(mid+1, end)
        return midNode
    def inorder(self, root: TreeNode) -> None:
        if not root:
            return
        self.inorder(root.left)
        self.order.append(root)
        self.inorder(root.right)