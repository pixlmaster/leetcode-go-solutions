class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        """
        1. Do DFS from root to start
            do DFS from root to end
        2.  both return deque of  integers
        3.  along the DFS store the parent of the nodes
        4. use the deques to figure out the common ancestor
        5. if common ancestor = start -> traverse from start to end
        6. if common ancestor = end -> travserse up from start to end
        7. else traverse up from start to common ancestor, then down to the destination

        """
        startDeq = deque()
        destDeq = deque()

        self.dfs(root, startValue, startDeq)
        self.dfs(root, destValue, destDeq)
        # print(startDeq)
        # print(destDeq)

        commonNode = self.findCommonAncestor(startDeq, destDeq)
        ans = ""
        # print(startDeq)
        # travel up to common ancestor
        while startDeq.pop() != commonNode:
            ans += "U"
        ansDeq = deque()
        # print(ans)
        # travel down to destNode via DFS
        self.dfs2(commonNode, destValue, ansDeq)
        # print(ans2)
        # print(ans)
        return ans + "".join(list(ansDeq))


    def dfs2(self, root: TreeNode, target: int, path: deque[str]) -> bool:
        # reached end of dfs
        if not root:
            return False
        if root.val == target:
            return True
        path.append("L")
        leftPath = self.dfs2(root.left, target, path)
        if leftPath:
            return True
        path.pop()
        path.append("R")
        rightPath = self.dfs2(root.right, target, path)
        if rightPath:
            return True
        path.pop()
        return False

    def dfs(self, root: TreeNode, target: int, deq: deque[TreeNode]) -> TreeNode:
        # reached end of dfs
        if not root:
            return None
        if root.val == target:
            deq.append(root)
            return root

        deq.append(root)
        # found in left subtree or right subtree
        left = self.dfs(root.left, target, deq)
        if left:
            return left
        right = self.dfs(root.right, target, deq)
        if right:
            return right
        # else pop node from path
        deq.pop()
        return None

    def findCommonAncestor(self, startDeq: deque[int], endDeq: deque[int]) -> TreeNode:
        prev = None
        startDeqCopy = startDeq.copy()

        while 1 and len(startDeqCopy) >0 and len(endDeq):
            start = startDeqCopy.popleft()
            end = endDeq.popleft()
            if start != end:
                break
            prev = start
        return prev