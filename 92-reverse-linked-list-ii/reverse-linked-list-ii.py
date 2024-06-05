# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        dhead = ListNode()
        dtail = dhead
        lbefore = None
        rafter = None

        itr = head
        count =1
        while itr :
            next = itr.next
            if count == left-1:
                lbefore = itr
            if count == right+1:
                rafter = itr
                break 
            if count>=left and count<=right:
                dtail = self.insertdhead(dhead,itr,dtail)
            # print(dhead)
            itr=next
            count+=1
        # print(rafter)
        if rafter:
            dtail.next = rafter

        if lbefore:
            lbefore.next = dhead.next
            return head
        
        return dhead.next


    
    def insertdhead(self,prev,node, tail):
        node.next = prev.next
        prev.next = node
        while tail.next:
            tail = tail.next
        return tail