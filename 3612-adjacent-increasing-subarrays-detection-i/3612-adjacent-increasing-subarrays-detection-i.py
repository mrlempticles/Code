class Solution(object):
    def hasIncreasingSubarrays(self, nums, k):
        n = len(nums)
        
        for a in range(n - 2*k + 1):
            # check first subarray
            ok1 = all(nums[i] < nums[i+1] for i in range(a, a+k-1))
            if not ok1:
                continue

            # check second subarray
            b = a + k
            ok2 = all(nums[i] < nums[i+1] for i in range(b, b+k-1))

            if ok2:
                return True
        
        return False
