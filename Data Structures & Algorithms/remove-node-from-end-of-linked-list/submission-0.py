# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Step 1: Create dummy node to simplify edge cases
        dummy = ListNode(0, head)
        first = second = dummy

        # Step 2: Move 'first' pointer n + 1 steps ahead
        for _ in range(n + 1):
            first = first.next

        # Step 3: Move both pointers until 'first' reaches the end
        while first:
            first = first.next
            second = second.next

        # Step 4: Remove the nth node from the end
        second.next = second.next.next

        # Step 5: Return new head
        return dummy.next
        