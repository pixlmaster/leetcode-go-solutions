"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node
        return copy.deepcopy(node)
    #     hmap = {}

    #     self.dfs(node,hmap)

    #     for node in hmap:
    #         newnode = hmap[node]
    #         for itr,child in enumerate(newnode.neighbors):
    #             newnode.neighbors[itr] = hmap[child]
    #         print("newnode",newnode.val)
    #         for child in  newnode.neighbors:
    #             print("child", child.val)
    #     return hmap[node]

    
    # def dfs(self,node,hmap):
    #     if not node or node in hmap:
    #         return
    #     neighbours =[]
    #     neighbours.extend(node.neighbors)
    #     newnode = Node(node.val, neighbours)
    #     hmap[node] = newnode

    #     # visit the children
    #     for child in node.neighbors :
    #         self.dfs(child,hmap)