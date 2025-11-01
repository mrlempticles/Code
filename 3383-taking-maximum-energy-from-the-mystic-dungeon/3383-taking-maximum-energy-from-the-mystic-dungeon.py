class Solution:
    def maximumEnergy(self, energy, k):
        n = len(energy)
        dp = energy[:]  # start with base values
        
        # fill from back to front
        for i in range(n - k - 1, -1, -1):
            dp[i] += dp[i + k]
        
        # answer = best total starting from any i
        return max(dp)
