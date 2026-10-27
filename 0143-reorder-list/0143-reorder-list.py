
class Solution(object):
    def reorderList(self, head):
        if not head or not head.next:
            return

        slow = head
        fast = head

        # Find the middle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse the second half
        curr = slow.next
        slow.next = None
        prev = None

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        # Merge both halves
        first = head
        second = prev

        while second:
            next_first = first.next
            next_second = second.next

            first.next = second
            second.next = next_first

            first = next_first
            second = next_second
