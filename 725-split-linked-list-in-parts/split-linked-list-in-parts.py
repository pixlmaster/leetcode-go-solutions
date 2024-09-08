class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        n = 0
        itr = head
        while itr:
            n += 1
            itr = itr.next

        numElems = n // k
        numsLeft = n % k
        ans = []
        totalElems = 0
        while totalElems < n:
            currElems = 0
            if head:
                currElems = 1
            else:
                break
            ans.append(head)
            itr = head
            while currElems < numElems and itr:
                currElems += 1
                totalElems += 1
                itr = itr.next
            print(currElems)
            print(itr.val)
            # add 1 extra for carry
            if numsLeft > 0 and itr:
                currElems+=1
                totalElems += 1
                numsLeft-=1
                if numElems !=0:
                    itr = itr.next
            
            if itr:
                head = itr.next
            else:
                head= itr
            if itr:
                itr.next = None

        while len(ans) < k :
            ans.append(None)

        return ans

