
class Solution:
    def connect(self, root):
        if not root:
            return None

        level_start = root

        while level_start:
            dummy = Node(0)
            tail = dummy
            curr = level_start

            while curr:
                if curr.left:
                    tail.next = curr.left
                    tail = tail.next

                if curr.right:
                    tail.next = curr.right
                    tail = tail.next

                curr = curr.next

            level_start = dummy.next

        return root
