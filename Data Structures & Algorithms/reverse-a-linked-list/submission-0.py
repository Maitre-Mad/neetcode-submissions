 #Definition for singly-linked list.
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous = None
        current = head

        # Check against None
        while current is not None:
            next_node = current.next
            
            # Point the current node backwards
            current.next = previous
            
            # Step forward
            previous = current
            current = next_node
            
        return previous
        