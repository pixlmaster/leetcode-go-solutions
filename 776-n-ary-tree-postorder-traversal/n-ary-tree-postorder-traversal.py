"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> list[int]:
        ans = []
        self.traverse(root, ans)
        return ans

    def traverse(self, root: 'Node', ans: list[int]) -> None:
        if not root:
            return

        for child in root.children:
            self.traverse(child, ans)

        ans.append(root.val)

        