# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        iterate over the linked list
        keep summing, when you encounter node.val ==0 , assign it the sum, prev.next = node
        set node = node.next and reset the sum
        """


        prev = head
        orig = head

        head = head.next
        currSum = 0
        
        while head:
            # in case head is not 0 , simply add it and skip
            if head.val != 0:
                currSum+=head.val
                head=head.next
                continue
            # we reached a 0 value
            head.val = currSum
            currSum = 0
            prev.next = head
            prev = head
            head=head.next
            
        return  orig.next
        