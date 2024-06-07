# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # create a min heap , for each list insert the starting listnode (node.val,node)
        #  pop top most, put in a dummy list, if there is a next put in the heap
        heap =[]
        heapq.heapify(heap)
        hmap = {}        
        for node in lists:
            if node:
                heappush(heap,node.val)
                if node.val not in hmap :
                    hmap[node.val] = deque()
                    hmap[node.val].append(node)
                else:
                    hmap[node.val].append(node)
                
        dnode = ListNode(-1)
        itr = dnode
        
        while heap :
            minElem = heappop(heap)
            minNode = hmap[minElem].pop()
            itr.next = minNode
            itr= itr.next
            minNext = minNode.next
            if minNext:
                heappush(heap,minNext.val)
                if minNext.val not in hmap :
                    hmap[minNext.val] = deque()
                    hmap[minNext.val].append(minNext)
                else:
                    hmap[minNext.val].append(minNext)
            
        return dnode.next