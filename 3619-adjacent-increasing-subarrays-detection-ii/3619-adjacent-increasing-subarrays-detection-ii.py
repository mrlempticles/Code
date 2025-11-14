class Solution:
    def maxIncreasingSubarrays(self, nums):
        n = len(nums)

        # Step 1: Compute inc[i] = length of strictly increasing streak starting at i
        inc = [1] * n
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                inc[i] = inc[i + 1] + 1

        # Step 2: Binary search for max k
        def ok(k):
            # Check if any i forms two adjacent increasing subarrays of length k
            for i in range(n - 2 * k + 1):
                if inc[i] >= k and inc[i + k] >= k:
                    return True
            return False

        left, right = 1, n // 2
        ans = 0

        while left <= right:
            mid = (left + right) // 2
            if ok(mid):
                ans = mid
                left = mid + 1   # Try bigger k
            else:
                right = mid - 1  # Try smaller k

        return ans
