class Solution(object):
    def combinationSum3(self, k, n):
        result = []

        def backtrack(start, path, total):

            # We have selected k numbers
            if len(path) == k:
                if total == n:
                    result.append(path[:])
                return

            # Try numbers from start to 9
            for num in range(start, 10):

                # Don't exceed the target
                if total + num > n:
                    break

                path.append(num)

                backtrack(
                    num + 1,
                    path,
                    total + num
                )

                path.pop()

        backtrack(1, [], 0)

        return result