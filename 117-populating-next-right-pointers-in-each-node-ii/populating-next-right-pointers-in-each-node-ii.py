"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        q = deque()
        q.append(root)
        n=1
        while len(q) > 0:
            newn=0
            count = 0
            level=[]
            prev= None
            while count < n :
                # pop leftmost from the queue
                node = q.popleft()
                # set the prev next if not already set
                if prev:
                    prev.next = node
                # update prev for next node
                prev = node
                count+=1
                # put children for next iteration
                if node.left:
                    q.append(node.left)
                    newn+=1
                if node.right:
                    q.append(node.right)
                    newn+=1
            node.next = None
            n=newn
        
        return root

