# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.inorder = []
        self.itr = -1
        self.traverse(root,self.inorder)
        self.n = len(self.inorder)


    def next(self) -> int:
        self.itr+=1
        return self.inorder[self.itr]
        

    def hasNext(self) -> bool:
        if self.itr + 1 < self.n:
            return True
        return False

    def traverse(self,root: TreeNode, curr: List[int]) -> None:
        if not root:
            return
        self.traverse(root.left,curr)
        curr.append(root.val)
        self.traverse(root.right,curr)
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()