/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

func add(l1 *ListNode, l2 *ListNode, l1prev *ListNode, l2prev *ListNode, carry int) {
    // Edge cases
    // 1st loop of recursion will never have l1 and l2 as null and l1prev and l2prev will be null
    if l2 == nil {
        if carry == 0 {
            // 2nd number is finished and there is no carry, do nothing
            return
        }
        // there is a carry
        // set the carry as a new node of l2 and continue recursion
        carry = 0
        l2 = &ListNode{1, nil}
        l2prev.Next = l2
        add(l1, l2, l1prev, l2prev, 0)
        return
    }

    if l1 == nil {
        if carry == 0 {
            // 1st number ended, there is no more addition to be performed
            // set the pointer of ending of the 1st list to the 2nd
            l1 = l2
            l1prev.Next = l1
            return
        }
        // there is a carry
        // set the carry as a new node of l1 and continue recrusion
        carry = 0
        l1 = &ListNode{1, nil}
        l1prev.Next = l1
        add(l1, l2, l1prev, l2prev , 0)
        return
    }

    // fmt.Println(l1.Val, l2.Val, carry)

    // both nodes exist
    sum := l1.Val + l2.Val + carry
    carry = sum/10
    l1.Val = sum%10
    add(l1.Next, l2.Next, l1 , l2, carry)
    return
}


func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
    if l1 == nil {
        return l2
    }
    if l2 == nil {
        return l1
    }

    add(l1,l2,nil,nil,0)

    return l1
    
}