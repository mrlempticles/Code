class Solution:
    def maxSubarraySum(self, nums, k):
        n = len(nums)
        prefix = 0
        best = [10**30] * k   # large initial value
        best[0] = 0           # prefix[0] = 0 at mod 0

        ans = -10**30

        for i in range(1, n+1):
            prefix += nums[i-1]
            mod = i % k
            
            ans = max(ans, prefix - best[mod])
            best[mod] = min(best[mod], prefix)

        return ans
