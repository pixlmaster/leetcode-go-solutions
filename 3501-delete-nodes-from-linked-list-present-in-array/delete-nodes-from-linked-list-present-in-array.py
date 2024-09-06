# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        numSet = set(nums)
        if not head:
            return head
        
        dummyNode = ListNode(-1, head)
        currNode = head
        prevNode = dummyNode
        while currNode:
            if currNode.val in numSet:
                # prev node points to 
                prevNode.next = currNode.next
                currNode = currNode.next
            else:
                prevNode = currNode
                currNode = currNode.next
            
        return dummyNode.next