# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dhead = head
        while dhead:
            # print ("node", dhead.val)
            dhead = dhead.next
        if not head or not head.next:
            return head     
        # base case of 2 elements
        if not head.next.next:
            if head.val > head.next.val:
                head.next.next = head
                temp = head.next
                head.next = None
                return temp
            else:
                return head
        
        slowPtr = head
        fastPtr = head
        
        while fastPtr and fastPtr.next:
            slowPtr= slowPtr.next
            fastPtr =fastPtr.next.next
            
        # slowPtr will aprrox be in middle
        right =slowPtr.next
        slowPtr.next = None
        
        l1 = self.sortList(head)
        l2 = self.sortList(right)
        
        return self.merge(l1,l2)
    
    def merge(self, l1: ListNode, l2 : ListNode) ->ListNode:
        dnode = ListNode(-1)
        storeHead = dnode
        while l1 and l2:
            if l1.val < l2.val:
                dnode.next = l1
                dnode = dnode.next
                l1=l1.next
            else:
                dnode.next = l2
                dnode = dnode.next
                l2=l2.next
        
        if not l1 :
            dnode.next = l2
        if not l2 :
            dnode.next = l1
        
        return storeHead.next