/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func removeNodes(head *ListNode) *ListNode {
    var right []int
    temp := head
    for ; temp!=nil ;{
        right = append(right, temp.Val)
        temp = temp.Next
    }
    max := -1
    for i :=len(right)-1 ; i >=0 ; i-- {
        if right[i]>max{
            max = right[i]
        } else {
            right[i] = max
        }
    }

    temp = head
    prev := head
    prev = nil
    for i:=0; temp!=nil ; i++{
        if temp.Val < right[i] {
            if prev == nil {
                head = head.Next
            } else {
                prev.Next = temp.Next
            }
            temp = temp.Next
        } else {
            prev = temp
            temp = temp.Next
        }
    }
    return head

}