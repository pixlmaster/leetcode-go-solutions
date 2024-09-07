class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        """
        find the first element of the the list and find the nodes which have this value, has them
        Try DFS with them and see if you find, if does not match, do early exit
        """
        if self.dfs(head, root, head.val) :
            return True
        return False
        
    def dfs(self, head : ListNode, root : TreeNode, firstVal: ListNode) -> bool:
        if not root:
            return False
        if root.val == firstVal:
            check = self.checkPath(head, root)
            print(root.val,check)
            if check:
                return True
        left = self.dfs(head, root.left, firstVal)
        right = self.dfs(head, root.right, firstVal)
        return left or right
    
    def checkPath(self, head : ListNode, root : TreeNode) -> bool:
        if not head:
            return True
        if not root:
            return False
        # print(root, head.val)
        if root.val == head.val :
            return self.checkPath(head.next, root.left) or self.checkPath(head.next, root.right)
        else:
            return False