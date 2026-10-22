
class Solution:
    def recoverTree(self, root):
        first = second = prev = None
        curr = root

        while curr:
            if curr.left is None:
                # Process current node
                if prev and prev.val > curr.val:
                    if first is None:
                        first = prev
                    second = curr

                prev = curr
                curr = curr.right

            else:
                # Find inorder predecessor
                pred = curr.left

                while pred.right and pred.right != curr:
                    pred = pred.right

                if pred.right is None:
                    # Create temporary thread
                    pred.right = curr
                    curr = curr.left
                else:
                    # Remove temporary thread
                    pred.right = None

                    if prev and prev.val > curr.val:
                        if first is None:
                            first = prev
                        second = curr

                    prev = curr
                    curr = curr.right

        # Restore the two swapped values
        first.val, second.val = second.val, first.val
