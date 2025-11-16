class Solution:
    def modifiedList(self, nums, head):
        to_delete = set(nums)

        # Dummy node handles deletion of head cleanly
        dummy = ListNode(0, head)
        current = dummy

        while current and current.next:
            if current.next.val in to_delete:
                current.next = current.next.next
            else:
                current = current.next

        return dummy.next
   