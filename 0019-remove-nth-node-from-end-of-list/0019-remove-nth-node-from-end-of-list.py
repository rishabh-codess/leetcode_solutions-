# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        fast = slow = dummy

        # Advance fast pointer by n + 1 steps
        for _ in range(n + 1):
            fast = fast.next

        # Move fast to the end, maintaining the gap
        while fast is not None:
            fast = fast.next
            slow = slow.next

        # Bypass the nth node from the end
        slow.next = slow.next.next

        return dummy.next
        