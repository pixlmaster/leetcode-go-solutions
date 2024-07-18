# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    parent = {}
    leaf = []

    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.parent = {}
        self.leaf = []
        """
        1. find all leaf nodes and store them in a list
        2. store the parent of each node along the way
        3. find the common ancestor for each pair of nodes
            if dist1 + dist2 = distance
                good pair ++
        """
        self.dfs(root, None)
        ans = 0
        for i in range(len(self.leaf)):
            for j in range(i + 1, len(self.leaf)):
                if self.shortestDist(self.leaf[i], self.leaf[j], distance):
                    ans += 1
        return ans

    def dfs(self, node: TreeNode, prev: TreeNode) -> None:
        if not node:
            return
        self.parent[node] = prev
        # found a leaf node
        if not node.left and not node.right:
            self.leaf.append(node)
            return
        self.dfs(node.left, node)
        self.dfs(node.right, node)

    def shortestDist(self, leaf1: TreeNode, leaf2: TreeNode, distance: int) -> int:
        deq1 = deque()
        deq2 = deque()
        self.travelToRoot(leaf1, deq1)
        self.travelToRoot(leaf2, deq2)
        if len(deq1) + len(deq2) < distance:
            return True
        while deq1 and deq2:
            if deq1[-1] != deq2[-1]:
                break
            deq1.pop()
            deq2.pop()
        if len(deq1) + len(deq2) <= distance:
            return True
        return False

    def travelToRoot(self, node: TreeNode, deq: deque[TreeNode]) -> None:
        while node:
            deq.append(node)
            node = self.parent[node]