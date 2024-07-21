# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> list[int]:
        if not head or not head.next:
            return [-1,-1]
        """
            iterate over the linkedList, store the lastIdx, firstIdx
            return[lastIdx - firstIdx, smallestDist]
        """
        smallestDist = float("inf")
        firstIdx = -1
        lastIdx = -1
        prev = head
        curr = prev.next
        next = curr.next
        currIdx = 1
        while next:
            # minima
            if (curr.val < prev.val and curr.val < next.val) or (curr.val > prev.val and curr.val > next.val):
                if firstIdx == -1:
                    firstIdx = currIdx    
                if lastIdx > 0:
                    smallestDist = min(smallestDist, currIdx - lastIdx)
                lastIdx = currIdx      
            prev = curr
            curr = next
            next = next.next
            currIdx += 1
        
        if smallestDist == float("inf"):
            return [-1,-1]
        
        return  [smallestDist,lastIdx - firstIdx]
