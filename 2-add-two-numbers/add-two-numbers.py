# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        h1 = l1
        h2 = l2
        carry = 0
        prev=None
        while h1 and h2:
            sum = h1.val + h2.val +carry
            carry = int(sum/10)
            h1.val = sum % 10

            prev = h1
            h1= h1.next
            h2 = h2.next

        if not h1:
            prev.next = h2
        
        h1 = prev.next
        while h1:
            sum =h1.val +carry
            carry = int(sum/10)
            h1.val = sum % 10
            prev=h1
            h1 = h1.next

        

        # both lists have ended
        if not h1 :
            if carry :
                prev.next=ListNode(carry)
        return l1
        
        

