# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: list[int]) -> list[TreeNode]:
        """
        1. do a DFS with prev tracked
        2. when value in to_delete
        3. delete the value
        4. and store the children in the map[children.val] = children (if none and not set)
        """
        toDeleteSet = set(to_delete)
        rootMap = set()
        if root.val not in toDeleteSet:
            rootMap.add(root)
        self.dfs(root,None,toDeleteSet,rootMap)
        return rootMap

    def dfs(self, node: TreeNode, prev: TreeNode, to_delete: set[int], rootMap: set[TreeNode]) -> None:
        if not node:
            return
        
        if node.val in to_delete:
            # delete the value
            if prev:
                if prev.left == node:
                    prev.left = None
                else:
                    prev.right = None
            # add it's children to the values
            if node.left and node.left.val not in to_delete:
                rootMap.add(node.left)
            if node.right and node.right.val not in to_delete:
                rootMap.add(node.right)
        
        self.dfs(node.left, node, to_delete, rootMap)
        self.dfs(node.right, node, to_delete, rootMap)
