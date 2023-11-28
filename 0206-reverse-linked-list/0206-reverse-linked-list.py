# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(root):
            nonlocal head
            if not root or not root.next:
                head=root
                return
            reverse(root.next)
            ahead=root.next
            ahead.next=root
            root.next=None
        reverse(head)
        return head
        