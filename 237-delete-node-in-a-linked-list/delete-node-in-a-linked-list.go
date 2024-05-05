/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func deleteNode(node *ListNode) {
    next1 := node.Next
    // next2 := next1.Next
    node.Val = next1.Val
    node.Next = next1.Next
}