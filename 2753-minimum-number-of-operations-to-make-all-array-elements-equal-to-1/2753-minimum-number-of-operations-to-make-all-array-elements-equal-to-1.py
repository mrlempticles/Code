class Solution:
    def minOperations(self, nums):
        n = len(nums)
        
        # Custom gcd because importing math.gcd may not be allowed
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        # Case 1: array already has 1
        ones = nums.count(1)
        if ones > 0:
            return n - ones
        
        # Case 2: find shortest subarray with gcd = 1
        min_len = float('inf')
        
        for i in range(n):
            g = nums[i]
            for j in range(i + 1, n):
                g = gcd(g, nums[j])
                if g == 1:
                    min_len = min(min_len, j - i + 1)
                    break
        
        if min_len == float('inf'):
            return -1
        
        return (min_len - 1) + (n - 1)
