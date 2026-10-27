
class Solution(object):
    def sortList(self, head):
        if not head or not head.next:
            return head

        # Step 1: Find the middle
        slow = head
        fast = head
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # Step 2: Split into two lists
        prev.next = None

        # Step 3: Sort both halves
        left = self.sortList(head)
        right = self.sortList(slow)

        # Step 4: Merge the sorted halves
        dummy = ListNode(0)
        curr = dummy

        while left and right:
            if left.val <= right.val:
                curr.next = left
                left = left.next
            else:
                curr.next = right
                right = right.next

            curr = curr.next

        if left:
            curr.next = left
        else:
            curr.next = right

        return dummy.next
