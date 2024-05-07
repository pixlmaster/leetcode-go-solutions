/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func doubleIt(head *ListNode) *ListNode {
    orig := head
    var parent []*ListNode
    prev := head
    prev = nil
    for  ; head!=nil; {
        parent = append(parent, prev)
        prev = head
        head = head.Next
    }
    n := len(parent)
    head = prev
    carry := 0
    for i:= n-1 ; i >=0 ; i--{
        // fmt.Println(head.Val)
        mult := head.Val*2 + carry
        head.Val = mult %10
        carry = mult/10
        // fmt.Println(head.Val, carry)
        head = parent[i]
    }
    // fmt.Println(carry)

    if carry !=0 {
        return &ListNode{carry,orig}
    }
    return orig

}